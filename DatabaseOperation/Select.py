from DatabaseConnection import Connection

def GetData():     
    conn = Connection.get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()

            # Define your INSERT query
            select_query = "SELECT * from Test"

            # Execute the SELECT query
            cursor.execute(select_query)

            # Fetch the results
            results = cursor.fetchall()

            # Process the results
            for row in results:
                print(f"Id: {row.Id}, Name: {row.Name}")
                
        except Exception as e:
            print(f"Database error: {e}")
        finally:
            conn.close()