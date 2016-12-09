import yaml
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__all__ = ['engine', 'Session', 'Base', 'session']

with open('config.yaml') as f:
    config_yaml = yaml.load(f)

engine = create_engine(config_yaml['db'])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
