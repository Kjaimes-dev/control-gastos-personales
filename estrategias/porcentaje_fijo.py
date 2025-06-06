from estrategias.estrategia_base import EstrategiaAhorro

class PorcentajeFijoStrategy(EstrategiaAhorro):
    def calcular_cuota(self, ingreso_mensual):
        return ingreso_mensual * 0.30
