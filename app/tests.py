from app import app, db

import os
import unittest
from flask import render_template
import datetime

from model import User, Table


class TestCase(unittest.TestCase):
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    def test_user(self):
        u = User(name='john',surname='Smith',tel=88005553456, table=1, time='19:08:2019 21:30' )
        user = User.query.filter_by(tel=u.tel).first()
        if user.tel ==u.tel:
            print("Пользователь уже создан")
        else:
            db.session.add(u)
            db.session.commit()

    def test_table(self):
        u = Table(id = 1,size =3, time1=datetime.datetime(2005, 7, 14, 12, 30) )
        db.session.add(u)
        db.session.commit()
    def test_registration(self):
        u = User(name='john', surname='Smith', tel=88005553456, table=1, time=datetime.datetime(2005, 7, 14, 12, 30))
        user = User.query.filter_by(table=u.table).first()
        if u.time ==user.time:
            print("Стол на это время уже задан")
        else:
            db.session.add(u)
            db.session.commit()

if __name__ == '__main__':
    unittest.main()