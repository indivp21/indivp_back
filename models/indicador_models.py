from pydantic import BaseModel

class IndicadorIn(BaseModel):
    id_indicador: int = 0
    name: str
    porcentaje: float
    gerencia: str
    central: str
    colorin: str
    formula: str
    calculo: str
    comentario: str
    ponderado: float
    lgreen: float
    lyellow: str
    lred: float

class IndicadorOut(BaseModel):
    id_indicador: int = 0
    name: str
    porcentaje: float
    gerencia: str
    central: str
    colorin: str
    formula: str
    calculo: str
    comentario: str
    ponderado: float
    lgreen: float
    lyellow: str
    lred: float
