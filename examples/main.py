import sqlalchemy as sa
from sqlalchemy.orm import Session

from config import SQLALCHEMY_DATABASE_URI
from model import meta, User

engine = sa.create_engine(SQLALCHEMY_DATABASE_URI)


if __name__ == "__main__":
    meta.create_all(engine)

    session = Session(engine, autoflush=False, autocommit=False)

    # identity map
    user1 = session.query(User).filter_by(id=1).first()
    user2 = session.query(User).filter_by(id=1).first()
    print(user2 is user1)

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

    session.expire(user)
    user.print_state("User expired")

    session.delete(user)
    user.print_state("User deleted")

    session.commit()
    user.print_state("Session commited")
