import psycopg2
from .config import PostgreSQL

# Global module variable of a single connection
connection = None
def init():
    """ Required to be called before invoking any submodule """
    global connection
    connection = SQLConnection()

def close():
    """ Clean up database connection"""
    global connection
    if connection is not None:
        connection.close()
        connection = None

# Internal class used by database API. 
# Instance of class exposed through connection variable.
class SQLConnection:
    """ An API Wrapper to the PostgreSQL database"""
    
    def __init__(self):
        """ Open a connection to the database """
        self.logging = PostgreSQL.get('logging')

        if self.logging:
            print("Opening connection to database.")

        self.raw_connection = psycopg2.connect( \
            dbname=PostgreSQL.get('database'), \
            user=PostgreSQL.get('username'), \
            password=PostgreSQL.get('password'), \
            host=PostgreSQL.get('server'), \
            connect_timeout=5)
        
        if self.logging:
            print("Connection opened successfully")

    def save_data(self, query, args):
        """ 
        Save data to the database. 
        Params: query (string), args (tuple of values)
        Returns: None
        """
        cursor = self.raw_connection.cursor()
        sql_statment = cursor.mogrify(query, args)
        
        if self.logging:
            print("Executing statement: ", sql_statment)
        cursor.execute(sql_statment)
        self.raw_connection.commit()

        cursor.close()
    
    def get_data(self, query, args):
        """ 
        Return data from the database.
        Params: query (string), args (tuple of values)
        Returns: the query result
        """
        cursor = self.raw_connection.cursor()
        sql_statment = cursor.mogrify(query, args)
        
        if self.logging:
            print("Executing statement: ", sql_statment)
        
        cursor.execute(sql_statment)

        results = cursor.fetchall()
        
        if self.logging:
            print("Results: ", results)

        cursor.close()
        return results

    def close(self):
        """ Close the connection to the database """
        self.raw_connection.close()
