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
    strategy_id = db.Column(db.Integer, db.ForeignKey('strategy.id'))

class projectAction(db.Model):
    __tablename__ = 'projectAction'
    __table_args__ = (db.UniqueConstraint('project_id', 'title', name='_project_title'),)

    id = db.Column(db.Integer, primary_key=True)

    # index indicates position on lists
    index = db.Column(db.Integer)
    title = db.Column(db.String())
    desc = db.Column(db.String())

    tenant_id = db.Column(db.Integer)

    # Impact of action on overall project
    impact = db.Column(db.Float())

    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    actionStatus_id = db.Column(db.Integer, db.ForeignKey('actionStatus.id'))

class actionDeliverable(db.Model):
    __tablename__ = 'actionDeliverable'
    __table_args__ = (db.UniqueConstraint('projectAction_id', 'title', name='_projectAction_title'),)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())

    tenant_id = db.Column(db.Integer)

    projectAction_id = db.Column(db.Integer, db.ForeignKey('projectAction.id'))
    actionStatus_id = db.Column(db.Integer, db.ForeignKey('actionStatus.id'))
