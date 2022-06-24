from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class GerInDB(BaseModel):
    name: str
    indigen: float
    rango: str

database_gerencias = Dict[str, GerInDB]
database_gerencias = {
	"Gerencia3": GerInDB(**{"name":"Gerencia Servicio a Cliente",
							"indigen":70.1,
							"rango":"27/05/2022 al 02/06/2022"}),
	"Gerencia2": GerInDB(**{"name":"Gerencia Servicio a Cliente",
							"indigen":72.6,
							"rango":"17/06/2022 al 23/06/2022"}),
	"Gerencia1": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":98.0,
							"rango":"17/06/2022 al 23/06/2022"}),               
}

def get_gerencia(gerencia: str):
    if gerencia in database_gerencias.keys():
        return database_gerencias[gerencia]
    else:
        return None
