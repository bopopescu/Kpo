from app import db
from datetime import datetime
import re


ROLE_USER = 0
ROLE_ADMIN = 1



class User(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(80), index=True)
    surname = db.Column(db.String(80), index=True, unique=True)
    tel = db.Column(db.Integer, unique=True, primary_key=True)
    table = db.Column(db.Integer, index=True)
    time = db.Column(db.DATETIME, index=True)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)



    def __repr__(self):
        return '<User %r     %r>' % (self.name, self.surname)


class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer, index=True, unique=True)
    time1 = db.Column(db.DateTime, index=True, unique=True)
    time2 = db.Column(db.DateTime, index=True, unique=True)
    time3 = db.Column(db.DateTime, index=True, unique=True)



    def __repr__(self):
        return '<Table %r' % (self.id)

