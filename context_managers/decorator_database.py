import logging
import psycopg2
from contextlib import contextmanager


@contextmanager
def open_db(connection_string: str):
    conn = psycopg2.connect(connection_string)
    try:
        logging.info("Creating connection")
        yield conn.cursor()
    finally:
        logging.info("Closing connection")
        conn.commit()
        conn.close()


def main():
    logging.basicConfig(level=logging.INFO)
    with open_db("database_string") as cursor:
        cursor.execute("SELECT * FROM users;")
        logging.info(cursor.fetchall())


if __name__ == "__main__":
    main()
