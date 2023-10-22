# Models(classes) used as schemas for tables in the database
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import BigInteger, String

from app.models._base import Base, ModelBaseMixin

# table names
ACC_TABLE = 'account_master'

class Account(ModelBaseMixin, Base):
    __tablename__ = ACC_TABLE
    account_id: Mapped[str] = mapped_column(BigInteger, primary_key=True)
    account_name: Mapped[str] = mapped_column(String(50), nullable=False)    
    
    def to_dict(self):
        return {
            'account_id': self.account_id,
            'account_name': self.account_name
        }