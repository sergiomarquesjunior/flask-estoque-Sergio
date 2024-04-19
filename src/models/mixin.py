import uuid
from typing import Optional, Self

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime

from src.modulos import db


class TimeStampMixin:
    """
    Mixin para incluir data de cadastro e data de atualização
    """
    dta_cadastro: Mapped[DateTime] = mapped_column(DateTime,
                                                   server_default=sa.func.now(),
                                                   nullable=False)
    dta_atualizaca: Mapped[Optional[DateTime]] = mapped_column(DateTime,
                                                               onupdate=sa.func.now(),
                                                               default=sa.func.now(),
                                                               nullable=True)


class BasicRepositoryMixin:
    @classmethod
    def is_empty(cls) -> bool:
        return not (db.session.execute(sa.select(cls).limit(1)).scalar_one_or_none())

    @classmethod
    def get_by_id(cls, cls_id) -> Self | None:
        try:
            cls_id = uuid.UUID(str(cls_id))
        except ValueError:
            cls_id = cls_id
        return db.session.get(cls, cls_id)

    @classmethod
    def get_first_or_none_by(cls,
                             atributo: str,
                             valor: str | int | uuid.UUID,
                             casesensitive: bool = True) -> Self | None:
        registro = None
        if hasattr(cls, atributo):
            if casesensitive:
                registro = db.session.execute(
                    sa.select(cls).
                    where(getattr(cls, atributo) == valor).
                    limit(1)
                ).scalar_one_or_none()
            else:
                if isinstance(valor, str):
                    # noinspection PyTypeChecker
                    registro = db.session.execute(
                        sa.select(cls).
                        where(sa.func.lower(getattr(cls, atributo)) == sa.func.lower(valor)).
                        limit(1)
                    ).scalar_one_or_none()
                else:
                    raise TypeError("Para a operação case insensitive, o "
                                    f"atributo \"{atributo}\" deve ser da classe str")
        return registro


class DataMixin:
    pass