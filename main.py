from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Juguete, Coleccionable, Didactico, Electronico
from schemas import JugueteCreate

# Configuración de la base de datos SQLite (puedes cambiar esto por PostgreSQL u otra)
DATABASE_URL = "sqlite:///./juguetes.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas
Base.metadata.create_all(bind=engine)


def crear_juguetes_iniciales(db: Session):
    if db.query(Juguete).count() == 0:
        juguetes_iniciales = [
            Electronico(nombre="Robot", precio=100000, stock=5, tipo="electronico"),
            Didactico(nombre="Lego", precio=350000, stock=10, tipo="didactico"),
            Coleccionable(nombre="Funko", precio=60000, stock=3, tipo="coleccionable"),
            Electronico(nombre="Carro", precio=200000, stock=6, tipo="electronico"),
            Didactico(nombre="Rubik", precio=15000, stock=18, tipo="didactico"),
            Coleccionable(nombre="Goku", precio=97000, stock=2, tipo="coleccionable"),
        ]
        db.add_all(juguetes_iniciales)
        db.commit()


def obtener_juguete_por_nombre(db: Session, nombre: str):
    return db.query(Juguete).filter(Juguete.nombre.ilike(nombre)).first()


def mostrar_inventario(db: Session):
    juguetes = db.query(Juguete).all()
    if not juguetes:
        print("¡El inventario está vacío!")
    else:
        for j in juguetes:
            print(f"{j.nombre} - Precio: {j.precio:.2f} - Stock: {j.stock}")


def vender_juguete(db: Session, nombre: str, cantidad: int):
    juguete = obtener_juguete_por_nombre(db, nombre)
    if juguete:
        print(juguete.vender(cantidad))
        db.commit()
    else:
        print("Juguete no encontrado.")


def aplicar_descuento(db: Session, nombre: str, porcentaje: int):
    juguete = obtener_juguete_por_nombre(db, nombre)
    if juguete:
        # Identificar subtipo manualmente
        if juguete.tipo == "coleccionable":
            juguete_real = Coleccionable(**juguete.__dict__)
        elif juguete.tipo == "didactico":
            juguete_real = Didactico(**juguete.__dict__)
        elif juguete.tipo == "electronico":
            juguete_real = Electronico(**juguete.__dict__)
        else:
            juguete_real = juguete

        # Aplicar descuento en instancia real
        print(juguete_real.aplicar_descuento(porcentaje))

        # Actualizar el juguete original
        juguete.precio = juguete_real.precio
        db.commit()
    else:
        print("Juguete no encontrado.")


def menu():
    db = SessionLocal()
    crear_juguetes_iniciales(db)

    while True:
        print("\n--- Menú Juguetería ---")
        print("1. Mostrar inventario")
        print("2. Vender juguete")
        print("3. Aplicar descuento")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_inventario(db)

        elif opcion == "2":
            nombre = input("Nombre del juguete: ").strip()
            entrada = input("Cantidad: ")
            if not entrada.isdigit():
                print("Debe ingresar un número válido.")
                continue
            cantidad = int(entrada)
            vender_juguete(db, nombre, cantidad)

        elif opcion == "3":
            nombre = input("Nombre del juguete: ").strip()
            entrada = input("Porcentaje de descuento: ")
            if not entrada.isdigit():
                print("Debe ingresar un número válido.")
                continue
            porcentaje = int(entrada)
            aplicar_descuento(db, nombre, porcentaje)

        elif opcion == "4":
            print("¡Gracias por utilizar nuestra aplicación!")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
