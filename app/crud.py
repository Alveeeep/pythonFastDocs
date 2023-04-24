from sqlalchemy.orm import Session
from .database import models
from sqlalchemy import or_, and_

models_dict = [models.Limits, models.Prohibitions]


def get_limits(item, db: Session):
    dic = {'name': [], "exceptions": []}
    if '.' in item:
        number = item.split('.')
        for i in range(len(number), 0, -1):
            num = '.'.join(number[0: i])
            limits = db.query(models.Limits).order_by(models.Limits.numbers).filter(
                models.Limits.numbers == num).all()
            if limits:
                for el in limits:
                    if dic['name'] != el.name:
                        dic['name'].append(el.name)
                    if dic['exceptions'] != el.exceptions:
                        dic['exceptions'].append(el.exceptions)
    else:
        limits = db.query(models.Limits).order_by(models.Limits.numbers).filter(
            models.Limits.numbers == item).all()
        if limits:
            for el in limits:
                if dic['name'] != el.name:
                    dic['name'].append(el.name)
                if dic['exceptions'] != el.exceptions:
                    dic['exceptions'].append(el.exceptions)
    return dic


def get_prohibitions(item, db: Session):
    dic = {'name': [], "exceptions": []}
    if '.' in item:
        number = item.split('.')
        for i in range(len(number), 0, -1):
            num = '.'.join(number[0: i])
            prohbs = db.query(models.Prohibitions).order_by(models.Prohibitions.numbers).filter(
                models.Prohibitions.numbers.startswith(num)).first()
            if prohbs:
               # for el in prohbs:
                    if prohbs.name not in dic['name']:
                        dic['name'].append(prohbs.name)
                    if prohbs.exceptions not in dic['exceptions']:
                        dic['exceptions'].append(prohbs.exceptions)
    else:
        prohbs = db.query(models.Prohibitions).order_by(models.Prohibitions.numbers).filter(
            models.Prohibitions.numbers == item).all()
        if prohbs:
            for el in prohbs:
                if el.name not in dic['name']:
                    dic['name'].append(el.name)
                if dic['exceptions'] != el.exceptions:
                    dic['exceptions'].append(el.exceptions)
    return dic


def get_all(db: Session, item: str):
    res = []
    okpd = db.query(models.Okpd).order_by(models.Okpd.number).filter(
        or_(models.Okpd.number.like(item + '%'), models.Okpd.description.like(item.capitalize() + '%'))).all()
    for ok in okpd:
        res.append(
            {'id': ok.id, 'number': ok.number, 'description': ok.description, 'limits': get_limits(ok.number, db),
             'prohibitions': get_prohibitions(ok.number, db)})
    return res
