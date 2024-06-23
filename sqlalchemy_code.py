from sqlalchemy import create_engine, text

from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgresql+psycopg2://awsuser:Karthiksara2123@redshift-cluster-2.czcdbl82hrrx.us-east-1.redshift.amazonaws.com:5439/dev'
)


Session = sessionmaker(bind=engine)

print("Creating a session...")
# Create a Session
session = Session()

print("Session created successfully.")

query = text("SELECT * FROM dev.public.listing limit 5;")       

result = session.execute(query)

Data = result.fetchall()

for row in Data:
    print(row)
  
print("Data recieved Sucessfully")

