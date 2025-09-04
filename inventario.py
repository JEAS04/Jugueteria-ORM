from sqlalchemy.orm import Session
from models import Juguete
from schemas import JugueteCreate

def agregar_juguete(db: Session, juguete_data: JugueteCreate):
    juguete = Juguete(**juguete_data.dict())
    db.add(juguete)
    db.commit()
    db.refresh(juguete)
    return juguete

def mostrar_inventario(db: Session) -> str:
    juguetes = db.query(Juguete).all()
    if not juguetes:
        return "¡El inventario está vacío!"
    return "\n".join([f"{j.nombre} - Precio: {j.precio} - Stock: {j.stock}" for j in juguetes])
