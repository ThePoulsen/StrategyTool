## -*- coding: utf-8 -*-

from app import db

class project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    desc = db.Column(db.String())

    tenant_id = db.Column(db.Integer)

    start = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    end = db.Column(db.Integer, db.ForeignKey('calendar.id'))
