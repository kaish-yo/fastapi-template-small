# Models(classes) used as schemas for tables in the database
from datetime import date
from sqlalchemy.types import BigInteger, Date, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models._base import Base, ModelBaseMixin

# table names
USER_TABLE = 'users'

class User(Base, ModelBaseMixin):
    __tablename__ = USER_TABLE
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_name: Mapped[str] = mapped_column(String(50), nullable=False)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    last_title: Mapped[str] = mapped_column(String(50), nullable=True)
    join_date: Mapped[date] = mapped_column(Date, nullable=False)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'title': self.title,
            'last_title': self.last_title,
            'join_date': self.join_date
        }