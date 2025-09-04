from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Juguete(Base):
    __tablename__ = "juguetes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)  # 'coleccionable', 'didactico', 'electronico'

    def vender(self, cantidad: int) -> str:
        if cantidad > 0 and cantidad <= self.stock:
            self.stock -= cantidad
            return f"Se vendieron {cantidad} {self.nombre}(s)."
        return "No hay elementos en el stock."

    def aplicar_descuento(self, porcentaje: int) -> str:
        if 0 < porcentaje < 100:
            self.precio -= self.precio * (porcentaje / 100)
            return f"Se aplicó el descuento. El precio nuevo es: {self.precio:.2f}"
        return "Porcentaje inválido."


class Coleccionable(Juguete):
    def aplicar_descuento(self, porcentaje: int) -> str:
        if porcentaje > 4:
            porcentaje = 4
            print("Error. El porcentaje máximo de descuento para los juguetes coleccionables es del 4%.")
        return super().aplicar_descuento(porcentaje)


class Didactico(Juguete):
    def aplicar_descuento(self, porcentaje: int) -> str:
        if porcentaje > 15:
            porcentaje = 15
            print("Error. El porcentaje máximo de descuento para los juguetes didácticos es del 15%.")
        return super().aplicar_descuento(porcentaje)


class Electronico(Juguete):
    def aplicar_descuento(self, porcentaje: int) -> str:
        if porcentaje > 20:
            porcentaje = 20
            print("Error. El porcentaje máximo de descuento para los juguetes electrónicos es del 20%.")
        return super().aplicar_descuento(porcentaje)
