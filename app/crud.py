from sqlalchemy.orm import Session
from .database import models
from sqlalchemy import or_, and_

models_dict = [models.Limits, models.Prohibitions]


def get_limits(item, db: Session):
    dic = []
    keys = []
    if '.' in item:
        for i in range(len(item), 0, -1):
            num = item[0: i]
            limits = db.query(models.Limits).order_by(models.Limits.numbers).filter(
                models.Limits.numbers == num).all()
            if limits:
                for el in limits:
                    res = {'name': '', "exceptions": []}
                    if el.name not in keys:
                        keys.append(el.name)
                        res['name'] = el.name
                        res['exceptions'].append(el.exceptions)
                        dic.append(res)
                    else:
                        for i in dic:
                            if i['name'] == el.name:
                                i['exceptions'].append(el.exceptions)
                                continue
    else:
        limits = db.query(models.Limits).order_by(models.Limits.numbers).filter(
            models.Limits.numbers == item).all()
        if limits:
            for el in limits:
                res = {'name': '', "exceptions": []}
                if el.name not in keys:
                    keys.append(el.name)
                    res['name'] = el.name
                    res['exceptions'].append(el.exceptions)
                    dic.append(res)
                else:
                    for i in dic:
                        if i['name'] == el.name:
                            i['exceptions'].append(el.exceptions)
                            continue
    return dic


def get_prohibitions(item, db: Session):
    dic = []
    keys = []
    if '.' in item:
        for i in range(len(item), 0, -1):
            num = item[0: i]
            prohbs = db.query(models.Prohibitions).order_by(models.Prohibitions.numbers).filter(
                models.Prohibitions.numbers == num).all()
            if prohbs:
                for el in prohbs:
                    res = {'name': '', "exceptions": []}
                    if el.name not in keys:
                        keys.append(el.name)
                        res['name'] = el.name
                        res['exceptions'].append(el.exceptions)
                        dic.append(res)
                    else:
                        for i in dic:
                            if i['name'] == el.name:
                                i['exceptions'].append(el.exceptions)
                                continue
    else:
        prohbs = db.query(models.Prohibitions).order_by(models.Prohibitions.numbers).filter(
            models.Prohibitions.numbers == item).all()
        if prohbs:
            for el in prohbs:
                res = {'name': '', "exceptions": []}
                if el.name not in keys:
                    keys.append(el.name)
                    res['name'] = el.name
                    res['exceptions'].append(el.exceptions)
                    dic.append(res)
                else:
                    for i in dic:
                        if i['name'] == el.name:
                            i['exceptions'].append(el.exceptions)
                            continue
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
