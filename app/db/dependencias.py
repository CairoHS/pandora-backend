from sqlalchemy.orm import sessionmaker
from sqlmodel import Session as BaseSession
from .conn import engine
from contextlib import contextmanager

# Para podef fazer varias sessões
SessionLocal = sessionmaker(class_= BaseSession, autocommit=False, autoflush=False, bind=engine)

def pega_session():
    return SessionLocal()
