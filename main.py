from few_shots import few_shots
from langchain_supporter import FewShotDBChain
import streamlit as st


st.title("World Co2 Emission: Database Q&A")

question = st.text_input("Queastion: ")
if question :
    few_    = FewShotDBChain()
    chain   = few_.create_chain(few_shots=few_shots)
    answer  = chain.run(str(question))
    st.header('Answer : ')
    st.write(answer)
