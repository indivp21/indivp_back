from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class GerInDB(BaseModel):
    name: str
    indigen: float
    rango: str

database_gerencias = Dict[str, GerInDB]
database_gerencias = {
	"Gerencia2": GerInDB(**{"name":"Gerencia Servicio a Cliente",
							"indigen":79.1,
							"rango":"02/09/2022 al 08/09/2022"}),
	"Gerencia1": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":97.4,
							"rango":"02/09/2022 al 08/09/2022"}),
	"Gerencia3": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":97.5,
							"rango":"26/08/2022 al 01/09/2022"}),      
}

def get_gerencia(gerencia: str):
    if gerencia in database_gerencias.keys():
        return database_gerencias[gerencia]
    else:
        return None
