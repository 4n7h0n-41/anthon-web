import sys

import psycopg2
from psycopg2.extras import DictCursor


class Database:

    def connect(self):
        """
        Connect to database and return connection
        """
        print("Connecting to PostgreSQL Database...")
        try:
            conn = psycopg2.connect(
                host='localhost',
                dbname='anthon',
                user='anthon',
                password='anthon',
                port='5432'
            )
        except psycopg2.OperationalError as e:
            print(f"Could not connect to Database: {e}")
            sys.exit(1)

        return conn


database = Database()
db_connection = database.connect()


def run_query(sql, params=None):
    # Establish connection
    with db_connection as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql, params)

            # If the SQL command is a SELECT statement, fetch the results
            if cur.description:
                return cur.fetchall()
            else:
                return None
