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
							"indigen":76.1,
							"rango":"03/12/2021 al 09/12/2021"}),
	"Gerencia1": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":97.0,
							"rango":"10/12/2021 al 16/12/2021"}),
	"Gerencia3": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":96.5,
							"rango":"XX/XX/2021 al XX/XX/2021"}),
}

def get_gerencia(gerencia: str):
    if gerencia in database_gerencias.keys():
        return database_gerencias[gerencia]
    else:
        return None
