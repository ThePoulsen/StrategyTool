## -*- coding: utf-8 -*-
import csv
from app import db
from app.masterData.models import weekDay, month, quarter, calendar, region, subRegion, country

weekDays = [('Monday','Mon','1'),
        ('Tuesday','Tue','2'),
        ('Wednesday','Wed','3'),
        ('Thursday','Thu','4'),
        ('Friday','Fri','5'),
        ('Saturday','Sat','6'),
        ('SunDay','Sun','7')]

months = [('January','Jan','1'),
          ('February','Feb','2'),
          ('March','Mar','3'),
          ('April','Apr','4'),
          ('May','May','5'),
          ('June','Jun','6'),
          ('July','Jul','7'),
          ('August','Aug','8'),
          ('September','Sep','9'),
          ('October','Oct','10'),
          ('November','Nov','11'),
          ('December','Dec','12')]

quarters = [('Q1','1'),
            ('Q2','2'),
            ('Q3','3'),
            ('Q4','4')]

calData = csv.reader(open('calendar.csv','r'), delimiter=';')
next(calData, None)

world = csv.reader(open('world.csv','r'))
next(world, None)

def createMasterData():
    for day, abbr, no in weekDays:
        if not weekDay.query.filter_by(no=no,title=day,abbr=abbr).first():
            db.session.add(weekDay(no=no,title=day,abbr=abbr))

    for mo, abbr, no in months:
        if not month.query.filter_by(no=no,title=mo,abbr=abbr).first():
            db.session.add(month(no=no,title=mo,abbr=abbr))

    for qty, no in quarters:
        if not quarter.query.filter_by(no=no,title=qty).first():
            db.session.add(quarter(no=no,title=qty))

    for calDate, day, week, mo, qty, year in calData:

        weekDay_id = weekDay.query.filter_by(no=day).first().id
        month_id = month.query.filter_by(no=mo).first().id
        quarter_id = quarter.query.filter_by(no=qty).first().id

        if not calendar.query.filter_by(date=calDate,
                                        weekDay_id=weekDay_id,
                                        weekNumber=week,
                                        month_id=month_id,
                                        quarter_id=quarter_id,
                                        year=year).first():

            calEntry = calendar(date=calDate,
                                weekDay_id=weekDay_id,
                                weekNumber=week,
                                month_id=month_id,
                                quarter_id=quarter_id,
                                year=year)
            db.session.add(calEntry)

    for r in world:
        if r[5]:
            if not region.query.filter_by(name=r[5]).first():
                db.session.add(region(name=r[5],code=r[7]))
        if r[6]:
            if not subRegion.query.filter_by(name=r[6]).first():
                reg = region.query.filter_by(code=r[7]).first()
                db.session.add(subRegion(name=r[6],code=r[8], region_id=reg.id))
        if r[0]:
            if not country.query.filter_by(name=r[0]).first():
                if r[6]:
                    subReg = subRegion.query.filter_by(code=r[8]).first()
                    db.session.add(country(name=r[0],
                                       alpha2=r[1],
                                       alpha3=r[2],
                                       code=r[3],
                                       subRegion_id=subReg.id))
                else:
                    db.session.add(country(name=r[0],
                                       alpha2=r[1],
                                       alpha3=r[2],
                                       code=r[3]))


    db.session.commit()