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
							"porcentaje":0.3,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.369.576 // reclamos radicados corte noviembre 805",
							"comentario":"El número de clientes activos tomado del mes de Septiembre, pendiente por actualización desde la Gerencia GCS.",
							"ponderado":0.8,
							"lgreen":1.1,
							"lyellow":"N/A",
							"lred":1.1}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":100,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"426 Casos por vencer // 00 casos vencidos //  00 casos prorrogados. Solucionadores 26 DAR y 11 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Habeas Data.  2. NM - Revisión comportamiento y/o condiciones del crédito. 3. NM - Debitó y no Pagó o Entrega parcial de efectivo ATM Propio.",
							"ponderado":98.5,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":89.8,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 48.323 // llamadas atendidas 43.427",
							"comentario":"Incremento de llamadas pos festivo, incidencias varias en RDS, entre otras.",
							"ponderado":94.1,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":96.1,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 2.527 // llamadas atendidas 2.429",
							"comentario":"Sin informacion",
							"ponderado":92.0,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":98.7,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 4.339 // llamadas atendidas 4.283",
							"comentario":"Sin informacion",
							"ponderado":96.9,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"WEB CHAT - Nivel de Atencion",
							"porcentaje":98.7,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Chat recibidos 3.840 // Chat atendidos 3.793",
							"comentario":"Sin informacion",
							"ponderado":99.5,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":81,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 07 presentaron incidencia, para un total 400 hrs 29 min.",
							"comentario":"Aplicativos con mas bajo desempeño:  STAR SET 0% //  SOS.NET 0% // SARE 79% Importante mencionar que variasTX Admtivas se vieron muy afectadas. La terminal RDS tambien se vio afectada en 11 hrs 38 min..",
							"ponderado":61.3,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
