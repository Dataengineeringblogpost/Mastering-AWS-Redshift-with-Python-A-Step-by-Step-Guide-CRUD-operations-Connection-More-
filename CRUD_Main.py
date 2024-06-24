import redshift_connector
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Optional: Add file handler for logging to a file
file_handler = logging.FileHandler('crud_operations.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class RedshiftClient:
    def __init__(self, Host , Port , Database , User, Password):
        self.Host = Host
        self.Port = Port
        self.Database = Database
        self.User = User
        self.Password = Password
        self.connection = None

    def connect(self):
        try:
            logger.info("Connecting to Redshift...")
            self.connection = redshift_connector.connect(
                host=self.Host,
                port=self.Port,
                database=self.Database,
                user=self.User,
                password=self.Password
            )
            self.connection.autocommit = True
            logger.info("Connected to Redshift.")
        except Exception as e:
            logger.error(f"Failed to connect to Redshift: {e}")
            raise
    
    def execute_command(self,Command):
        cursor = self.connection.cursor()

        result = cursor.execute(Command)

        return  result


    def fetch_data(self, Table_name):
        
        query = f"SELECT * FROM {Table_name}"
        
        logger.info(f"Executing query: {query}")
    
        result = self.execute_command(query)

        data = result.fetchall()

        for row in data:
            logging.info(row)

        return f"Query executed successfully. Fetched {len(data)} rows."
        

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            logger.info("Connection to Redshift closed.")

if __name__ == "__main__":

    Host_Name = "redshift-cluster-2.czcdbl82hrrx.us-east-1.redshift.amazonaws.com"

    Port_Number = 5439

    Database_Name = "my_db"

    User_Name = "awsuser"

    Password = "Karthiksara2123"

    client = RedshiftClient(
        Host = Host_Name,
        Port = Port_Number,
        Database = Database_Name,
        User = User_Name,
        Password = Password
    )

    try:
        
        client.connect()
        Table_Name = "Customer_data"
        Condition = "id = 2"
        data = client.fetch_data(Table_name = Table_Name ,)
        
    finally:

        client.close_connection()