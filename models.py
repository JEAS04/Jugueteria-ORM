from sqlalchemy import Column, Integer, String, Float
from UUID import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Juguete(Base):
    __tablename__ = 'juguetes'

    id_juguete = Column(UUID, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False, index=true)
descripcion = Column(text,nullable=true)
    precio = Column(Float,nullable=False)
    stock = Column(Integer,default = 0, nullable=False)
activo = Column(boolean, default=true, nullable=false)
    tipo = Column(String, nullable=False)  # 'coleccionable', 'didactico', 'electronico'
id_usuario_creacion = column(integer, foreignkey('id_usuario', nullable=False)
id_usuario_edicion = column(integer, foreignkey('id_usuario', nullable=True)
fecha_creacion = column(integer, foreignkey('id_usuario', nullable=True, default=None))
fecha_actualizacion = column(DateTime, default=datetime.now, onupdate=datetime.now)                             

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
