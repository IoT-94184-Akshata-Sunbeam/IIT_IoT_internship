from utils.dbconnection import dbconnection

def executeQuery(query):

    connection=dbconnection()

    cursor=connection.cursor()

    cursor.execute(query)

    connection.commit()

    cursor.close()
    connection.close()