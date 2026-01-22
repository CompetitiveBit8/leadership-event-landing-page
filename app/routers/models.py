from sqlalchemy import Column, String, Integer
from routers.database import Base

class feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True) 
    name = Column(String, index=True)
    subject = Column(String, index=True)
    message = Column(String, index=True)