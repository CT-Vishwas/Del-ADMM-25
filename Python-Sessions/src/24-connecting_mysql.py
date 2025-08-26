import mysql.connector

# Replace with your actual MySQL credentials
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'Northwind'
}

try:
    conn = mysql.connector.connect(**config)
    print("Connected to MySQL database 'Northwind'")
    # Your database operations go here
    my_cursor = conn.cursor()

    select_query = "SELECT * FROM Employees"

    my_cursor.execute(select_query)
    records = my_cursor.fetchall() # fetchone(), fetchmany(size=n)
    print(f"Total number of rows in Employees table: {my_cursor.rowcount}")
    for row in records:
        print(row)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed.")