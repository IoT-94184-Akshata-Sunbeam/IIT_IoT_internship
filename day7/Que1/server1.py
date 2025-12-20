from flask import Flask ,request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server=Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/sensor_readings')
def create_sensor_readings():
    id=request.form.get('id')
    temprature=request.form.get('temprature')
    humidity=request.form.get('humidity')
    timestamp=request.form.get('timestamp')

    query=f"insert into sensor_readings values('{id}', '{temprature}','{humidity}','{timestamp}');"

    executeQuery(query=query)

    return "reading is added successfully "

@server.get('/sensor_readings')
def retrieve_sensor_readings():

    query="select * from sensor_readings"
    data=executeSelectQuery(query=query)

    return f"temperature:{data}"

@server.put('/sensor_readings')
def update_sensor_readings():
   temprature=request.form.get('temprature')
   humidity=request.form.get('humidity')

   query=f"update sensor_readings SET humidity='{humidity}' where temprature='{temprature}';"

   executeQuery(query=query)

   return "reading is updated successfully"

@server.delete('/sensor_readings')
def delete_sensor_readings():
    temprature=request.form.get('temprature')

    query=f"delete from sensor_readings where temprature={temprature};"

    executeQuery(query=query)
    return "reading is deleted successfully"


@server.get('/sensor_readings/below')
def below_threshold():
    threshold = request.form.get('temprature')

    query = f"""
    SELECT * FROM sensor_readings
    WHERE temprature < {threshold};
    """

    data = executeSelectQuery(query=query)
    return f"{data}"

if __name__=='__main__':
    server.run(host='0.0.0.0',port=4000,debug=True)