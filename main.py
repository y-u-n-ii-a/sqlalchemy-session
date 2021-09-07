from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import SQLALCHEMY_DATABASE_URI
from model import meta, User

engine = create_engine(SQLALCHEMY_DATABASE_URI)

if __name__ == '__main__':
    meta.create_all(engine)

    session = Session(engine, autoflush=False, autocommit=False)
    session.begin()
    print()
    user = User()
    user.name = 'yuniia'
    session.flush()
    session.commit()
