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
    data = db.query(models.Limits).filter(models.Limits.numbers.endswith('\n')).all()
    for el in data:
        el.numbers = el.numbers[:-2]
        db.commit()
    # doc_result = docx2python('app/okpd.docx')
    # for el in doc_result.body:
    #    for i in el:
    #        if i[0][0] != '' and 'Раздел ' not in i[0][0]:
    #            db_okpd = models.Okpd(number=i[0][0], description=i[1][0])
    #            db.add(db_okpd)
    #            db.commit()
    #            db.refresh(db_okpd)
    return 'надеюсь норм'


@router.post("/ogranicheniya", tags=['НЕ ЗАПУСКАТЬ ЭТО ДЛЯ ОКПД БЫЛО'])
def create_ogr(request: Request, db: Session = Depends(get_db)):
    with open('app/2014.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for el in data:
            if el.count('.') >= 1:
                el = el.split('_')
                db_ogr = models.Limits(numbers=el[0].rstrip(),
                                       name='Постановление Правительства РФ от 3 декабря 2020 г. N 2014',
                                       exceptions=el[1].rstrip())
                db.add(db_ogr)
                db.commit()
                db.refresh(db_ogr)
    return 'надеюсь норм'


@router.post("/zapret", tags=['НЕ ЗАПУСКАТЬ ЭТО ДЛЯ ОКПД БЫЛО'])
def create_zapret(request: Request, db: Session = Depends(get_db)):
    codes = ["13.2", "13.9", "14.1", "14.20", "14.3", "15.1", "15.2", "16.21.13", "16.21.14", "17.12",
             "20.30", "20.52", "20.59.1", "22.11.1", "22.19.73", "22.29.29", "23.11", "23.2", "23.3",
             "23.6", "23.70", "23.91.11", "25.73.30", "25.73.40", "25.73.60", "26.51.44.000", "27.11.3", "27.90.31.110",
             "28.21.13.111", "28.22.14.125", "28.22.14.151", "28.22.14.159", "28.22.15.110", "28.22.15.120",
             "28.22.18.261", "28.22.18.269", "28.22.18.314",
             "28.22.18.390", "28.24.1", "28.24.2", "28.25.13.111", "28.25.13.112", "28.25.13.114", "28.29.50.000",
             "28.29.70", "28.30", "28.41.1", "28.41.2", "28.41.3", "28.41.4", "28.49.1", "28.49.2", "28.92.21",
             "28.92.22", "28.92.24", "28.92.25.000", "28.92.26", "28.92.27", "28.92.28.110", "28.92.28.120", "28.92.29",
             "28.92.30.110", "28.92.30.150", "28.92.30.160", "28.92.30.190", "28.92.40.130", "28.92.50.000",
             "28.93.15.110", "28.93.15.120", "28.93.17.110", "28.93.17.120", "28.99.39.190", "29.10.2", "29.10.3",
             "29.10.4", "29.10.51.000", "29.10.52", "29.10.59.110", "29.10.59.120", "29.10.59.130", " 29.10.59.140",
             "29.10.59.150", "29.10.59.160", "29.10.59.180", "29.10.59.220", "29.10.59.230", "29.10.59.240",
             "29.10.59.250", "29.10.59.270", "29.10.59.280", "29.10.59.310", "29.10.59.320", "29.10.59.390",
             "29.20.21.110", "29.20.21.120", "29.20.23.110", "29.20.23.120", "29.20.23.130", "29.20.23.190", "30.11.21",
             "30.11.22", "30.11.23",
             "30.11.24", "30.11.31", "30.11.32", "30.11.33", "30.11.40", "30.11.50", "30.20.1", "30.20.2", "30.20.3",
             "30.20.4", "30.30.31", "30.30.34", "30.92.10", "31.01.1", "31.02.10", "31.03.1", "31.09.11", "31.09.12",
             "31.09.13", "31.09.14.110", "32.99.11.130", "32.99.11.140", "32.99.11.190"]
    for el in codes:
        db_ogr = models.Prohibitions(numbers=el,
                                     name="Постановление Правительства РФ от 30 апреля 2020 г. N 616 Об установлении запрета на допуск промышленных товаров, происходящих из иностранных государств, для целей осуществления закупок для государственных и муниципальных нужд, а также промышленных товаров, происходящих из иностранных государств, работ (услуг), выполняемых (оказываемых) иностранными лицами, для целей осуществления закупок для нужд обороны страны и безопасности государства",
                                     exceptions=None)
        db.add(db_ogr)
        db.commit()
        db.refresh(db_ogr)
    return 'надеюсь норм'
