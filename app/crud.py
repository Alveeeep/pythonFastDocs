from sqlalchemy.orm import Session
from .database import models
from collections import defaultdict
from sqlalchemy import or_, and_

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
