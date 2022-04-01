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
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"Reclamos - Indicador de reclamos vs Clientes Activos",
							"porcentaje":1.0,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.291.716 // reclamos radicados parcial Marzo 2397",
							"comentario":"El número de clientes activos tomado del mes de Febrero, pendiente por actualización desde la Gerencia GCS.",
							"ponderado":1.1,
							"lgreen":1.3,
							"lyellow":"N/A",
							"lred":1.3}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":99.2,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"694 Casos por vencer // 00 casos vencidos //  05 casos prorrogados. Solucionadores 29 DAR y 17 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Revisión comportamiento y/o condiciones del crédito. 2. NM - Habeas Data.. 3. NM - Debito y no pago o entrega parcial de efectivo ATM propio.",
							"ponderado":96.8,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":96.0,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 53.048 // llamadas atendidas 50.930",
							"comentario":"Sin informacion",
							"ponderado":96.4,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":95.1,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 3.372 // llamadas atendidas 3.549",
							"comentario":"Presentamos un incremento en las llamadas recibidas en varias franjas, lo que supero nuestra capacidad instalada (franja de break y almuerzos), sumado a esto presentamos un alto número de novedades en personal, por incapacidad, vacaciones o prestamos",
							"ponderado":89.5,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":94.3,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 6.204  // llamadas atendidas 5.584",
							"comentario":"Sin informacion",
							"ponderado":98.3,
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
							"calculo":"Chat recibidos 5.207 // Chat atendidos 5.197",
							"comentario":"Sin informacion",
							"ponderado":99.5,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":38,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 10 presentaron incidencia, para un total 1178 hrs 49 min.",
							"comentario":"Aplicativos con mas bajo desempeño: BACKBASE 0% // PORTAL INTRANET 0% // CREDITO 5.0 47%. Importante mencionar que variasTX Admtivas se vieron muy afectadas. La terminal RDS tambien se vio afectada en 40 hrs 39 min.",
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
