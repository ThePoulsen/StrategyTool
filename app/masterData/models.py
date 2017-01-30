## -*- coding: utf-8 -*-

from app import db

class quarter(db.Model):
    __tablename__ = 'quarter'

    id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.Integer)
    title = db.Column(db.String(), unique=True)

class month(db.Model):
    __tablename__ = 'month'

    id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.Integer)
    title = db.Column(db.String(), unique=True)
    abbr = db.Column(db.String(), unique=True)

class weekDay(db.Model):
    __tablename__ = 'weekDay'

    id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.Integer)
    title = db.Column(db.String(), unique=True)
    abbr = db.Column(db.String(), unique=True)

class calendar(db.Model):
    __tablename__ = 'calendar'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    weekNumber = db.Column(db.Integer)
    year = db.Column(db.Integer)

    weekDay_id = db.Column(db.Integer, db.ForeignKey('weekDay.id'))
    month_id = db.Column(db.Integer, db.ForeignKey('month.id'))
    quarter_id = db.Column(db.Integer, db.ForeignKey('quarter.id'))

class country(db.Model):
    __tablename__ = 'country'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    alpha2 = db.Column(db.String(128))
    alpha3 = db.Column(db.String(128))
    code = db.Column(db.Integer())

    subRegion_id = db.Column(db.Integer, db.ForeignKey('subRegion.id'))

class region(db.Model):
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    code = db.Column(db.Integer())

class subRegion(db.Model):
    __tablename__ = 'subRegion'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    code = db.Column(db.Integer())

    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
