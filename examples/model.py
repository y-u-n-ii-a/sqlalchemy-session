import sqlalchemy as sa
from sqlalchemy import func, MetaData, orm

meta = MetaData()
Base = orm.declarative_base(metadata=meta)


class User(Base):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sa.Column(sa.String(100))
    created_at = sa.Column(sa.DateTime(), default=func.now())

    def __str__(self):
        return "<User {id}: {name}>".format(id=self.id, name=self.name)

    def print_state(self, msg: str = ''):
        print(msg)
        ins = sa.inspect(self)
        print(f"{self} status: \033[36m", end="")
        if ins.transient:
            print("transient\n")
        elif ins.pending:
            print("pending\n")
        elif ins.persistent:
            print("persistent\n")
        elif ins.deleted:
            print("deleted\n")
        elif ins.detached:
            print("detached\n")
        print('\033[38m', end='')
