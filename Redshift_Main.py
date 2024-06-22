import redshift_connector

host_name = 'redshift-cluster-2.czcdbl82hrrx.us-east-1.redshift.amazonaws.com'

conn = redshift_connector.connect(
        host=host_name, 

        port= 5439,

        database='dev',
        
        user='awsuser',
        
        password='Karthiksara2123'
     )

conn.autocommit = True

cursor =conn.cursor()

result = cursor.execute('SELECT * FROM "dev"."public"."listing" limit 5;')

data = result.fetchall()   

for row in data:
    print(row)

cursor.close()

conn.close()