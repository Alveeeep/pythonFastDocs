from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TEXT

from .database import Base


class Okpd(Base):
    __tablename__ = "OKPD2"

    id = Column(Integer, primary_key=True)
    number = Column(TEXT)
    description = Column(TEXT)


class Auction(Base):
    __tablename__ = "Auction lists"
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    numbers = Column(TEXT)
    exceptions = Column(TEXT)


class Limits(Base):
    __tablename__ = "Limits"
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    numbers = Column(TEXT)
    exceptions = Column(TEXT)


class Prohibitions(Base):
    __tablename__ = "Prohibitions"
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    numbers = Column(TEXT)
    exceptions = Column(TEXT)


class Admission(Base):
    __tablename__ = "Admission conditions"
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    numbers = Column(TEXT)
    exceptions = Column(TEXT)


class Privileges(Base):
    __tablename__ = "Privileges"
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    numbers = Column(TEXT)
    exceptions = Column(TEXT)


class UIS(Base):
    __tablename__ = "UIS"
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    numbers = Column(TEXT)
    exceptions = Column(TEXT)


class Share(Base):
    __tablename__ = "Minimal share"
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    numbers = Column(TEXT)
    exceptions = Column(TEXT)



