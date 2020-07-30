#IMPORT LIBRARIES ##
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_jsonpify import jsonify
import pyodbc

#OPEN THE APP ##
app = Flask(__name__)
#CONECTION TO DATA BASE ##
server = 'tcp:energyms.database.windows.net' 
database = 'EMS' 
username = 'ems' 
password = 'Ezeq0211' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
#CALL THE VARIABLE API ##
api = Api(app)
#GET DATA FROM THE DATA BASE ##
class Shift(Resource):
        def get(self):
                query = cursor.execute("SELECT * FROM EMS.dbo.tbl_shifts;") 
                records = cursor.fetchall()
                print("Total rows are:  ", len(records))
                list_records = []
#VARIABLES TO USE ##
                for row in records:
                        lv_id_shift   = str(row[0])
                        lv_start_time = str(row[1])
                        lv_end_time   = str(row[2])
#JOIN VARIABLE ##
                        dataset_entry = {'id_shift': lv_id_shift, 'start_time': lv_start_time, 'end_time': lv_end_time}
#ADJUNTAR LISTA A LA LISTA X ##
                        list_records.append(dataset_entry)
#RETURN THE DATA IN THE WEB PAGE ##
                return list_records
#DATA ROUTE ##
api.add_resource(Shift, '/shifts')
#END OF THE APP ##
if __name__ == '__main__':
    app.run(port='5002')