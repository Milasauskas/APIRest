from app import db
from app import manager


class Temperamento (db.Model):
    idTemp = db.Column(db.Integer, primary_key = True)
    origem = db.Column(db.String(80))
    Temperamento = db.Column(db.String(300))

    db.create_all()
    manager.crete_api(temperamento, methods = ['POST', 'GET', 'PUT', 'DELETE'])