from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.ext.declarative import declarative_base
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.database import crud
from app.database import models

from docx2python import docx2python

router = APIRouter()

get_db()

templates = Jinja2Templates(directory="templates")


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
    return db.query(models.Okpd).filter(models.Okpd.number.find(item) or models.Okpd.description.find(item)).all()


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
