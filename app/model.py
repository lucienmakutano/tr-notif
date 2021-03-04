from datetime import datetime

from app.__main__ import db


class Teacher(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)


class User(db.Model):
    phone_number = db.Column(db.String(15), nullable=False)
