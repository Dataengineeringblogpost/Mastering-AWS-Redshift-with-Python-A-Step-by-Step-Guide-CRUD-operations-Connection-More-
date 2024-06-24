import redshift_connector # To connect redshift to python (connector)

host_name = 'redshift-cluster-2.czcdbl82hrrx.us-east-1.redshift.amazonaws.com'

conn = redshift_connector.connect(
        host=host_name, 
        port= 5439,
        database= "dev",
        user='awsuser',
        password='Karthiksara2123'
     )
conn.autocommit = True

cursor =conn.cursor()
DataBase_Name = "My_DB"
cursor.execute(f"create DATABASE {DataBase_Name}")

print("Database created succesfully")

cursor.close()

conn.close()