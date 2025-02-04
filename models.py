from datetime import datetime
from sqlalchemy import Column, Integer, String, Text,
DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime,
default=datetime.utcnow)
    updated_at = Column(DateTime,
onupdate=datetime.utcnow)

def init_db():
    engine = create_engine('mysql+mysqlconnector:username:password@locreate_engine('mysql+mysqlconnector://mysql1:password1@localhost/mysql')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
