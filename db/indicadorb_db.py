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
							"porcentaje":1.4,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.237.174 // reclamos diciembre radicados 3.184",
							"comentario":"El número de clientes activos corresponde con el valor del mes de noviembre, pendiente actualización  de estos datos desde la Gerencia GCS.",
							"ponderado":1.0,
							"lgreen":1.8,
							"lyellow":"N/A",
							"lred":1.8}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":99.5,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"697 Casos por vencer // 00 casos vencidos // 03 casos prorrogados. Solucionadores 28 DAR y 15 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM -Debitó y no Pagó o Entrega parcial de efectivo ATM Otras Redes. 2. NM - Revisión comportamiento y/o condiciones del crédito. 3. NM - Inconsistencia en compra o pago en canales virtuales.",
							"ponderado":97.2,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":97.3,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 45.447 // llamadas atendidas 44.262",
							"comentario":"Sin informacion",
							"ponderado":96.2,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":96.6,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 2.421 // llamadas atendidas 2.339",
							"comentario":"Sin informacion",
							"ponderado":91.3,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":96.8,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 4.748  // llamadas atendidas 4.600",
							"comentario":"Sin informacion",
							"ponderado":97.8,
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
							"calculo":"Chat recibidos 3.734 // Chat atendidos 3.730",
							"comentario":"Sin informacion",
							"ponderado":99.5,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":53,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 08 presentaron incidencia, para un total 1337 hrs 40 min.",
							"comentario":"Aplicativos con mas bajo desempeño: BACKBASE 0%  // SOS.NET 57%. La terminal RDS tambien se vio afectada en 8 hrs 0,8 min.",
							"ponderado":67.5,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
