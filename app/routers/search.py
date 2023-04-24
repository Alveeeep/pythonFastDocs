from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.ext.declarative import declarative_base
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.database import crud
from app.database import models
from app.crud import get_all

from docx2python import docx2python

router = APIRouter()

get_db()

templates = Jinja2Templates(directory="templates")

eto_vremenno = {
    '(1)': 'За исключением входящих в указанные коды ОКПД2 товаров, работ, услуг, в случае осуществления закупок которых заказчик вправе проводить конкурс с ограниченным участием и двухэтапный конкурс в соответствии с частью 2 статьи 56 и пунктом 1 части 2 статьи 57 Федерального закона "О контрактной системе в сфере закупок товаров, работ, услуг для обеспечения государственных и муниципальных нужд".',
    '(2)': 'За исключением пищевых продуктов, закупаемых для дошкольных образовательных учреждений, общеобразовательных учреждений, образовательных учреждений начального профессионального, среднего профессионального и высшего профессионального образования, специальных (коррекционных) образовательных учреждений для обучающихся, воспитанников с ограниченными возможностями здоровья, учреждений для детей-сирот и детей, оставшихся без попечения родителей, специальных учебно-воспитательных учреждений закрытого типа для детей и подростков с девиантным (общественно опасным) поведением, нетиповых образовательных учреждений высшей категории для детей, подростков и молодых людей, проявивших выдающиеся способности, образовательных учреждений дополнительного образования детей и других организаций, осуществляющих образовательный процесс для детей, медицинских организаций, учреждений социального обслуживания, организаций отдыха детей и их оздоровления и (или) на оказание услуг общественного питания для указанных учреждений и организаций.',
    '(3)': 'За исключением детской одежды.',
    '(4)': 'За исключением работ по строительству, реконструкции, капитальному ремонту особо опасных, технически сложных объектов капитального строительства, а также искусственных дорожных сооружений, включенных в состав автомобильных дорог федерального, регионального или межмуниципального, местного значения, а также работ, включенных в эту группировку, в случае если начальная (максимальная) цена контракта при осуществлении закупок для обеспечения государственных нужд превышает 150 млн. рублей, для обеспечения муниципальных нужд превышает 50 млн. рублей.',
    '(5)': 'За исключением услуг по обеспечению питанием и обслуживанию ритуально-обрядовых мероприятий (свадеб, банкетов по случаю рождения ребенка, юбилея и др.).',
    '(6)': 'За исключением наборов сувенирных и подарочных (блокноты и записные книжки), бюллетеней для голосования на выборах и референдумах.',
    '(7)': 'За исключением услуг по обмену жилого недвижимого имущества.'}


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@router.get("/page/{page_name}", response_class=HTMLResponse)
def page(request: Request, page_name: str):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@router.get("/getsymb/{item}", response_class=HTMLResponse)
def get_users(request: Request, item: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=item)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/test/{item}")
def search_for_item(request: Request, item: str, db: Session = Depends(get_db)):
    return get_all(db, item)


# Нужно чтобы проверялось на 01 (самый родительский номер)


@router.post("/createit", tags=['НЕ ЗАПУСКАТЬ ЭТО ДЛЯ ОКПД БЫЛО'])
def create_okpd(request: Request, db: Session = Depends(get_db)):
    doc_result = docx2python('app/okpd.docx')
    for el in doc_result.body:
        for i in el:
            if i[0][0] != '' and 'Раздел ' not in i[0][0]:
                db_okpd = models.Okpd(number=i[0][0], description=i[1][0])
                db.add(db_okpd)
                db.commit()
                db.refresh(db_okpd)
    return 'надеюсь норм'


@router.post("/ogranicheniya", tags=['НЕ ЗАПУСКАТЬ ЭТО ДЛЯ ОКПД БЫЛО'])
def create_ogr(request: Request, db: Session = Depends(get_db)):
    doc_result = docx2python('app/ogranicheniya471.docx')
    for el in doc_result.body:
        for i in el:
            if '*' in i[0][0]:
                number = i[0][0].split('*')
                db_ogr = models.Limits(numbers=number[0],
                                       name='Распоряжение Правительства РФ от 21 марта 2016 г. № 471-р',
                                       exceptions=eto_vremenno[number[1]])
            else:
                db_ogr = models.Limits(numbers=i[0][0],
                                       name='Распоряжение Правительства РФ от 21 марта 2016 г. № 471-р',
                                       exceptions=None)
            db.add(db_ogr)
            db.commit()
            db.refresh(db_ogr)
    return 'надеюсь норм'


@router.post("/zapret", tags=['НЕ ЗАПУСКАТЬ ЭТО ДЛЯ ОКПД БЫЛО'])
def create_zapret(request: Request, db: Session = Depends(get_db)):
    codes = ["62", "58.29.11", "63.11", "61.10.3", "61.10.4", "61.20.3", "61.20.4", "61.90.10", "58.29.13", "58.29.12",
             "63.11.12", "63.11.19", "58.29.14", "58.29.21", "58.29.29", "58.29.21", "58.29.29", "69", "71.12",
             "70.22.2", "18", "70.22", "26.5"]
    for el in codes:
        db_ogr = models.Prohibitions(numbers=el,
                                     name="Постановление Правительства Российской Федерации от 16.11.2015 № 1236 «Об установлении запрета на допуск программного обеспечения, происходящего из иностранных государств, для целей осуществления закупок для обеспечения государственных и муниципальных нужд»",
                                     exceptions=None)
        db.add(db_ogr)
        db.commit()
        db.refresh(db_ogr)
    return 'надеюсь норм'
