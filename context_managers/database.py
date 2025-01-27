import psycopg2

class DatabaseContextManager:
    def __init__(self, connection_string: str):
        self.connection = psycopg2.connect(connection_string)
    
    def __enter__(self):
        return self.connection.cursor()

    def __exit__(self, error: Exception, value: object, trackback: object):
        self.connection.commit()
        self.connection.close()
    

def main():
    with DatabaseContextManager("database_string") as cursor:
        cursor.execute("SELECT * FROM users;")
        res = cursor.fetchall()

    print(res)

if __name__ == "__main__":
    main()
