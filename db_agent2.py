db_url="postgresql://intern:password@192.168.10.120:5432/drm"

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    select,
)

engine = create_engine(db_url)
metadata_obj = MetaData()

from llama_index.core import SQLDatabase
sql_database = SQLDatabase(engine)
