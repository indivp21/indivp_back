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
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Reclamos - Indicador de reclamos vs Clientes Activos",
							"porcentaje":1.1,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.349.262 // reclamos radicados cierre de Agosto 2.628",
							"comentario":"El número de clientes activos tomado del mes de Julio, pendiente por actualización desde la Gerencia GCS.",
							"ponderado":0.8,
							"lgreen":1.2,
							"lyellow":"N/A",
							"lred":1.2}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":100,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"645 Casos por vencer // 00 casos vencidos //  00 casos prorrogados. Solucionadores 26 DAR y 14 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Revisión comportamiento y/o condiciones del crédito. 2.  NM - Debitó y no Pagó o Entrega parcial de efectivo ATM Propio. 3. NM - Habeas Data.",
							"ponderado":98.3,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":94.2,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 53.536 // llamadas atendidas 50.473",
							"comentario":"Se presentó alto trafico de llamadas producto de cierre y comienzo de mes, sumado a esto incidencias en terminal RDS, temas de Impacto, entre otras.",
							"ponderado":93.8,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":94.6,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 3.382 // llamadas atendidas 3.201",
							"comentario":"Se presentó un aumento en las llamadas recibidas en la franja 09:00-11:00 y debido a novedades de personal en la franja en mención, bajo nuestra capacidad de atención, generando un alto numero de abandonos.",
							"ponderado":91.1,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":93.3,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 6.816 // llamadas atendidas 6.364",
							"comentario":"Se presentó colas por fin de mes en horas puntuales, en las cuales no contábamos con la totalidad del personal dada la distribución horaria, lo que originó gran abandono de llamadas.",
							"ponderado":96.8,
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
							"calculo":"Chat recibidos 4.485 // Chat atendidos 4.483",
							"comentario":"Sin información",
							"ponderado":99.5,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":63,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 07 presentaron incidencia, para un total 632 hrs 06 min.",
							"comentario":"Aplicativos con mas bajo desempeño:  STAR SET 0% // B-BACKBASE 0% // SARE TC 55% Importante mencionar que variasTX Admtivas se vieron muy afectadas. La terminal RDS tambien se vio afectada en 37 hrs 10 min.",
							"ponderado":60.3,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
