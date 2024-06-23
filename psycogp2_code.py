import psycopg2


# Establish a connection to the Redshift cluster
conn = psycopg2.connect(
    dbname='dev',
    user='awsuser',
    password='Karthiksara2123',
    host='redshift-cluster-2.czcdbl82hrrx.us-east-1.redshift.amazonaws.com',
    port='5439'
)
print("Connection to Redshift established successfully.")

cursor = conn.cursor()

query = 'SELECT * FROM "dev"."public"."listing" limit 5;'  

results = cursor.execute(query)

data = cursor.fetchall()

for row in data:
    print(row)