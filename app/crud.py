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


def get_auctions(item, db: Session):
    dic = []
    keys = []
    if '.' in item:
        for i in range(len(item), 0, -1):
            num = item[0: i]
            limits = db.query(models.Auction).order_by(models.Auction.numbers).filter(
                models.Auction.numbers == num).all()
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
        limits = db.query(models.Auction).order_by(models.Auction.numbers).filter(
            models.Auction.numbers == item).all()
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


def get_admissions(item, db: Session):
    dic = []
    keys = []
    if '.' in item:
        for i in range(len(item), 0, -1):
            num = item[0: i]
            limits = db.query(models.Admission).order_by(models.Admission.numbers).filter(
                models.Admission.numbers == num).all()
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
        limits = db.query(models.Admission).order_by(models.Admission.numbers).filter(
            models.Admission.numbers == item).all()
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


def get_privileges(item, db: Session):
    dic = []
    keys = []
    if '.' in item:
        for i in range(len(item), 0, -1):
            num = item[0: i]
            limits = db.query(models.Privileges).order_by(models.Privileges.numbers).filter(
                models.Privileges.numbers == num).all()
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
        limits = db.query(models.Privileges).order_by(models.Privileges.numbers).filter(
            models.Privileges.numbers == item).all()
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


def get_uis(item, db: Session):
    dic = []
    keys = []
    if '.' in item:
        for i in range(len(item), 0, -1):
            num = item[0: i]
            limits = db.query(models.UIS).order_by(models.UIS.numbers).filter(
                models.UIS.numbers == num).all()
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
        limits = db.query(models.UIS).order_by(models.UIS.numbers).filter(
            models.UIS.numbers == item).all()
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


def get_share(item, db: Session):
    dic = []
    keys = []
    if '.' in item:
        for i in range(len(item), 0, -1):
            num = item[0: i]
            limits = db.query(models.Share).order_by(models.Share.numbers).filter(
                models.Share.numbers == num).all()
            if limits:
                for el in limits:
                    res = {'name': '', "exceptions": []}
                    if el.name not in keys:
                        keys.append(el.name)
                        res['name'] = el.name
                        res['exceptions'].append(eval(el.exceptions))
                        dic.append(res)
                    else:
                        for i in dic:
                            if i['name'] == el.name:
                                i['exceptions'].append(eval(el.exceptions))
                                continue
    else:
        limits = db.query(models.Share).order_by(models.Share.numbers).filter(
            models.Share.numbers == item).all()
        if limits:
            for el in limits:
                res = {'name': '', "exceptions": []}
                if el.name not in keys:
                    keys.append(el.name)
                    res['name'] = el.name
                    res['exceptions'].append(eval(el.exceptions))
                    dic.append(res)
                else:
                    for i in dic:
                        if i['name'] == el.name:
                            i['exceptions'].append(eval(el.exceptions))
                            continue
    return dic


def get_all(db: Session, item: str):
    res = []
    okpd = db.query(models.Okpd).order_by(models.Okpd.number).filter(
        or_(models.Okpd.number.like(item + '%'), models.Okpd.description.like(item.capitalize() + '%'))).all()
    for ok in okpd:
        res.append(
            {'id': ok.id, 'number': ok.number, 'description': ok.description, 'limits': get_limits(ok.number, db),
             'prohibitions': get_prohibitions(ok.number, db), 'auction': get_auctions(ok.number, db),
             'admission': get_admissions(ok.number, db),
             'privileges': get_privileges(ok.number, db), 'uis': get_uis(ok.number, db),
             'share': get_share(ok.number, db)})
    return res






"""

Версия от CHATGPT

from sqlalchemy.orm import Session
from .database import models
from collections import defaultdict

def get_data(item, db, Model):
    result = defaultdict(lambda: {'name': '', 'exceptions': []})
    
    if '.' in item:
        for i in range(len(item), 0, -1):
            num = item[:i]
            items = db.query(Model).order_by(Model.numbers).filter(Model.numbers == num).all()
            if items:
                for el in items:
                    if not result[el.name]['name']:
                        result[el.name]['name'] = el.name
                    result[el.name]['exceptions'].append(el.exceptions)
    else:
        items = db.query(Model).order_by(Model.numbers).filter(Model.numbers == item).all()
        if items:
            for el in items:
                if not result[el.name]['name']:
                    result[el.name]['name'] = el.name
                result[el.name]['exceptions'].append(el.exceptions)
    
    return [res for res in result.values() if res['name']]

def get_all(db: Session, item: str):
    res = []
    okpd = db.query(models.Okpd).order_by(models.Okpd.number).filter(
        or_(models.Okpd.number.like(item + '%'), models.Okpd.description.like(item.capitalize() + '%'))).all()

    for ok in okpd:
        data = {
            'id': ok.id,
            'number': ok.number,
            'description': ok.description,
            'limits': get_data(ok.number, db, models.Limits),
            'prohibitions': get_data(ok.number, db, models.Prohibitions),
            'auction': get_data(ok.number, db, models.Auction),
            'admission': get_data(ok.number, db, models.Admission),
            'privileges': get_data(ok.number, db, models.Privileges),
            'uis': get_data(ok.number, db, models.UIS),
            'share': get_data(ok.number, db, models.Share),
        }
        res.append(data)
    
    return res

"""


