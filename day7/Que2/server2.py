from flask import Flask ,request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server=Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/soil_moisture')
def create_moisture():
    sensor_id=request.form.get('sensor_id')
    moisture =request.form.get('moisture')
    DateAndTime=request.form.get('DateAndTime')

    query=f"insert into moisture values('{ sensor_id}', '{ moisture }','{DateAndTime}');"

    executeQuery(query=query)

    return "reading is added successfully "

@server.get('/soil_moisture')
def retrieve_moisture():

    query="select * from moisture"
    data=executeSelectQuery(query=query)

    return f"moisture:{data}"

@server.put('/soil_moisture')
def update_moisture():
   sensor_id=request.form.get('sensor_id')
   moisture =request.form.get('moisture')

   query=f"update moisture SET moisture='{moisture}' where sensor_id='{sensor_id}';"

   executeQuery(query=query)

   return "reading is updated successfully"

@server.delete('/soil_moisture')
def delete_moisture():
    sensor_id=request.form.get('sensor_id')

    query=f"delete from moisture where sensor_id={sensor_id};"

    executeQuery(query=query)
    return "reading is deleted successfully"


@server.get('/soil_moisture/below')
def below_threshold():
    threshold = request.form.get('moisture')

    query = f"""
    SELECT * FROM moisture
    WHERE moisture < {threshold};
    """

    data = executeSelectQuery(query=query)
    return f"{data}"

if __name__=='__main__':
    server.run(host='0.0.0.0',port=4000,debug=True)