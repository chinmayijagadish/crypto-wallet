from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Integer)
    timestamp = db.Column(db.Float)
    transactions = db.Column(db.Text)
    previous_hash = db.Column(db.String(64))
    hash = db.Column(db.String(64))

    def __init__(self, index, timestamp, transactions, previous_hash, hash_):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = hash_
