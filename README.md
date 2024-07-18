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

3. **Create  sample server database**:

    ```sh
    python3 create_cmdb.py
    ```
    This will create a sample sqlite db - cmdb.db


## Usage

### Running the CLI to find food item

To start the application, use the following command:

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