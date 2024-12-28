import psycopg2

# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    1,      # minimum number of connections
    10,     # maximum number of connections
    user="username",
    password="password",
    host="localhost",
    port="5432",
    database="database_name"
)

# Get a connection from the pool
connection = connection_pool.getconn()

# Use the connection
cursor = connection.cursor()
cursor.execute("SELECT * FROM my_table")
result = cursor.fetchall()

# Return the connection to the pool
connection_pool.putconn(connection)