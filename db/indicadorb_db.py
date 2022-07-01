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
							"porcentaje":1.1,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.335.337 // reclamos radicados Junio 2.636",
							"comentario":"El número de clientes activos tomado del mes de Mayo, pendiente por actualización desde la Gerencia GCS.",
							"ponderado":0.9,
							"lgreen":1.3,
							"lyellow":"N/A",
							"lred":1.3}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":99.8,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"601 Casos por vencer // 01 casos vencidos //  00 casos prorrogados. Solucionadores 32 DAR y 24 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Revisión comportamiento y/o condiciones del crédito. 2. NM -Compra Tarjeta de Crédito No autorizada. 3. NM - Habeas Data.",
							"ponderado":97.8,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":90.1,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 46.095 // llamadas atendidas 41.546",
							"comentario":"Incremento de llamadas cierre de mes, adicional se presentó incidencias en el  Portal Transaccional, entre otras e inconsistencia en terminal RDS.",
							"ponderado":94.5,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":96.5,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 2.520 // llamadas atendidas 2.434",
							"comentario":"Sin informacion",
							"ponderado":89.5,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":94.2,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 6.202 // llamadas atendidas 5.843",
							"comentario":"Incremento de llamadas, incidencias en Avaya,  adicionalmente se presentaron intermitencias en la página Web y la App y sumado a esto novedades de personal.",
							"ponderado":96.9,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"WEB CHAT - Nivel de Atencion",
							"porcentaje":99.5,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Chat recibidos 3.839 // Chat atendidos 3.821",
							"comentario":"Sin informacion",
							"ponderado":99.4,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":14,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 08 presentaron incidencia, para un total 1.027 hrs 36 min.",
							"comentario":"Aplicativos con mas bajo desempeño:  PORTAL INTRANET 0% // STAR SET 0% // SARE 6%  Importante mencionar que variasTX Admtivas se vieron muy afectadas. La terminal RDS tambien se vio afectada en 135 hrs 20 min.",
							"ponderado":57.9,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
