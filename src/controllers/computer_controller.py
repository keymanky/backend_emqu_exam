from flask import request, Response, json, Blueprint
from src.models.computer_model import Computer
from src.models.ping_model import Ping
from src import bcrypt, db
from datetime import datetime
from flask import jsonify
import jwt
import os

# Convert sqlalchemy object to dict
def to_dict(self):
    keys = self.__mapper__.attrs.keys()
    attrs = vars(self)
    return { k : attrs[k]  for k in keys}

# user controller blueprint to be registered with api blueprint
computers = Blueprint("computers", __name__)

# route for create api/computers/create
@computers.route('/create', methods = ["POST"])
def handle_create():
    try: 
        # first validate required use parameters
        data = request.json
        if "name" in data and "ip" in data:
            # validate if the ip exist 
            computer = Computer.query.filter_by(ip = data["ip"]).first()
            # usecase if the ip doesn't exists
            if not computer:
                # creating the computer instance of Computer Model to be stored in DB
                computer_obj = Computer(
                    name = data["name"],
                    ip = data["ip"],
                )
                db.session.add(computer_obj)
                db.session.commit()

                return Response(
                response=json.dumps({
                                        'status': 'success',
                                        'message': 'Created Computer',
                                        'id': computer_obj.id
                                    }),
                status=201,
                mimetype='application/json'
            )
            else:
                # if ip already exists
                return Response(
                response=json.dumps({"status": 'failed', 'message': 'IP already exists, ip is unique'}),
                status=409,
                mimetype='application/json'
            )
        else:
            # if request parameters are not correct 
            return Response(
                response=json.dumps({"status": 'failed', 'message': 'Computer Parameters name, ip are required'}),
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

# route for get api/computers/get
@computers.route('/get', methods = ["GET"])
def handle_get():
    try: 
        # first check computer parameters
        data = request.args

        if "id" in data:
            # check db for id records
            computer = Computer.query.filter_by(id = data["id"]).first()

            if computer:
                msn = {'status' : 'success', 'values': 0}
                results = to_dict(computer)
                msn['values'] = results
                return Response(
                    response=json.dumps(msn),
                        status=200,
                        mimetype='application/json'
                )
                

            # if there is no computer record
            else:
                return Response(
                    response=json.dumps({"status": "failed", "message": "Computer Record doesn't exist, kindly register"}),
                    status=404,
                    mimetype='application/json'
                ) 
        else:
            # if request parameters are not correct 
            return Response(
                response=json.dumps({"status": "failed", "message": "id Parameters required"}),
                status=400,
                mimetype='application/json'
            )
        
    except Exception as e:
        return Response(
                response=json.dumps({'status': "failed", 
                                     "message": "Error Occured",
                                     "error": str(e)}),
                status=500,
                mimetype='application/json'
            )

# route for update api/computers/update
@computers.route('/update', methods = ["PUT"])
def handle_update():
    try: 
        # first validate required use parameters
        data = request.json
        if "name" and data and "ip" in data and "id" in data:

            # check db for id records
            exits = Computer.query.filter_by(id = data["id"]).first()

            if exits:

                computer = Computer.query.filter_by(id = data["id"]).update(values={'name': data["name"], 'ip': data["ip"]})
                db.session.commit()
                return Response(
                    response=json.dumps({"status": "success", "message": "Computer Updated "}),
                    status=200,
                    mimetype='application/json'
                )                 

            # if there is no computer record
            else:

                return Response(
                    response=json.dumps({"status": "failed", "message": "Computer Record doesn't exist, kindly register"}),
                    status=404,
                    mimetype='application/json'
                ) 
           
        else:
            # if request parameters are not correct 
            return Response(
                response=json.dumps({"status": "failed", "message": "Computer Parameters id, name, ip are required"}),
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

# route for delete api/computers/delete
@computers.route('/delete', methods = ["DELETE"])
def handle_delete():
    try: 
        # first validate required use parameters
        data = request.json
        if "id" in data:
            # validate if the id exits
            computer = Computer.query.filter_by(id = data["id"]).first()

            # usecase if the ip doesn't exists
            if computer:

                # validate if the id haves pings
                ping = Ping.query.filter_by(ip = computer.ip).first()
                print(ping)
                if ping:

                    return Response(
                    response=json.dumps({"status": "unsuccess","message": "The Computer have pings"}),
                    status=403,
                    mimetype='application/json'
                    )

                
                else:

                    Computer.query.filter_by(id = data["id"]).delete()
                    db.session.commit()
                    return Response(
                    response=json.dumps({"status": "success","message": "Deleted Computer"}),
                    status=202,
                    mimetype='application/json'
                    )
        

            else:
                # if not exits
                return Response(
                response=json.dumps({"status": "failed", "message": "id not exits"}),
                status=409,
                mimetype='application/json'
            )
        else:
            # if request parameters are not correct 
            return Response(
                response=json.dumps({"status": "failed", "message": "Computer Parameters id is required"}),
                status=400,
                mimetype='application/json'
            )
        
    except Exception as e:
        return Response(
                response=json.dumps({'status': "failed", 
                                     "message": "Error Occured",
                                     "error": str(e)}),
                status=500,
                mimetype='application/json'
            )

# route for get api/computers/getAll
@computers.route('/getAll', methods = ["GET"])
def handle_getAll():
    try: 
        # first check computer parameters
        if True:

            # check db all records
            computer = Computer.query.all()
            tmp ={}
            x=0
            if computer:
                
                for i in computer:
                    tmp["Computer: " + str(x)] = to_dict(i)
                    x+=1

                msn = {'status' : 'success', 'values': 0}
                msn['values'] = tmp
                return Response(
                    response=json.dumps(msn),
                        status=200,
                        mimetype='application/json'
                )

            # if there is no computer record
            else:
                return Response(
                    response=json.dumps({"status": "failed", "message": "Computer Record doesn't exist, kindly register"}),
                    status=404,
                    mimetype='application/json'
                ) 
        else:
            # if request parameters are not correct 
            return Response(
                response=json.dumps({"status": "failed", "message": "id Parameters required"}),
                status=400,
                mimetype='application/json'
            )
        
    except Exception as e:
        return Response(
                response=json.dumps({'status': "failed", 
                                     "message": "Error Occured",
                                     "error": str(e)}),
                status=500,
                mimetype='application/json'
            )
