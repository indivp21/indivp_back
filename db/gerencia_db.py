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
							"indigen":71.7,
							"rango":"04/02/2022 al XX/XX/2022"}),
	"Gerencia3": GerInDB(**{"name":"Gerencia Cartera Operativa",
							"indigen":95.3,
							"rango":"04/02/2022 al XX/XX/2022"}),
	"Gerencia1": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":96.2,
							"rango":"04/02/2022 al XX/XX/2022"}),
}

def get_gerencia(gerencia: str):
    if gerencia in database_gerencias.keys():
        return database_gerencias[gerencia]
    else:
        return None
