from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

info = dotenv_values("app/.env")
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://{0}:{1}@{2}:5445/{3}".format(info['LOGIN'], info['PASSWORD'],
                                                                              info['HOST'], info['NAME'])
#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{0}:{1}@{2}:3306/{3}".format(info['MYSQL_LOGIN'], info['MYSQL_PASSWORD'],
#                                                                              info['MYSQL_HOST'], info['MYSQL_NAME'])
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, future=True
)

Base = declarative_base()

SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
