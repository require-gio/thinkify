from sqlalchemy import Column, Integer, String, DateTime
from openapi_server import database


class Note(database.db.Model):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    name = Column(String)
    raw_text = Column(String)
    ai_output = Column(String)
