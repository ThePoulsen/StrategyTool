## -*- coding: utf-8 -*-

from app import db

class organization(db.Model):
    __tablename__ = 'organization'

    id = db.Column(db.Integer, primary_key=True)
    departmentTitle = db.Column(db.String(), unique=True)
    head = db.Column(db.Integer)

    tenant_id = db.Column(db.Integer)
    parent = db.Column(db.Integer, db.ForeignKey('organization.id'))
