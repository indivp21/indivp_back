from typing import Dict
from pydantic import BaseModel
from pydantic.errors import ArbitraryTypeError

class IndicadorInDB(BaseModel):
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

database_indicadores = Dict[str, IndicadorInDB]
database_indicadores = {
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"Reclamos - Indicador de reclamos vs Clientes Activos",
							"porcentaje":1.1,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.237.174 // reclamos parcial diciembre radicados 2.534",
							"comentario":"El número de clientes activos corresponde con el valor del mes de noviembre, pendiente actualización  de estos datos desde la Gerencia GCS.",
							"ponderado":1.0,
							"lgreen":1.8,
							"lyellow":"N/A",
							"lred":1.8}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":98.9,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"888 Casos por vencer // 00 casos vencidos // 09 casos prorrogados. Solucionadores 30 DAR y 08 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Habeas Data. 2. NM - Revisión comportamiento y/o condiciones del crédito. 3. NM -Debitó y no Pagó o Entrega parcial de efectivo ATM Otras Redes.",
							"ponderado":97.1,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":95.3,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 49.674 // llamadas atendidas 47.372",
							"comentario":"Sin información",
							"ponderado":96.1,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":97.1,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 2.539 // llamadas atendidas 2.466",
							"comentario":"Sin información",
							"ponderado":91.0,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":98.9,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 5.461 // llamadas atendidas 5.406",
							"comentario":"Sin información",
							"ponderado":97.9,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"WEB CHAT - Nivel de Atencion",
							"porcentaje":99.7,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Chat recibidos 4.309 // Chat atendidos 4.297",
							"comentario":"Sin información",
							"ponderado":99.5,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":48,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 05 presentaron incidencia, para un total 1363 hrs 56 min.",
							"comentario":"Aplicativos con mas bajo desempeño: BACKBASE 0%  // SAPRO 89%. La terminal RDS tambien se vio afectada en 15 hrs 39 min.",
							"ponderado":68.4,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
