from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///user_database.db")
with open("user_database.sql","r") as sql_file:
    lines = sql_file.readlines()
    transaction = "".join(lines)
    sql_file.close()
with engine.connect() as conn:
    conn.execute(text(transaction))