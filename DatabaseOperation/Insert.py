from DatabaseConnection import Connection

def InsertData():     
    conn = Connection.get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()

            # Define your INSERT query
            insert_query = "INSERT INTO Test (Name) VALUES (?)"

            # Define the values to be inserted
            values_to_insert = ("Ayaz")

            # Execute the INSERT query
            cursor.execute(insert_query, values_to_insert)

            # Commit the transaction (required to save the changes)
            conn.commit()

            print("Insertion successful!")

        except Exception as e:
            print(f"Database error: {e}")
        finally:
            conn.close()