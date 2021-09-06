import sqlalchemy as sa
from sqlalchemy import func, MetaData, orm

meta = MetaData()
Base = orm.declarative_base(metadata=meta)


class User(Base):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sa.Column(sa.String(100))
    created_at = sa.Column(sa.DateTime(), default=func.now())

    def __repr__(self):
        return "<Person {id}: {name}>".format(
            id=self.id, name=self.name
        )
