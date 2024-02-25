from flask import request, Response, json, Blueprint
from src.models.ping_model import Ping
from src.models.computer_model import Computer
from src import utils
from src import bcrypt, db
from datetime import datetime
from sqlalchemy.sql import text
import jwt
import os

# user controller blueprint to be registered with api blueprint
pings = Blueprint("pings", __name__)

# route for create api/pings/callPingTest
@pings.route('/callPingTest', methods = ["POST"])
def handle_callPingTest():
    try: 
        # first validate required use parameters
        data = request.json
        if "ip" in data :
            # validate if the ip exist 
            computer = Computer.query.filter_by(ip = data["ip"]).first()
            # usecase if the ip doesn't exists
            if computer:

                resultPing = utils.pingE(data["ip"])
                comentarioPing = "Prueba de Conexion Exitosa" if resultPing else "No hay conexion"
                created_at = datetime.now()
                #print("Resultado del ping ::: " +str(created_at) + ":::")

                # creating the ip instance of User Model to be stored in DB
                ping_obj = Ping(
                    ip = data["ip"],
                    result = resultPing,
                    comment = comentarioPing,
                    moment = created_at
                )
                db.session.add(ping_obj)
                db.session.commit()

                return Response(
                response=json.dumps({"status": resultPing,
                                    "message": comentarioPing,
                                    "ip": ping_obj.ip}),
                status=201,
                mimetype='application/json'
            )
            else:
                # ip not exits
                return Response(
                response=json.dumps({"status": "failed", "message": "IP not exists in database please register it"}),
                status=409,
                mimetype='application/json'
            )
        else:
            # if request parameters are not correct 
            return Response(
                response=json.dumps({"status": "failed", "message": "ip Parameters is required"}),
                status=400,
                mimetype='application/json'
            )
        
    except Exception as e:
        return Response(
                response=json.dumps({"status": "failed", 
                                     "message": "Error Occured",
                                     "error": str(e)}),
                status=500,
                mimetype='application/json'
            )

# route for get api/pings/statistics
@pings.route('/statistics', methods = ["POST"])
def handle_statistics():
    try: 
        # first check ip parameters
        data = request.json
        if "ip" in data:
            # check db for ip records
            ping = Ping.query.filter_by(ip = data["ip"]).first()

            # if ip exits
            if ping:

                count_sucess = db.session.execute(text("SELECT count(*) FROM ping where ip='%s' and result='%s'" % (str(data["ip"]), '1'  ) ) )
                int_count_sucess = count_sucess.scalar()

                count_unsucess = db.session.execute(text("SELECT count(*) FROM ping where ip='%s' and result='%s'" % (str(data["ip"]), '0'  ) ) )
                int_count_unsucess = count_unsucess.scalar()

                int_total = int_count_sucess + int_count_unsucess
                effectiveness = round( (int_count_sucess / int_total) * 100 , 2)

                statistics = {
                        'ip' : data['ip'],
                        'bad_response': int_count_unsucess,
                        'ok_response': int_count_sucess,
                        'effectiveness_percent': effectiveness,
                        'total_response': int_total,                       
                }

                msn = {'status' : 'success', 'statistics': 0}
                msn['statistics'] = statistics

                return Response(
                        response=json.dumps(msn),
                        status=200,
                        mimetype='application/json'
                    )
            # if there is no IP record
            else:
                return Response(
                    response=json.dumps({"status": "failed", "message": "Empty test, no statistics"}),
                    status=404,
                    mimetype='application/json'
                ) 
        else:
            # if request parameters are not correct 
            return Response(
                response=json.dumps({"status": "failed", "message": "ip Parameters is required"}),
                status=400,
                mimetype='application/json'
            )
        
    except Exception as e:
        return Response(
                response=json.dumps({"status": "failed", 
                                     "message": "Error Occured",
                                     "error": str(e)}),
                status=500,
                mimetype='application/json'
            )
