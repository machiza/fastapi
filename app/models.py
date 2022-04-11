from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from .database import Base

class Post(Base):
  __tablename__ = "posts"

  id = Column(Integer, primary_key=True, nullable=False)
  title = Column(String, nullable=False)
  content = Column(String, nullable=False)
  published = Column(Boolean, server_default='TRUE', default=True, nullable=False)
  created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))