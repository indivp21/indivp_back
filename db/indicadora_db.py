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
	"Indicador8": IndicadorInDB(**{"id_indicador": 8,
							"name":"Cajeros: Up time cajeros NCR",
							"porcentaje":97.3,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time cajeros NCR",
							"calculo":"Cantidad de cajeros: 501",
							"comentario":"Up time semanal del  25 de noviembre al 01 de diciembre de 2021",
							"ponderado":97.2,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"Cajeros: Up time cajeros DIEBOLD",
							"porcentaje":96.5,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Up time cajeros DIEBOLD",
							"calculo":"Cantidad de cajeros: 190",
							"comentario":"Up time semanal del  25 de noviembre al 01 de diciembre de 2021.  Los atm´s Diebold incrementaron catidad de fallas. Se recomienda seguimiento al proveedor.",
							"ponderado":96.8,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Cajeros: Up time Multifuncionales DIEBOLD",
							"porcentaje":95.3,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time Multifuncionales DIEBOLD",
							"calculo":"Cantidad de MF: 55",
							"comentario":"Up time semanal del  25 de noviembre al 01 de diciembre de 2021",
							"ponderado":94.2,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"Efectivo: Cumplimiento Saldo de Caja",
							"porcentaje":89.9,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Total meta  / Total promedio semana (meta  para el 2021:  $570,000,000,000 promd)",
							"calculo":"Saldo promedio: $656.145.541.503",
							"comentario":"Semana del 25 Noviembre al 01 Diciembre, se incremento saldo de caja debido a la necesidades de efectivo para cubrir la operación por la temporada alta.",
							"ponderado":97.2,
							"lgreen":100,
							"lyellow":"95",
							"lred":95}),
	"Indicador11": IndicadorInDB(**{"id_indicador": 11,
							"name":"Transferencias Electrónicas. Calidad lotes  aplicados",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Lotes aplicados / Lotes recibidos",
							"calculo":"Lotes aplicados: 51.311                                                                               Valor Total $760,185,986,470.95",
							"comentario":"Semana del 26 de noviembre al 2 de diciembre.",
							"ponderado":99.6,
							"lgreen":100,
							"lyellow":"90",
							"lred":90}),
	"Indicador12": IndicadorInDB(**{"id_indicador": 12,
							"name":"Canje: Oportunidad compensación todas las Centrales.",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Centrales de Canje con compensación canje / transmisión a Banco de la República oportunamente",
							"calculo":"Centrales de Canje: 38. 8 Cedec, 17 CUD o delegadas teercerizadas y 13 propias delegadas. Valor Canje Rec.: $150.097.141.814.56 Valor Canje Env.: $119.521.635.537.14",
							"comentario":"c",
							"ponderado":100.0,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
	"Indicador9": IndicadorInDB(**{"id_indicador": 9,
							"name":"Oportunidad en la atención de Embargos-Desembargos",
							"porcentaje":99,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Atención Requerimientos de Entes Extern",
							"colorin":"3. Green",
							"formula":"Embargos-Desembargos atendidos oportunamente /Total Embargos-Desembargos radicados *Fuente: Sistema de embargos",
							"calculo":"Identificaciones Capturadas 76.225 Identificaciones Oportunas (1-3 días) 75.459 Identificaciones Inoportunas(4 - más días) 513 Identificaciones Pendientes 253",
							"comentario":"Semana del  22 al 28 de noviembre de 2021",
							"ponderado":96.3,
							"lgreen":98,
							"lyellow":"92",
							"lred":92}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CSCB: Atención casos escalados por OMAT por correo (En construcción y validación con otras áreas)",
							"porcentaje":78.2,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte a Aplicaciones",
							"colorin":"2. Yellow",
							"formula":"# de casos atendidos / # casos escalados por OMAT por correo Fuente: Correos enviados por OMAT y registro de los casos atendidos en el grupo.",
							"calculo":"358 (# casos escalados por OMAT por correo)",
							"comentario":"Semana de 26 Noviembre al 02 Diciembre",
							"ponderado":82.3,
							"lgreen":100,
							"lyellow":"76",
							"lred":76}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"COI: Cumplimiento de operaciones Clientes",
							"porcentaje":92.5,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Coordinación Moneda Extranjera",
							"colorin":"2. Yellow",
							"formula":"Operaciones para tramitar en el exterior/ Operaciones enviadas por oficinas.",
							"calculo":"Op. Recibidas de clientes 431 Op. Cumplidas 399 por valor de USD 7,846,052,13",
							"comentario":"El incumplimiento se debe a inconsisistencias presentadas en las operaciones que no lograron ser corregidas el mismo día en que las solicita el cliente, estas operaciones habitualmente se tramitan al día siguiente de su recepción",
							"ponderado":90.9,
							"lgreen":100,
							"lyellow":"90",
							"lred":90}),
	"Indicador13": IndicadorInDB(**{"id_indicador": 13,
							"name":"CC: Oportunidad en conciliación",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Cuadre",
							"colorin":"3. Green",
							"formula":"Canales  a conciliar (oficinas, centros de canje, cajeros corresponsales propios, Carvajal, Efectivo clientes, centros de efectivo, AFC, impuestos, ACH, transferencias ya, mi pago amigo ) / canales  conciliados",
							"calculo":"6,613 puntos conciliados 4,412 Ajustes aplicados",
							"comentario":"Semana de 26 Noviembre al 02 Diciembre",
							"ponderado":99.2,
							"lgreen":100,
							"lyellow":"90",
							"lred":90}),
	"Indicador10": IndicadorInDB(**{"id_indicador": 10,
							"name":"CC: Partidas pendientes mayores a 30 días",
							"porcentaje":99.5,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Cuadre",
							"colorin":"3. Green",
							"formula":"Partidas conciliatorias mayores a 30 días sin ajustar resultado de la conciliación contable  mensual con corte al mes anterior / total partidas conciliatorias presentadas durante el  mes",
							"calculo":"33 partidas por $ 28,410,827,84 con corte Octubre 31/2021",
							"comentario":"Semana de 26 Noviembre al 02 Diciembre",
							"ponderado":99.1,
							"lgreen":90,
							"lyellow":"N/A",
							"lred":90}),
	"Indicador14": IndicadorInDB(**{"id_indicador": 14,
							"name":"CCE: Oportunidad en la inclusión de negociaciones vinculación o mantenimiento Clientes Empresariales",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Operaciones Convenios Empresariales",
							"colorin":"3. Green",
							"formula":"Solicitudes atendidas oportunamente (Fuente Herramienta de negociación Star Cash estado de la propuesta) / Total solicitudes recibidas (Fuente excel herremienta de gestión y Control Cash relación diaria)",
							"calculo":"187",
							"comentario":"Semana del 26 de Noviembre al 2 de Diciembre de 2021",
							"ponderado":99.8,
							"lgreen":100,
							"lyellow":"97.9",
							"lred":97.9}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"COE: Oportunidad transacciones atendidas en los tiempos definidos ANS",
							"porcentaje":96.3,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Centro Operación Empresarial  - Fiduciario",
							"colorin":"3. Green",
							"formula":"Transacciones cumplidas según ANS / solicitudes radicadas [Fuente: Excel - Inventario de solicitudes]",
							"calculo":"49530 Q $18,2 billones semanal: $1,393 mm",
							"comentario":"",
							"ponderado":97.8,
							"lgreen":95,
							"lyellow":"90",
							"lred":90}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"CCB: Oportunidad en la disponibilidad del Canal Modelo Propio",
							"porcentaje":95.9,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"1 - (Número de transacciones Rechazadas / Número de transacciones Exitosas)",
							"calculo":"=1-(7594/187623)",
							"comentario":"Aunque la causal de rechazo más relevante a cierre noviembre fue fondos insuficientes para el retiro con un 35% esta no obedece a factores propios de la Entidad, comportamiento que permanece en los dos priemros días de diciembre Mientras que el error",
							"ponderado":101.5,
							"lgreen":95,
							"lyellow":"93",
							"lred":93}),
	"Indicador15": IndicadorInDB(**{"id_indicador": 15,
							"name":"CCB: Oportunidad en la disponibilidad del Canal Carvajal",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"La información es generada por el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas.",
							"calculo":"",
							"comentario":"Información suministrada por el aliado Carvajal cierre Noviembre: La información es generada por assenda red, el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas. No presentó afec",
							"ponderado":97,
							"lgreen":98,
							"lyellow":"97.6",
							"lred":97.6}),
	"Indicador16": IndicadorInDB(**{"id_indicador": 16,
							"name":"BO: Oportunidad en el cumplimiento de operaciones del Piso Financiero y otras Áreas de las empresas",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "UAC Back Office",
							"colorin":"3. Green",
							"formula":"Número total operaciones cumplidas/ operaciones a cumplir.",
							"calculo":"626 operaciones por $12,736´´581´614,057,40",
							"comentario":"",
							"ponderado":100.0,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
