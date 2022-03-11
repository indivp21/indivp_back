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
							"porcentaje":0.4,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"No_reclamos radicados*1000) / No_clientes_activos",
							"calculo":"Clientes Activos 2.291.716 // reclamos radicados parcial Marzo 1099",
							"comentario":"El número de clientes activos tomado del mes de Febrero, pendiente por actualización desde la Gerencia GCS.",
							"ponderado":1.1,
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
							"calculo":"716 Casos por vencer // 00 casos vencidos //  01 casos prorrogados. Solucionadores 36 DAR y 19 áreas descentralizadas.",
							"comentario":"Top 3 de la semana: 1. NM - Revisión comportamiento y/o condiciones del crédito. 2. NM - Habeas Data.. 3. NM - Debito y no pago o entrega parcial de efectivo ATM propio.",
							"ponderado":96.6,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CAT PNA - Nivel de Atencion",
							"porcentaje":90.9,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 71.814 // llamadas atendidas 54.417",
							"comentario":"Volúmenes altos de llamadas comienzo de mes, llamadas del canal Digital, temas de impacto, lentitud en RDS, incidencias en aplicativos del banco e incidencia en pagina transaccional.",
							"ponderado":96.4,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CAT Empresarial  - Nivel de Atencion",
							"porcentaje":65.2,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 7.943 // llamadas atendidas 3.597",
							"comentario":"Estamos en atención de la linea empresarial para renovación de Token, se tiene volumen alto de llamadas, superando asi nuestra capacidad instalada y generando un alto numero de abandonos.",
							"ponderado":89.2,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CAT DIGITAL - Nivel de Atencion",
							"porcentaje":96.2,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"3. Green",
							"formula":"# casos redicados / # casos atendidos",
							"calculo":"Llamadas recibidas 7.400  // llamadas atendidas 5.995",
							"comentario":"Sin informacion",
							"ponderado":98.4,
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
							"calculo":"Chat recibidos 6.774 // Chat atendidos 6.715",
							"comentario":"Sin informacion",
							"ponderado":99.5,
							"lgreen":92,
							"lyellow":"N/A",
							"lred":92}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CAT PNA - -Disponibilidad aplicativos",
							"porcentaje":62,
							"gerencia":"Gerencia Servivio a Cliente",
							"central": "Gerencia de servicio a cliente",
							"colorin":"1. Red",
							"formula":"# de horas con incidencia / (24 hrs*7 dias *19 aplicativos)",
							"calculo":"Total aplicativos 19 // 09 presentaron incidencia, para un total 1532 hrs 23 min.",
							"comentario":"Aplicativos con mas bajo desempeño: BACKBASE 0% // PORTAL INTRANET 0% // STAR SET 0%  // VPR CREDITO 5.0 0%. Importante mencionar que variasTX Admtivas se vieron muy afectadas. La terminal RDS tambien se vio afectada en 63 hrs 16 min.",
							"ponderado":75.6,
							"lgreen":99,
							"lyellow":"N/A",
							"lred":99}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
