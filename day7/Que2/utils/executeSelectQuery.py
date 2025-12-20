from utils.dbconnection import dbconnection

def executeSelectQuery(query):

    connection=dbconnection()

    cursor=connection.cursor()

    cursor.execute(query)
    data=cursor.fetchall()


   

    cursor.close()
    connection.close()

    return data
    