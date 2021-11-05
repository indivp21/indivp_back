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
							"indigen":93.6,
							"rango":"XX/XX/2021 al XX/XX/2021"}),
	"Gerencia1": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":95.8,
							"rango":"XX/XX/2021 al XX/XX/2021"}),
	"Gerencia2": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":95.8,
							"rango":"XX/XX/2021 al XX/XX/2021"}),
}

def get_gerencia(gerencia: str):
    if gerencia in database_gerencias.keys():
        return database_gerencias[gerencia]
    else:
        return None
