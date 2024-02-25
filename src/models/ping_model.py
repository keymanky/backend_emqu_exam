
from src import db

class Ping(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique=True)
    ip = db.Column(db.String(70))
    result = db.Column(db.String(60))
    comment = db.Column(db.String(360))
    moment = db.Column(db.DateTime())
