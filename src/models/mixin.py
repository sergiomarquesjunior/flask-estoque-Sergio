from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime

class DataMixin:
    dta_cadastro: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    dta_atualizacao: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True, server_default=func.now(), onupdate=func.now())
