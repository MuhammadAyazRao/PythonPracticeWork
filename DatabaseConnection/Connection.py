import pyodbc

server = 'DESKTOP-01LQ3IF'
database = 'Python_db'
username = ''
password = ''

def get_db_connection():
    #conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'
   
    try:
        conn = pyodbc.connect(conn_str)
        print("SuccessFull")
        return conn
        
    except pyodbc.Error as e:
        print(f"Error: {e}")
        return None
    