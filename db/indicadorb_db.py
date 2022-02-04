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
							"porcentaje":0.1,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.246.465 // reclamos radicados parcial Febrero 390",
							"comentario":"El número de clientes activos tomado del mes de Diciembre, la meta tomada del mes de Enero, ambos pendiente por actualización desde la Gerencia GCS.",
							"ponderado":0.9,
							"lgreen":1.3,
							"lyellow":"N/A",
							"lred":1.3}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":99.5,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"673 Casos por vencer // 00 casos vencidos //  03 casos prorrogados. Solucionadores 26 DAR y 18 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Revisión comportamiento y/o condiciones del crédito. 2. Debito y no pago o entrega parcial de efectivo ATM Otras redes. 3. NM - Habeas Data.",
							"ponderado":97.4,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":92.4,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 58.772 // llamadas atendidas 54.324",
							"comentario":"Se presenta volumen alto de llamadas producto cierre y comienzo de mes, incidencias y temas de impacto, como tambien varias ausencias.",
							"ponderado":95.8,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":89.3,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 3.788 // llamadas atendidas 3.383",
							"comentario":"Alto flujo de llamadas por temas de lotes, activacion de portal, activacion de token, renovaciones, desbloqueo, entre otros.",
							"ponderado":91.6,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":96.6,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 7.144  // llamadas atendidas 6.906",
							"comentario":"",
							"ponderado":97.7,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"WEB CHAT - Nivel de Atencion",
							"porcentaje":96.5,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Chat recibidos 6.767 // Chat atendidos 6.531",
							"comentario":"",
							"ponderado":99.4,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":48,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 05 presentaron incidencia, para un total 1216 hrs 59 min.",
							"comentario":"Aplicativos con mas bajo desempeño: BACKBASE 0%  // OPENCARD TC 44%. La terminal RDS tambien se vio afectada en 22 hrs 38 seg.",
							"ponderado":66,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
