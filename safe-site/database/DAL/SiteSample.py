from sqlalchemy import Column, Integer, String, Boolean, DATETIME
from database.DbUtils import Base
from datetime import datetime


class SiteSample(Base):
    __tablename__ = 'samples'

    id = Column(Integer, primary_key=True)
    site = Column(String)
    is_risk = Column(Boolean)
    timestamp = Column(DATETIME, default=datetime.now())
    categories = Column(String)
    votes = Column(String)
