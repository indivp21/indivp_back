from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class GerInDB(BaseModel):
    name: str
    indigen: float
    rango: str

database_gerencias = Dict[str, GerInDB]
database_gerencias = {
	"Gerencia2": GerInDB(**{"name":"Gerencia Servivio a Cliente",
							"indigen":81.0,
							"rango":"18/11/2022 al 24/11/2022"}),
	"Gerencia1": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":97.4,
							"rango":"18/11/2022 al 24/11/2022"}),
}

def get_gerencia(gerencia: str):
    if gerencia in database_gerencias.keys():
        return database_gerencias[gerencia]
    else:
        return None
