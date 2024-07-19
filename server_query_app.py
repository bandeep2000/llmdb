"""
Application that queries server db using NLP with LLMs and outputs the results with sql query used
Please ensure you have OPENAI_API_KEY set in env variables
"""
import os
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
import streamlit as st
from config_vars import sample_queries,db_file

api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise EnvironmentError("The OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
     
# connect to db
if not os.path.isfile(db_file):
    raise FileNotFoundError("Database file not found")
db = SQLDatabase.from_uri(f"sqlite:///{db_file}")

#openai_model = "gpt-4o-mini"
openai_model = "gpt-3.5-turbo"
# create open ai llm
#llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
llm = ChatOpenAI(model=openai_model, temperature=0)

# initilize sql agent to run queries
agent = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True,agent_executor_kwargs = {"return_intermediate_steps": True})

# Streamlit UI
st.title("CMDB Query Assistant")

query = st.text_input(
    "Enter your question about the CMDB:",
    placeholder=f"e.g., {sample_queries[1]}"
)

if query:
    try:
         with st.spinner("Executing query..."):
            # Execute the agent to get SQL and result
            response = agent.invoke(query)

            # display sql query to the user
            sql_query = []
            for (log, output) in response["intermediate_steps"]:
                if log.tool == 'sql_db_query':
                    sql_query.append(log.tool_input)
            # if still not initialized some error ccouured
            if not sql_query:
                raise Exception("Seem some error happened,may be input is not valid")
            st.code(sql_query, language="sql")

            # write the LLM response #
            st.header("LLM Response")
            st.write(response["output"])
            print(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")



