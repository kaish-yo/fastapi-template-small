# Models(classes) used as schemas for tables in the database
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import BigInteger, DateTime, Float, Integer, String

from app.models._base import Base, ModelBaseMixin

# table names
GL_TABLE = 'general_ledger'

class GeneralLedger(Base, ModelBaseMixin):
    __tablename__ = GL_TABLE
    record_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    journal_id: Mapped[str] = mapped_column(String(50), nullable=False)
    account_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    account_name: Mapped[str] = mapped_column(String(50), nullable=True)
    subaccount_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    vat_id: Mapped[int] = mapped_column(Integer, nullable=False)
    debter_creditor: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[float] = mapped_column(Float(), nullable=False)
    creator_id: Mapped[int] = mapped_column(Integer(), nullable=False)
    approver_id: Mapped[int] = mapped_column(Integer(), nullable=False)
    approved_at: Mapped[datetime] = mapped_column(DateTime(), nullable=True) # approve later
    
    def to_dict(self):
        return {
            'record_id': self.record_id,
            'journal_id': self.journal_id,
            'account_id': self.account_id,
            'account_name': self.account_name,
            'subaccount_id': self.subaccount_id,
            'vat_id': self.vat_id,
            'debter_creditor': self.debter_creditor,
            'amount': self.amount,
            'creator_id': self.creator_id,
            'approver_id': self.approver_id,
            'created_at': self.created_at,
            'approved_at': self.approved_at
        }