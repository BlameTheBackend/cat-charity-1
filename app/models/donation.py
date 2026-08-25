from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.mixins import InvestmentMixin
from app.core.db import Base


class Donation(InvestmentMixin, Base):
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
