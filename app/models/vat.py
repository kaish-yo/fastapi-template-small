# Models(classes) used as schemas for tables in the database
from sqlalchemy.schema import Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer, String

from app.models._base import Base, ModelBaseMixin

# table names
VAT_TABLE = 'vat_master' # almost static

class Vat(Base, ModelBaseMixin):
    __tablename__ = VAT_TABLE
    vat_id: Mapped[int]       = mapped_column(Integer, primary_key=True)
    vat_category: Mapped[str] = mapped_column(String(50))
    
    def to_dict(self):
        return {
            'vat_id': self.vat_id,
            'vat_category': self.vat_category
        }