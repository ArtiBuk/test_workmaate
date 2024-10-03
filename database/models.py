import sqlalchemy as sa
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}

metadata = sa.MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

NOW_AT_UTC = sa.text("timezone('utc', now())")


class TimestampMixin:
    """
    Миксин для добавления временных меток создания и обновления записи.

    Атрибуты:
    ----------
    :param created_at: время создания записи.
    :type datetime.datetime
    :param updated_at: время обновления записи.
    :type datetime.datetime
    """

    created_at = Column(
        sa.TIMESTAMP(timezone=False), server_default=NOW_AT_UTC, nullable=False
    )
    updated_at = Column(
        sa.TIMESTAMP(timezone=False),
        server_default=NOW_AT_UTC,
        nullable=False,
        onupdate=NOW_AT_UTC,
    )


class SoftDeleteMixin:
    """
    Миксин для добавления пометки об удалении записи.

    Атрибуты:
    ----------
    :param deleted_at: время удаления записи.
    :type datetime.datetime
    """

    deleted_at = Column(sa.TIMESTAMP(timezone=False), nullable=True, index=True)


class User(Base, TimestampMixin, SoftDeleteMixin):
    """
        Модель пользователя

        Таблица: user
    """
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    username: str = Column(String, nullable=False, unique=True)
    password_hash: str = Column(String, nullable=False)
    refresh_token: str = Column(String, nullable=False)


class Kitty(Base, TimestampMixin, SoftDeleteMixin):
    """
        Модель котят

        Таблица: kittens
    """
    __tablename__ = 'kittens'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    color: str = Column(String, nullable=False)
    age: int = Column(
        Integer,
        nullable=False,
        info={"description": "Возраст указывается в полных месяцах"}
    )
    description: str = Column(String, nullable=True)
    breed_id: int = Column(
        Integer,
        ForeignKey("breeds.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )

    breed = relationship("Breed", back_populates="kittens")


class Breed(Base):
    """
        Модель для хранения всех пород котят

        Таблица: breeds
    """
    __tablename__ = 'breeds'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    description: str = Column(String, nullable=True)

    kittens = relationship("Kitty", back_populates="breed")
