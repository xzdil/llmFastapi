from langchain_community.utilities import SQLDatabase
from test import llm
db = SQLDatabase.from_uri(f'postgresql://intern:{password}@192.168.10.120:5432/drm')

from langchain_community.agent_toolkits import create_sql_agent
          
agent = create_sql_agent(llm, db=db, verbose=True)
