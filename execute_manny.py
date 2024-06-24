import redshift_connector # To connect redshift to python (connector)

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

Table_name = "Customer_data"
data = [
            (1, 'John Doe'),
            (2, 'Jane Smith'),
            (3, 'Alice Johnson')
        ]
cursor.executemany(f"INSERT INTO {Table_name} (id, name) VALUES (%s, %s)",data)
print("Data inserted successfully")

cursor.close()
conn.close()