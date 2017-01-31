## -*- coding: utf-8 -*-

from app import db

class indicator(db.Model):
    __tablename__ = 'indicator'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)

    tenant_id = db.Column(db.Integer)

    UOM_id = db.Column(db.Integer, db.ForeignKey('UOM.id'))
    measurementFrequency_id = db.Column(db.Integer, db.ForeignKey('measurementFrequency.id'))
    indicatorType_id = db.Column(db.Integer, db.ForeignKey('indicatorType.id'))

    # Safety, Quality, Delivery, Cost, Productivity
    processType_id = db.Column(db.Integer, db.ForeignKey('processType.id'))
