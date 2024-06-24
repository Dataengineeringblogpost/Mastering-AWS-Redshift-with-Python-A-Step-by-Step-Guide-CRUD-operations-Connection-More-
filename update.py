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
cursor.execute(f"""UPDATE {Table_name} SET name ='Sara' WHERE id = 1 """)
results = cursor.execute(f"""select * from {Table_name} """)

data = results.fetchall()   

for row in data:
    print(row)

cursor.close()

conn.close()