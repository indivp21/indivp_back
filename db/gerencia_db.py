from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class GerInDB(BaseModel):
    name: str
    indigen: float
    rango: str

database_gerencias = Dict[str, GerInDB]
database_gerencias = {
	"Gerencia3": GerInDB(**{"name":"Gerencia Cartera Operativa",
							"indigen":93.8,
							"rango":"29/05/2022 al 05/05/2022"}),
	"Gerencia2": GerInDB(**{"name":"Gerencia Servivio a Cliente",
							"indigen":72.0,
							"rango":"XX/XX/2021 al XX/XX/2021"}),
	"Gerencia1": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":97.3,
							"rango":"XX/XX/2021 al XX/XX/2021"}),
}

def get_gerencia(gerencia: str):
    if gerencia in database_gerencias.keys():
        return database_gerencias[gerencia]
    else:
        return None
