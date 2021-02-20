# Create your models here.
from sqlalchemy import (
    Column, DateTime,ForeignKey,
    Index, Integer, String, TIMESTAMP, text
)

from sqlalchemy.dialects.mysql import (
    DATETIME, VARCHAR, TEXT
)

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(VARCHAR(10), primary_key=True)
    real_name = Column(VARCHAR(50))
    time_zone =  Column(VARCHAR(30))
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    
class UserActivity(Base):
    __tablename__ = 'user_activity'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    start_time = Column(VARCHAR(30))
    end_time = Column(VARCHAR(30))

    user = relationship('User')

