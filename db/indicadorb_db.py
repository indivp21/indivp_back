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
							"porcentaje":0.8,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.267.228 // reclamos radicados parcial Febrero 1996",
							"comentario":"El número de clientes activos tomado del mes de Enero, pendiente por actualización desde la Gerencia GCS.",
							"ponderado":0.9,
							"lgreen":1.3,
							"lyellow":"N/A",
							"lred":1.3}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Reclamos - Nivel de Oportunidad",
							"porcentaje":98.5,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Direccion de Atencion de reclamos",
							"colorin":"3. Green",
							"formula":"(# de casos con vencimiento semana evaluada - prorrogados semana evaluada - vencidos semana evaluada)/# de casos con vencimiento semana evaluada /",
							"calculo":"706 Casos por vencer // 05 casos vencidos //  05 casos prorrogados. Solucionadores 35 DAR y 29 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. Debito y no pago o entrega parcial de efectivo ATM Otras redes. 2. NM - Revisión comportamiento y/o condiciones del crédito. 3. NM - Habeas Data.",
							"ponderado":97.5,
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
							"calculo":"Llamadas recibidas 56.952 // llamadas atendidas 51.975",
							"comentario":"Se presentó lentitud y algunos usuarios bloqueados en terminal RDS. Incidencia, temas de impacto y ausencias afectaron indicadores de la semana..",
							"ponderado":95.6,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":89.9,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 4.043 // llamadas atendidas 3.638",
							"comentario":"Volumen alto de llamadas por renovación de dispositivo, llamadas referentes a pago de nómina y proveedores.",
							"ponderado":91.5,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":97.6,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 6.189  // llamadas atendidas 6.042",
							"comentario":"Sin informacion",
							"ponderado":97.7,
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
							"calculo":"Chat recibidos 6.437 // Chat atendidos 6.408",
							"comentario":"Sin informacion",
							"ponderado":99.4,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":19,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 08 presentaron incidencia, para un total 1546 hrs 08 min.",
							"comentario":"Aplicativos con mas bajo desempeño: BACKBASE 0% // STAR SET 0% // SARE 27%. La terminal RDS tambien se vio afectada en 54 hrs.",
							"ponderado":61.7,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
