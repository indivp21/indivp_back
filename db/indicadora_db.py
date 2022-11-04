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
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"Cajeros: Up time cajeros NCR",
							"porcentaje":97.3,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time cajeros NCR",
							"calculo":"Cantidad de cajeros: 453",
							"comentario":"up time semanal del 27 de octubre al 03 de noviembre",
							"ponderado":97.2,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"Cajeros: Up time cajeros DIEBOLD",
							"porcentaje":95.0,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Up time cajeros DIEBOLD",
							"calculo":"Cantidad de cajeros: 170",
							"comentario":"up time semanal del 27 de octubre al 03 de noviembre - las fallas de hardware, la inoportunidad en la atención de servicios, la falta de gestión del proveedor y la alta operación de fin de mes afectaron el indicador semanal - se está realizando segui",
							"ponderado":96.1,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"Cajeros: Up time Multifuncionales DIEBOLD",
							"porcentaje":94.5,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Up time Multifuncionales DIEBOLD",
							"calculo":"Cantidad de MF: 55",
							"comentario":"up time semanal del 27 de octubre al 03 de noviembre - las fallas de hardware, la inoportunidad en la atención de servicios, la falta de gestión del proveedor y la alta operación de fin de mes afectaron el indicador semanal - se está realizando segui",
							"ponderado":93.9,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Efectivo: Cumplimiento Saldo de Caja",
							"porcentaje":97.2,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"2. Yellow",
							"formula":"Total meta  / Total promedio semana (meta  para el 2021:  $660,000,000,000 promd)",
							"calculo":"Saldo promedio: $678.464.643.985",
							"comentario":"Semana 26 octubre 2022 al 02 noviembre 2022 Pago nómina Colpensiones",
							"ponderado":98.9,
							"lgreen":100,
							"lyellow":"97",
							"lred":97}),
	"Indicador12": IndicadorInDB(**{"id_indicador": 12,
							"name":"Transferencias Electrónicas. Calidad lotes  aplicados",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Lotes aplicados / Lotes recibidos",
							"calculo":"Lotes aplicados: 56.951                                                    Valor Total $744.217.462.094.86",
							"comentario":"Semana del 28 de octubre al 3 de noviembre",
							"ponderado":99.5,
							"lgreen":100,
							"lyellow":"90",
							"lred":90}),
	"Indicador13": IndicadorInDB(**{"id_indicador": 13,
							"name":"Canje: Oportunidad compensación todas las Centrales.",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Centrales de Canje con compensación canje / transmisión a Banco de la República oportunamente",
							"calculo":"Centrales de Canje: 38. 8 Cedec, 17 CUD o delegadas teercerizadas y 13 propias delegadas. Valor Canje Rec.: $109.279.376.823.13 Valor Canje Env.: $111.025.856.154.09",
							"comentario":"Semana del 26 octubre al 01 de noviembre",
							"ponderado":100.0,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
	"Indicador10": IndicadorInDB(**{"id_indicador": 10,
							"name":"Oportunidad en la atención de Embargos-Desembargos",
							"porcentaje":99.7,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Atención Requerimientos de Entes Extern",
							"colorin":"3. Green",
							"formula":"Embargos-Desembargos atendidos oportunamente /  Total Embargos-Desembargos radicados *Fuente: Sistema de embargos",
							"calculo":"Identificaciones Capturadas 61.544 Identificaciones Oportunas (1-3 dias)  61.353 Identificaciones Inoportunas (4 ó mas dias )  152 Identificaciones Pendientes 39",
							"comentario":"Semana del 24 al 30 de octubre de 2022",
							"ponderado":97.2,
							"lgreen":96,
							"lyellow":"92",
							"lred":92}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"CSCB: Atención casos escalados por OMAT por correo (En construcción y validación con otras áreas)",
							"porcentaje":95.6,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte a Aplicaciones",
							"colorin":"2. Yellow",
							"formula":"# de casos atendidos / # casos asignados en Service Now Fuente: Notificaciones enviadas por Service Now y registro de los casos atendidos en el grupo..",
							"calculo":"300 (# casos asignados en Service Now)",
							"comentario":"Semana del 28 octubre al 3 de noviembre",
							"ponderado":86.6,
							"lgreen":100,
							"lyellow":"76",
							"lred":76}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"COI: Cumplimiento de operaciones Clientes",
							"porcentaje":92.6,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Coordinación Moneda Extranjera",
							"colorin":"2. Yellow",
							"formula":"Operaciones para tramitar en el exterior/ Operaciones enviadas por oficinas.",
							"calculo":"Op. Recibidas de clientes 392 Op. Cumplidas 363 por valor de USD 5,327,193,04",
							"comentario":"Semana del 28 octubre al 3 de noviembre",
							"ponderado":91.1,
							"lgreen":100,
							"lyellow":"90",
							"lred":90}),
	"Indicador14": IndicadorInDB(**{"id_indicador": 14,
							"name":"CC: Oportunidad en conciliación",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Cuadre",
							"colorin":"3. Green",
							"formula":"Canales  a conciliar (oficinas, centros de canje, cajeros corresponsales propios, Carvajal, Efectivo clientes,centros de efectivo,AFC,impuestos, ACH, transferencias ya, mi pago amigo ) / canales  conciliados",
							"calculo":"5.801 puntos conciliados 8.955 ajustes aplicados",
							"comentario":"Semana del 28 de octubre al 03 de noviembre",
							"ponderado":99.3,
							"lgreen":100,
							"lyellow":"90",
							"lred":90}),
	"Indicador11": IndicadorInDB(**{"id_indicador": 11,
							"name":"CC: Partidas pendientes mayores a 30 días",
							"porcentaje":99.9,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Cuadre",
							"colorin":"3. Green",
							"formula":"Partidas conciliatorias mayores a 30 días sin ajustar resultado de la conciliación contable  mensual con corte al mes anterior / total partidas conciliatorias presentadas durante el  mes",
							"calculo":"7 por $ 5.720.155 corte septiembre 30 de 2.022",
							"comentario":"Semana del 21  al 27 de octubre",
							"ponderado":99.1,
							"lgreen":90,
							"lyellow":"N/A",
							"lred":90}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"CCE: Oportunidad en la inclusión de negociaciones vinculación o mantenimiento Clientes Empresariales",
							"porcentaje":96.7,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Operaciones Convenios Empresariales",
							"colorin":"1. Red",
							"formula":"Solicitudes atendidas oportunamente (Fuente Herramienta de negociación Star Cash estado de la propuesta) / Total solicitudes recibidas (Fuente excel herremienta de gestión y Control Cash relación diaria)",
							"calculo":"Solicitudes recibidas: 170 Atendidas:165 Total Servicios Activados: 338 Creación de Servicios: Recibidos:160 - Atendidos: 29",
							"comentario":"Semana del 28 octubre al 02 de noviembre de 2022",
							"ponderado":99.2,
							"lgreen":100,
							"lyellow":"97",
							"lred":97}),
	"Indicador9": IndicadorInDB(**{"id_indicador": 9,
							"name":"COE: Oportunidad transacciones atendidas en los tiempos definidos ANS",
							"porcentaje":98.8,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Centro Operación Empresarial  - Fiduciario",
							"colorin":"3. Green",
							"formula":"Transacciones cumplidas según ANS / solicitudes radicadas [Fuente: Excel - Inventario de solicitudes]",
							"calculo":"Semanal:   Q 1,165    $224,432 MMI",
							"comentario":"Semana del 28 octubre al 3 de noviembre",
							"ponderado":97.5,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador8": IndicadorInDB(**{"id_indicador": 8,
							"name":"CCB: DISPONIBILIDAD Transaccioalidad corresponsales bancarios modelo propio",
							"porcentaje":97.0,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"1 - (Número de transacciones Rechazadas / Número de transacciones Exitosas)",
							"calculo":"=1-(5981/202253)",
							"comentario":"Se detalla los rechazos operacionales de transaccionalidad en el canal, donde el mayor volumen o relevancia no son atribuibles a fallas del canal, sin embargo, se presentaron 292 trx con error de verificación de estatus: W2- FONDOS INSUFICIENTES PARA",
							"ponderado":99.3,
							"lgreen":95,
							"lyellow":"93",
							"lred":93}),
	"Indicador15": IndicadorInDB(**{"id_indicador": 15,
							"name":"CCB: DISPONIBILIDAD Oportunidad en la disponibilidad del Canal Carvajal",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"La información es generada por el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas.",
							"calculo":"La información es generada por el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas.",
							"comentario":"Información suministrada por el aliado Carvajal a corte 15 de octubre 2022. La información es generada por assenda red, el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas. No se",
							"ponderado":98.8,
							"lgreen":99.6,
							"lyellow":"97",
							"lred":97}),
	"Indicador16": IndicadorInDB(**{"id_indicador": 16,
							"name":"Número total operaciones cumplidas/ operaciones a cumplir.",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "UAC Back Office",
							"colorin":"3. Green",
							"formula":"Número total operaciones cumplidas/ operaciones a cumplir.",
							"calculo":"Se atendieron 634 operaciones por un valor de $3.265.723.870.372.28",
							"comentario":"Semana del 28 octubre al 3 de noviembre",
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
