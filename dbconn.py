import mysql.connector

# Replace these values with your database information
hostname = "localhost"
username = "umesh"
password = "User@123"
database_name = "employee_db"

# Connect to the database
connection = mysql.connector.connect(
    host=hostname,
    user=username,
    password=password,
    database=database_name
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Example query: select all data from the table
select_query = "INSERT INTO annual_package (employee_id, year, annual_salary, working_days) VALUES (20, 2024, 90000.00, 1000),(21, 2024, 80000.00, 1000);"

# Execute the query
cursor.execute(select_query)
connection.commit()

# Fetch all rows from the result set
rows = cursor.fetchall()


# # Display the retrieved data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()



