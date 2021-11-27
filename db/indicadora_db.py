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
							"porcentaje":97.5,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time cajeros NCR",
							"calculo":"Cantidad de cajeros: 501",
							"comentario":"Up time semanal del 18 al 24 de noviembre",
							"ponderado":97.2,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"Cajeros: Up time cajeros DIEBOLD",
							"porcentaje":96.9,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Up time cajeros DIEBOLD",
							"calculo":"Cantidad de cajeros: 190",
							"comentario":"Up time semanal del 18 al 24 de noviembre - algunos ATM´s Diebold presentaron fallas constantes y su recuperación demandó mayor tiempo - Los ATM´s afectados quedaron en seguimiento.",
							"ponderado":96.8,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Cajeros: Up time Multifuncionales DIEBOLD",
							"porcentaje":95.5,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time Multifuncionales DIEBOLD",
							"calculo":"Cantidad de MF: 55",
							"comentario":"Up time semanal del 18 al 24 de noviembre",
							"ponderado":94.2,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"Efectivo: Cumplimiento Saldo de Caja",
							"porcentaje":97.2,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"2. Yellow",
							"formula":"Total meta  / Total promedio semana (meta  para el 2021:  $570,000,000,000 promd)",
							"calculo":"Saldo promedio: $606,435,053,940",
							"comentario":"Semana del 18 al 24 Noviembre",
							"ponderado":97.5,
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
							"calculo":"Lotes aplicados: 32.902                                                                               Valor Total $489,750,383,907.74",
							"comentario":"Semana del 19 al 25 de noviembre.",
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
							"calculo":"Centrales de Canje: 38. 8 Cedec, 17 CUD o delegadas teercerizadas y 13 propias delegadas. Valor Canje Rec.: $138.441.725.146.13 Valor Canje Env.: $122.663.360.598.19",
							"comentario":"Semana del 18 al 24 noviembre",
							"ponderado":100.0,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
	"Indicador9": IndicadorInDB(**{"id_indicador": 9,
							"name":"Oportunidad en la atención de Embargos-Desembargos",
							"porcentaje":99.1,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Atención Requerimientos de Entes Extern",
							"colorin":"3. Green",
							"formula":"Embargos-Desembargos atendidos oportunamente /Total Embargos-Desembargos radicados *Fuente: Sistema de embargos",
							"calculo":"Identificaciones Capturadas 12.101 Identificaciones Oportunas (1-3 días) 12.002 Identificaciones Inoportunas(4 - más días) 72 Identificaciones Pendientes 27",
							"comentario":"Semana del  15 al 21 de noviembre de 2021",
							"ponderado":96.3,
							"lgreen":98,
							"lyellow":"92",
							"lred":92}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"CSCB: Atención casos escalados por OMAT por correo (En construcción y validación con otras áreas)",
							"porcentaje":78.3,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte a Aplicaciones",
							"colorin":"2. Yellow",
							"formula":"# de casos atendidos / # casos escalados por OMAT por correo Fuente: Correos enviados por OMAT y registro de los casos atendidos en el grupo.",
							"calculo":"286 (# casos escalados por OMAT por correo)",
							"comentario":"Semana del 19 al 25 de noviembre.",
							"ponderado":82.3,
							"lgreen":100,
							"lyellow":"76",
							"lred":76}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"COI: Cumplimiento de operaciones Clientes",
							"porcentaje":91.1,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Coordinación Moneda Extranjera",
							"colorin":"2. Yellow",
							"formula":"Operaciones para tramitar en el exterior/ Operaciones enviadas por oficinas.",
							"calculo":"Op. Recibidas de clientes 337 Op. Cumplidas 307 por valor de USD 3,997,7644,55",
							"comentario":"Semana del 19 al 25 de noviembre.",
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
							"formula":"Canales  a conciliar (oficinas, centros de canje, cajeros corresponsales propios, Carvajal, Efectivo clientes,centros de efectivo,AFC,impuestos, ACH, transferencias ya, mi pago amigo ) / canales  conciliados",
							"calculo":"6.619 puntos conciliados 8.566 ajustes aplicados",
							"comentario":"Semana del 19 al 25 de noviembre.",
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
							"calculo":"33 partidas por $ 28,410,827,84 corte octubre 31-2021",
							"comentario":"Semana del 19 al 25 de noviembre.",
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
							"calculo":"213",
							"comentario":"Semana del 19 al 25 de Noviembre de 2021",
							"ponderado":99.8,
							"lgreen":100,
							"lyellow":"97.9",
							"lred":97.9}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"COE: Oportunidad transacciones atendidas en los tiempos definidos ANS",
							"porcentaje":96.8,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Centro Operación Empresarial  - Fiduciario",
							"colorin":"3. Green",
							"formula":"Transacciones cumplidas según ANS / solicitudes radicadas [Fuente: Excel - Inventario de solicitudes]",
							"calculo":"Acumul  Q 48076     $ 17,9 Bll Semana  Q   1097    $    286 MMll.",
							"comentario":"Semana del 19 al 25 de Noviembre 2021",
							"ponderado":97.8,
							"lgreen":95,
							"lyellow":"90",
							"lred":90}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"CCB: Oportunidad en la disponibilidad del Canal Modelo Propio",
							"porcentaje":96.5,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"1 - (Número de transacciones Rechazadas / Número de transacciones Exitosas)",
							"calculo":"=1-(5297/152559)",
							"comentario":"Indicador proporcionado por Movistar Empresas, tipo de indicador es por enlace de nivel one, que emite comunicación al rauter. Cuentan con dos reguladores en caso de falla en un rauter por criticidad, se cuenta con un segundo soporte en el data cente",
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
							"formula":,
							"calculo":"La información es generada por el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas.",
							"comentario":"Información suministrada por el aliado Carvajal cierre Octubre: La información es generada por assenda red, el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas. No presentó afecta",
							"ponderado":97,00,
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
							"calculo":"Se atendieron un total de 607 operaciones por valor de $10.862.387.452.361.70",
							"comentario":"Semana del 19 al 25 de noviembre.",
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
