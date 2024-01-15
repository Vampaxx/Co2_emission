# Co2_emission Database Q&A with GooglePalm

Building an end-to-end Language Model (LLM) project integrating Google Palm and Langchain for interaction with a MySQL database, specifically focused on CO2 emissions data, is an exciting endeavor. This project aims to enhance user experience by allowing natural language queries, which are then translated into SQL queries for execution on the underlying MySQL database.

1. User Interaction:
Users can interact with the system using natural language queries about CO2 emissions. For example:

    - "Which country emitted the most CO2 in 2002?"
    - "How many countries emitted between 4.25 and 20 CO2 units in 2010?"

2. Language Understanding:
Utilize the language model (Google Palm) to parse and understand the user's input. Extract key information such as the target year, emission range, and specific requirements.


## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/Vampaxx/Co2_emission.git
```
2.Navigate to the project directory:

```bash
  cd 'project directory'
```
3. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
4.Acquire an api key through makersuite.google.com and put it in .env file

```bash
  GOOGLE_API_KEY="your_api_key_here"
```

## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser where you can ask questions. It in the localHost

## Sample Questions
1. which country has maximum co2 emission in the year of 2002?
2. Which country had the maximum CO2 emissions in the year 2002, and to which income group category do they belong?
3. how many countries emit co2 in the range of 4.25 to 20 in the year of 2010?
4. No of countries emit co2 in the range of 1.25 to 15 in the year of 2010 AND 1990?
5. Identify the number of countries that exceeded 2 standard deviations in 2013?
6. Identify the countries that exceeded 2 standard deviations in 2013?
7. Identify the total countries that exceeded 2 standard deviations in 2013 and 2015?
8. Which country recorded the highest CO2 emissions in 2020,and what its emission value?
