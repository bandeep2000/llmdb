FROM python:3.9-slim

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# COPY files
COPY cmdb.db server_query_app.py config_vars.py . 

EXPOSE 8501

CMD [ "streamlit", "run", "server_query_app.py" ]
