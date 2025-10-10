import duckdb
import pandas

zoo_dict = {
    "name": ["bear", "cat", "dog"],
    "count": [2, 3, 1],
    "ent": [2000.0, 13.2, 1340.1],
}

my_db = pandas.DataFrame.from_dict(zoo_dict)

results = duckdb.sql("SELECT * FROM my_db").df()
print(results)
