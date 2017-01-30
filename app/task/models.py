## -*- coding: utf-8 -*-

from app import db

class task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    desc = db.Column(db.String())

    tenant_id = db.Column(db.Integer)

    taskStatus_id = db.Column(db.Integer, db.ForeignKey('taskStatus.id'))
    deadline = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    read_at = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    conf_at = db.Column(db.Integer, db.ForeignKey('calendar.id'))
