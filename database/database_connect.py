import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings_env import name_database

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, name_database)
path_database = f'sqlite:///{db_path}'

engine = create_engine(path_database)
session = sessionmaker(engine)
