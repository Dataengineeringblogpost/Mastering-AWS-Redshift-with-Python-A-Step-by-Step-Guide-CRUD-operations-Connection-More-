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

cursor.execute(f"""INSERT INTO {Table_name} (id, name) VALUES (1, 'KARTHIK')""")

print("Data inserted succesfully")

cursor.close()

conn.close()