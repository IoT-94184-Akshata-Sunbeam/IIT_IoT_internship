from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)


@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"



@server.post('/home')
def create_status():
    id           = request.form.get('id')           
    light_status = request.form.get('light_status')
    fan_status   = request.form.get('fan_status')
    temprature   = request.form.get('temprature')

    query = (
        "INSERT INTO smart_home(id, light_status, fan_status, temprature) "
        f"VALUES({id}, '{light_status}', '{fan_status}', {temprature});"
    )
    executeQuery(query=query)
    return "reading is added successfully"



@server.get('/home')
def get_all_status():
    query = "SELECT * FROM smart_home;"
    data = executeSelectQuery(query=query)
    return f"all_readings:{data}"



@server.put('/home')
def update_status():
    id           = request.form.get('id')            
    light_status = request.form.get('light_status')
    fan_status   = request.form.get('fan_status')
    temprature   = request.form.get('temprature')

    query = (
        "UPDATE smart_home "
        f"SET light_status = '{light_status}', "
        f"fan_status = '{fan_status}', "
        f"temprature = {temprature} "
        f"WHERE id = {id};"
    )
    executeQuery(query=query)
    return "reading is updated successfully"



@server.delete('/home')
def delete_status():
    id = request.form.get('id')                    

    query = f"DELETE FROM smart_home WHERE id = {id};"
    executeQuery(query=query)
    return "reading is deleted successfully"


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
