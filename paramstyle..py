import redshift_connector

# Connection details
host_name = 'redshift-cluster-2.czcdbl82hrrx.us-east-1.redshift.amazonaws.com'
port = 5439
database = "my_db"
user = 'awsuser'
password = 'Karthiksara2123'

# Establish connection
conn = redshift_connector.connect(
    host=host_name, 
    port=port,
    database=database,
    user=user,
    password=password
)
conn.autocommit = True
cursor = conn.cursor()

# Numeric style example
cursor.paramstyle = 'numeric'
insert_query_numeric = """
INSERT INTO Customer_data(id, name) VALUES (:1, :2)
"""
data_to_insert_numeric = [(1, 'A'), (2, 'B'), (3, 'C')]

for data in data_to_insert_numeric:
    cursor.execute(insert_query_numeric, data)

# Named style example
cursor.paramstyle = 'named'
insert_query_named = """
INSERT INTO Customer_data(id, name) VALUES (:id, :name)
"""
data_to_insert_named = {"id": 4, "name": "David"}
cursor.execute(insert_query_named, data_to_insert_named)

# Format style example
cursor.paramstyle = 'format'
insert_query_format = """
INSERT INTO Customer_data(id, name) VALUES (%s, %s)
"""
data_to_insert_format = (5, "Eve")
cursor.execute(insert_query_format, data_to_insert_format)

# Pyformat style example
cursor.paramstyle = 'pyformat'
insert_query_pyformat = """
INSERT INTO Customer_data(id, name) VALUES (%(id)s, %(name)s)
"""
data_to_insert_pyformat = {"id": 6, "name": "Frank"}
cursor.execute(insert_query_pyformat, data_to_insert_pyformat)

# Select and fetch data
cursor.execute('SELECT * FROM Customer_data')
results = cursor.fetchall()
for row in results:
    print(row)

print("Data inserted successfully")

# Close connection
conn.close()
