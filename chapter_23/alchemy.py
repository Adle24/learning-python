import sqlalchemy


conn = sqlalchemy.create_engine("sqlite:///:memory:")

meta = sqlalchemy.MetaData()
zoo = sqlalchemy.Table(
    "zoo",
    meta,
    sqlalchemy.Column("critter", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("count", sqlalchemy.Integer),
    sqlalchemy.Column("damages", sqlalchemy.Float),
)

meta.create_all(conn)

with conn.connect() as conn:
    conn.execute(zoo.insert())
    result = conn.execute(zoo.select())
    rows = result.fetchall()
    print(rows)
