# Server Database Query Assistant

This Streamlit UI application allows users to query the server database using natural language Processing(NLP). It leverages the power of  OpenAI and LangChain sql agents to interpret user queries and generate appropriate SQL statements and outputs.

It creates a sample server database and allows you to query using NLP queries. It can be modified to connect to a different database.


## Installation

1. **Clone the repository**:

    ```
    git clone git@github.com:bandeep2000/llmdb.git
    cd llmdb
    ```


2. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```
    *Note:* This assumes you have python 3.8 installed

3. **SET open api key in env variable**:
     ```export OPENAI_API_KEY=<your key> ```

3. **Create  sample server database**:

    ```sh
    python3 create_cmdb.py
    ```
    This will create a sample sqlite db - cmdb.db

    It creates 3 tables - servers, applications, newtwork_interfaces - with primary and foreign key relationships

    Some sample db data output:

    ```
    sqlite> select * from servers;
    1|win-srv-01|192.168.1.10|Windows|Server 2019|8|64|1000|NYC|Production|2024-07-18 18:32:25.242319
     2|ubuntu-srv-01|192.168.1.20|Ubuntu|20.04 LTS|4|32|500|NYC|Production|2024-07-18 18:32:25.243818

    sqlite> SELECT * FROM applications;
    1|SQL Server|2019|2021-01-01 00:00:00.000000|1
    2|IIS|10|2021-01-01 00:00:00.000000|1
    3|MySQL|8.0|2021-02-01 00:00:00.000000|2
    ...

    sqlite> SELECT * FROM network_interfaces;
    1|eth0|09:1A:2B:..|192.168.1.10|1
    ...
    
    ```


## Usage

### Start the application


**streamlit run server_query_app.py**


This will open app on your localhost http://localhost:8501/

### Run the queries to get server details

Applications opens a form and allows user to run queries

Some sample queries are:

  "How many Windows servers do we have?",
  "List all Ubuntu servers with their RAM and disk space.",
  "What applications are installed on the server with IP 192.168.1.10?",
  "Show me all servers in the Production environment.",
  "Which server has the most CPU cores?"

## References:

https://python.langchain.com/v0.1/docs/use_cases/sql/agents/
