## -*- coding: utf-8 -*-

from app import db

class mission(db.Model):
    __tablename__ = 'mission'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    desc = db.Column(db.String())

class vision(db.Model):
    __tablename__ = 'vision'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    desc = db.Column(db.String())

class strategy(db.Model):
    __tablename__ = 'strategy'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    desc = db.Column(db.String())
    year = db.Column(db.Integer)
    responsible = db.Column(db.Integer)
    tenant_id = db.Column(db.Integer)
    owner = db.Column(db.Integer)


    implemented_by = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    parent = db.Column(db.Integer, db.ForeignKey('strategy.id'))
    strategyLevel_id = db.Column(db.Integer, db.ForeignKey('strategyLevel.id'))
