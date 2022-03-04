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
							"indigen":60.7,
							"rango":"25/02/2021 al 03/03/2021"}),
	"Gerencia3": GerInDB(**{"name":"Gerencia Cartera Operativa",
							"indigen":95.3,
							"rango":"04/02/2022 al XX/XX/2022"}),
	"Gerencia1": GerInDB(**{"name":"Gerencia de Operación Bancaria",
							"indigen":96.1,
							"rango":"25/02/2021 al 03/03/2021"}),
}

def get_gerencia(gerencia: str):
    if gerencia in database_gerencias.keys():
        return database_gerencias[gerencia]
    else:
        return None
