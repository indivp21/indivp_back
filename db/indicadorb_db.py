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
							"calculo":"Clientes Activos 2.291.716 // reclamos radicados parcial Abril 706",
							"comentario":"El número de clientes activos tomado del mes de Febrero, pendiente por actualización desde la Gerencia GCS.",
							"ponderado":1.1,
							"lgreen":1.3,
							"lyellow":"N/A",
							"lred":1.3}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":100,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"680 Casos por vencer // 00 casos vencidos //  00 casos prorrogados. Solucionadores 31 DAR y 21 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Revisión comportamiento y/o condiciones del crédito. 2. NM - Debito y no pago o entrega parcial de efectivo ATM propio. 3. NM - Habeas Data.",
							"ponderado":96.8,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":91.2,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 57.352 // llamadas atendidas 52.312",
							"comentario":"Volumen alto de llamadas comienzo de mes, varias incidencias, problemas con la terminal RDS e incidencias de portal empresarial replico en varias llamadas.",
							"ponderado":96.4,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":84.4,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 6.229 // llamadas atendidas 5.258",
							"comentario":"Incidencia en portal empresarial.",
							"ponderado":89.5,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":97.4,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 6.778  // llamadas atendidas 6.605",
							"comentario":"Sin informacion",
							"ponderado":98.3,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"WEB CHAT - Nivel de Atencion",
							"porcentaje":99.9,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Chat recibidos 4.960 // Chat atendidos 4.955",
							"comentario":"Sin informacion",
							"ponderado":99.5,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":36,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 07 presentaron incidencia, para un total 1179 hrs 02 min.",
							"comentario":"Aplicativos con mas bajo desempeño: VPR CREDITO 5.0 0% // PORTAL INTRANET 0% // SARE 43%. Importante mencionar que variasTX Admtivas se vieron muy afectadas. La terminal RDS tambien se vio afectada en 45 hrs 22 min.",
							"ponderado":73.8,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
