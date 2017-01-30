#!/usr/bin/python
# -*- coding: utf-8 -*-
# project/data.py

from app import db

from datetime import datetime
import csv

def createMessages():
    pass

def deleteData():
    pass
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()
