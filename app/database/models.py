from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text

from .database import Base


class Okpd(Base):
    __tablename__ = "OKPD2"

    id = Column(Integer, primary_key=True)
    number = Column(String)
    description = Column(Text)
