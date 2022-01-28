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
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"Indicador",
							"porcentaje":Resul,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Area que reporta",
							"colorin":"3. Green",
							"formula":"Fórmula",
							"calculo":"Valores",
							"comentario":"Observaciones",
							"ponderado":Ponde,
							"lgreen":Meta,
							"lyellow":"Valor",
							"lred":Valor}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Reclamos - Indicador de reclamos vs Clientes Activos",
							"porcentaje":1.1,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.246.465 // reclamos radicados parcial Enero 2537",
							"comentario":"El número de clientes activos y la meta corresponde con el valor del mes de diciembre, ambos pendiente por actualización desde la Gerencia GCS.",
							"ponderado":1.0,
							"lgreen":1.8,
							"lyellow":"N/A",
							"lred":1.8}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":97.4,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"1. Red",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"705 Casos por vencer // 04 casos vencidos // 14 casos prorrogados. Solucionadores 24 DAR y 19 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Revisión comportamiento y/o condiciones del crédito. 2. NM - Habeas Data. 3. NM -Compra Tarjeta de Crédito No autorizada.",
							"ponderado":97.4,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":98.4,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 45.224 // llamadas atendidas 44.521",
							"comentario":"",
							"ponderado":96.0,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":93.4,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 3.121 // llamadas atendidas 2.915",
							"comentario":"Se presento incrmento de llamadas por diferentes temas, se realiza movimiento de mallas de personal, para dar mejor atención en horas pico.",
							"ponderado":92.0,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador8": IndicadorInDB(**{"id_indicador": 8,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":98.1,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 5.767  // llamadas atendidas 5.661",
							"comentario":"",
							"ponderado":97.6,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"WEB CHAT - Nivel de Atencion",
							"porcentaje":94.4,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Chat recibidos 5.579 // Chat atendidos 5.270",
							"comentario":"Salió atención con la nueva actualización de Zendesk herramienta que esta en proceso de estabilización, sumado a esto se presentaron varias ausencias.",
							"ponderado":99.2,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":62,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 08 presentaron incidencia, para un total 1133 hrs 25 min.",
							"comentario":"Aplicativos con mas bajo desempeño: BACKBASE 0%  // STAR SET (Acme) 39%. La terminal RDS tambien se vio afectada en 4 hrs 48 seg.",
							"ponderado":67.6,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
