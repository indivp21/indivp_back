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
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"Reclamos - Indicador de reclamos vs Clientes Activos",
							"porcentaje":0.2,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.237.174 // reclamos radicados parcil Enero 585",
							"comentario":"El número de clientes activos corresponde con el valor del mes de noviembre y la meta se toma la del mes de diciembre, ambos pendiente por actualización desde la Gerencia GCS.",
							"ponderado":1.0,
							"lgreen":1.8,
							"lyellow":"N/A",
							"lred":1.8}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":98.7,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"624 Casos por vencer // 01 casos vencidos // 07 casos prorrogados. Solucionadores 27 DAR y 15 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Revisión comportamiento y/o condiciones del crédito. 2. NM -Debitó y no Pagó o Entrega parcial de efectivo ATM Otras Redes. 3. NM - Inconsistencia en compra o pago en canales virtuales.",
							"ponderado":97.3,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":91.9,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 39.483 // llamadas atendidas 36.307",
							"comentario":"Se presntó alto volumen de llamadas consecuencia de cierre y comienzo de mes, incidencias, temas de impacto y afectacion de indicador por ausencias.",
							"ponderado":95.9,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":99.3,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 1.450 // llamadas atendidas 1.440",
							"comentario":"Sin informacion",
							"ponderado":91.8,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":96.2,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 4.803  // llamadas atendidas 4.621",
							"comentario":"Sin informacion",
							"ponderado":97.7,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"WEB CHAT - Nivel de Atencion",
							"porcentaje":99.9,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Chat recibidos 4.021 // Chat atendidos 4.017",
							"comentario":"Sin informacion",
							"ponderado":99.6,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":56,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 04 presentaron incidencia, para un total 897 hrs 08 seg.",
							"comentario":"Aplicativos con mas bajo desempeño: BACKBASE 0%  // TX ADMINISTRATIVAS 72%. La terminal RDS tambien se vio afectada en 25 hrs 04 seg.",
							"ponderado":66.9,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
