import os
from dotenv import load_dotenv
from few_shots import few_shots
from langchain.llms import GooglePalm
from langchain.utilities import (SQLDatabase)

from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

from langchain.chains.sql_database.prompt import _mysql_prompt,PROMPT_SUFFIX,MYSQL_PROMPT
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate



class FewShotDBChain:
    load_dotenv()
    def __init__(self):
        self.palm_api_key   = os.getenv('PALM_API_KEY')
        self.db_user        = os.getenv('db_user')
        self.db_password    = os.getenv('db_password')
        self.db_host        = os.getenv('db_host')
        self.db_name        = os.getenv('db_name')
        self.db_uri         = f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}"
        self.db             = SQLDatabase.from_uri(self.db_uri, sample_rows_in_table_info=3)
        self.llm            = GooglePalm(google_api_key=self.palm_api_key, temperature=0.65)

    def create_chain(self, few_shots):
        self.few_shots          = few_shots
        self.embeddings         = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        example_prompt     = PromptTemplate(input_variables=['Question', 'SQLQuery', 'SQLResult', 'Answer'],
                                                 template='\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}',)
        to_vectorize            = [' '.join(sent.values()) for sent in self.few_shots]
        vectorstore        = Chroma.from_texts(to_vectorize, self.embeddings, metadatas=self.few_shots)
        example_selector   = SemanticSimilarityExampleSelector(vectorstore=vectorstore, k=2)

        few_shot_prompt    = FewShotPromptTemplate(example_selector=example_selector,                                                        
                                                        example_prompt=example_prompt,
                                                        prefix=_mysql_prompt,
                                                        suffix=PROMPT_SUFFIX,
                                                        input_variables=['input', 'table_info', 'top_k'])
        chain = SQLDatabaseChain.from_llm(llm=self.llm,
                                            db=self.db,
                                            verbose=True,
                                            prompt=few_shot_prompt)
        return chain
    
if __name__ == "__main__":
    few_    = FewShotDBChain()
    chain   = few_.create_chain(few_shots=few_shots)
    chain.run('Which country recorded the leaset CO2 emissions in 1997,and what its incomegroup name')
        