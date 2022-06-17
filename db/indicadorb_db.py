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
							"porcentaje":0.6,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.335.337 // reclamos radicados parcial Junio 1.479",
							"comentario":"El número de clientes activos tomado del mes de Mayo, pendiente por actualización desde la Gerencia GCS.",
							"ponderado":0.8,
							"lgreen":1.3,
							"lyellow":"N/A",
							"lred":1.3}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":99.5,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"601 Casos por vencer // 00 casos vencidos //  03 casos prorrogados. Solucionadores 31 DAR y 19 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Revisión comportamiento y/o condiciones del crédito. 2. NM - Habeas Data. 3. NM -Compra Tarjeta de Crédito No autorizada.",
							"ponderado":98,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":93.6,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 51.335 // llamadas atendidas 48.094",
							"comentario":"Incidencias varias, inconsistencia terminal RDS.",
							"ponderado":95.6,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":97.9,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 2.841 // llamadas atendidas 2.782",
							"comentario":"Sin informacion",
							"ponderado":91.1,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":96.3,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 6.569 // llamadas atendidas 6.327",
							"comentario":"Sin informacion",
							"ponderado":97.5,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"WEB CHAT - Nivel de Atencion",
							"porcentaje":99.8,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Chat recibidos 4.090 // Chat atendidos 4.085",
							"comentario":"Sin informacion",
							"ponderado":97.2,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":23,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 06 presentaron incidencia, para un total 1.017 hrs 05 min.",
							"comentario":"Aplicativos con mas bajo desempeño:  PORTAL INTRANET 0% // MICROCREDITO MICROFINANZAS 26% Importante mencionar que variasTX Admtivas se vieron muy afectadas. La terminal RDS tambien se vio afectada en 75 hrs 50 min.",
							"ponderado":55.7,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
