from pydantic import BaseModel, Field, validator
from typing import Literal


class JugueteBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    tipo: Literal["coleccionable", "didactico", "electronico"]

    @validator("tipo")
    def validar_tipo(cls, v):
        if v not in ["coleccionable", "didactico", "electronico"]:
            raise ValueError("Tipo de juguete inválido")
        return v


class JugueteCreate(JugueteBase):
    pass


class JugueteOut(JugueteBase):
    id: int

    class Config:
        orm_mode = True
