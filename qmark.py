import redshift_connector 

host_name = 'redshift-cluster-2.czcdbl82hrrx.us-east-1.redshift.amazonaws.com'

conn = redshift_connector.connect(
        host=host_name, 
        port= 5439,
        database= "my_db",
        user='awsuser',
        password='Karthiksara2123'
     )
conn.autocommit = True

cursor =conn.cursor()

cursor.paramstyle = 'qmark'

Table_name = "Customer_data"
# Insert data
cursor.execute('INSERT INTO Customer_data(id, name) VALUES(?, ?)', (3, "Sara"))
print("Data inserted succesfully")
cursor.execute('SELECT * FROM Customer_data')
results = cursor.fetchall()
for row in results:
    print(row)
# Select data
cursor.execute('SELECT * FROM Customer_data WHERE id = ?', (3,))
results = cursor.fetchall()
for row in results:
    print(row)

# Update data
cursor.execute('UPDATE Customer_data SET id = ? WHERE name = ?', (3, "karthik"))
print("DATA UPDATED SUCCESSFULLY ouput below:- ")
cursor.execute('SELECT * FROM Customer_data')
results = cursor.fetchall()
for row in results:
    print(row)

# Delete data
cursor.execute('DELETE FROM Customer_data WHERE id = ?', (3,))
print("Data Deleted ouput below:- ")
cursor.execute('SELECT * FROM Customer_data')
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()

conn.close()