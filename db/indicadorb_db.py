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
							"name":"Reclamos - Indicador de reclamos vs Clientes Activos",
							"porcentaje":1.2,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.267.228 // reclamos radicados parcial Febrero 2722",
							"comentario":"El número de clientes activos tomado del mes de Enero, pendiente por actualización desde la Gerencia GCS.",
							"ponderado":0.9,
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
							"calculo":"724 Casos por vencer // 00 casos vencidos //  03 casos prorrogados. Solucionadores 36 DAR y 24 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Revisión comportamiento y/o condiciones del crédito. 2. Debito y no pago o entrega parcial de efectivo ATM Otras redes. 3. NM - Habeas Data.",
							"ponderado":97.6,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":94.5,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 51.307 // llamadas atendidas 48.509",
							"comentario":"Incidencias y lentitud en terminal RDS.",
							"ponderado":95.6,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":82.6,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 4.794 // llamadas atendidas 3.964",
							"comentario":"Altos volúmenes de llamadas debido a proceso de renovación de dispositivo, proceso de desbloqueo de token y activación de token.",
							"ponderado":91.2,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":98.3,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 4.501  // llamadas atendidas 4.428",
							"comentario":"Sin informacion",
							"ponderado":97.7,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"WEB CHAT - Nivel de Atencion",
							"porcentaje":99.6,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Chat recibidos 5.539 // Chat atendidos 5.518",
							"comentario":"Sin informacion",
							"ponderado":99.4,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":50,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 08 presentaron incidencia, para un total 1334 hrs 42 min.",
							"comentario":"Aplicativos con mas bajo desempeño: BACKBASE 0% // PORTAL INTRANET 0% // VRP CREDITO 5.0 57%. Importante mencionar que variasTX Admtivas se vieron afectadas. La terminal RDS tambien se vio afectada en 13 hrs 20 min.",
							"ponderado":61.2,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
