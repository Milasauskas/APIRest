from app import db
from app import manager


class Raca (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    raca = db.Column(db.String(80))
    descricao = db.Column(db.String(300))

    db.create_all()
    manager.crete_api(Raca, methods=['POST', 'GET', 'PUT', 'DELETE'])

    idTemp = db.Column(db.Integer, db.ForeingnKey (idTemp))
    raca = db.relationship ('Raca')