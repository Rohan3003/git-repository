import pyodbc
SERVER = "Rohan_ASUS"
DATABASE = "test"
USERNAME = "rohan"
PASSWORD = "Sqlserver@3003"

connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes;Encrypt=yes'
print(connection_string)
conn = pyodbc.connect(connection_string)

SQL_QUERY = """
SELECT * FROM table_name
"""
# -> cursors are basically used to navigate the rows of a table and fetch the data.
# -> It serves as a pointer to navigate through the result set

# creating a cursor
cursor = conn.cursor()
cursor.execute(SQL_QUERY)


# fetchone(), fetchall(), fetchmany() are some of cursor methods.