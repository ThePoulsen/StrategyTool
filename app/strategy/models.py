## -*- coding: utf-8 -*-

from app import db

class mission(db.Model):
    __tablename__ = 'mission'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    desc = db.Column(db.String())
    currentMission = db.Column(db.Boolean)

    start = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    end = db.Column(db.Integer, db.ForeignKey('calendar.id'))

class vision(db.Model):
    __tablename__ = 'vision'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    desc = db.Column(db.String())
    currentVision = db.Column(db.Boolean)

    start = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    end = db.Column(db.Integer, db.ForeignKey('calendar.id'))

class objective(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    desc = db.Column(db.String())

    start = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    end = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    tenant_id = db.Column(db.Integer)

class strategy(db.Model):
    __tablename__ = 'strategy'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    desc = db.Column(db.String())

    tenant_id = db.Column(db.Integer)

    start = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    end = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    strategyLevel_id = db.Column(db.Integer, db.ForeignKey('strategyLevel.id'))
    objective_id = db.Column(db.Integer, db.ForeignKey('objective.id'))
