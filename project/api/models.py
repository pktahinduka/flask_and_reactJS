# project/api/models.py

import datetime

from project import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(80), nullable = False)
    is_active = db.Column(db.Boolean(), default = False, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.datetime.utcnow(), nullable = False)

def __init__(self, username, email):
    self.username = username
    self.email = email
    self.created_at = datetime.datetime.now()
    
def save(self):
    db.session.add(self)
    db.session.commit()
