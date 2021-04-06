# coding: utf-8
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from assets.database import Base
from datetime import datetime as dt

#Table情報
class Data(Base):
    #TableNameの設定
    __tablename__ = "data"

    #Column情報を設定する
    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=False)
    country = Column(String, unique=False)
    python = Column(Integer, unique=False)
    javascript = Column(Integer, unique=False)
    php = Column(Integer, unique=False)
    ruby = Column(Integer, unique=False)
    c = Column(Integer, unique=False)
    java = Column(Integer, unique=False)
    timestamp = Column(DateTime, default=dt.now())

    def __init__(self, date=None, country=None, python=None, javascript=None, php=None, ruby=None, c=None, java=None, timestamp=None):
        self.date = date
        self.country = country
        self.python = python
        self.javascript = javascript
        self.php = php
        self.ruby = ruby
        self.c = c
        self.java = java
        self.timestamp = timestamp
