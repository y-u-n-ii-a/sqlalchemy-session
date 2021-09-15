import sqlalchemy as sa
from sqlalchemy.orm import Session

from model import User, meta
from config import SQLALCHEMY_DATABASE_URI

engine = sa.create_engine(SQLALCHEMY_DATABASE_URI)

if __name__ == "__main__":
    meta.create_all(engine)
    session = Session(engine, autoflush=False, autocommit=False)

    # object states
    user = User(name="eva")
    user.print_state("User created")

    session.add(user)  # new
    user.print_state("User added")

    session.flush()  # in identity map
    user.print_state("Session flushed")

    session.commit()  # in identity map
    user.print_state("Session commited")

    user.name = "sasha"  # dirty
    user.print_state("User name changed")

    session.rollback()
    user.print_state("Session rolled back")

    session.delete(user)
    user.print_state("User deleted")

    session.commit()  # deleted
    user.print_state("Session commited")
