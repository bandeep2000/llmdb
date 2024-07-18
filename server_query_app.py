"""
Application that queries server db using NLP with LLMs and outputs the results with sql query used
Please ensure you have OPENAI_API_KEY set in env variables
"""
import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
import streamlit as st
from queries import sample_queries

api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise EnvironmentError("The OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
     
#TODO change this to read uri, create exception if not able to conn
# Load DB and OpenAI llm
engine = create_engine("sqlite:///cmdb.db", echo=True, future=True)
db = SQLDatabase(engine)
#db.run("SELECT * FROM employees LIMIT 10;")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# initilize sql agent to run queries
agent = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True,agent_executor_kwargs = {"return_intermediate_steps": True})

# Streamlit UI
st.title("CMDB Query Assistant")

# TODO  modify create_engine, create dockerfile
# readme should have details of db with foreigh key

query = st.text_input(
    "Enter your question about the CMDB:",
    placeholder=f"e.g., {sample_queries[1]}"
)

if query:
    try:
         with st.spinner("Executing query..."):
            # Execute the agent to get SQL and result
            response = agent.invoke(query)

            # get sql query details 
            sql_query = []
            for (log, output) in response["intermediate_steps"]:
                if log.tool == 'sql_db_query':
                    sql_query.append(log.tool_input)
            # if still not initialized some error ccouured
            if not sql_query:
                raise Exception("Seem some error happened,may be input is not valid")
            st.code(sql_query, language="sql")

            # write the LLM response
            st.header("LLM Response")
            st.write(response["output"])
            print(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")



