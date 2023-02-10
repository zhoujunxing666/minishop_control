#main
import database

if __name__ == "__main__":
    cnx = database.connect_to_database()
#fix it
    # Do some database operations
    cursor = cnx.cursor()
    query = "SELECT * FROM table"
    cursor.execute(query)

    database.close_database_connection(cnx)
