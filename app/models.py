from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# Need User Admin for Company and need basic user as well 


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), index=True, unique=True)
    company_vision = db.Column(db.String(255))
    date_founded = db.Column(db.DateTime)
    needs = db.relationship('Need', backref='company', lazy='dynamic')

    def __str__(self):
        return self.company_name
    def date(self):
        return self.date_founded

class Need(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplies_needed = db.Column(db.String(255))
    volunteers_needed = db.Column(db.String(255))
    money_needed = db.Column(db.Integer)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))


    
