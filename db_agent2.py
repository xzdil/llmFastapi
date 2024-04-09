db_url="postgresql://intern:assa_2023@192.168.10.120:5432/drm"

from test import llm

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    select,
)

engine = create_engine(url)
metadata_obj = MetaData()

from llama_index.core import SQLDatabase
sql_database = SQLDatabase(engine)

from llama_index.core.query_engine import NLSQLTableQueryEngine

query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database, tables=["city_stats"], llm=llm
)
