from abc import ABC, abstractmethod
from sqlalchemy import create_engine, text
from sqlalchemy import create_engine, ForeignKey, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

