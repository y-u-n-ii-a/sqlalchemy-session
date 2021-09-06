from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import SQLALCHEMY_DATABASE_URI


engine = create_engine(SQLALCHEMY_DATABASE_URI)

if __name__ == '__main__':
    session = Session(engine, autoflush=False, autocommit=False)
    print()
    session.commit()
    print('hello')
