from abc import ABC, abstractmethod

class EstrategiaAhorro(ABC):
    @abstractmethod
    def calcular_cuota(self, ingreso_mensual):
        pass
