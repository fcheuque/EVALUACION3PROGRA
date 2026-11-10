from abc import ABC, abstractmethod
from sqlalchemy import create_engine, text
from sqlalchemy import create_engine, ForeignKey, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

class Vehiculo(ABC):
    def __init__(self,patente,registroE,registroS):
        self.__patente = patente
        self.__registroE = registroE
        self.__registroS = registroS
    @abstractmethod
    def consultarVehiculo(self):
        return self.__patente
    def validarEstadia(self):
        if self.__registroS == self.__registroE:
            raise ValueError("Error, no es posible un  vehiculo con estado de salida y entrada iguales")
    def registrarIngreso(self):
        self.validarEstadia()
        return self.__registroE
    def registrarSalida(self):
        return self.__registroS
