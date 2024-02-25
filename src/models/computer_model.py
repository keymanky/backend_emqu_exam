from dataclasses import dataclass
from src import db

@dataclass
class Computer(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique=True)
    name = db.Column(db.String(60))
    ip = db.Column(db.String(70), unique = True)
