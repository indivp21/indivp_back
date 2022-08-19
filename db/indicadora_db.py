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
							"porcentaje":97.9,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time cajeros NCR",
							"calculo":"Cantidad de cajeros: 453",
							"comentario":"up time semanal del 11 al 17 de agosto",
							"ponderado":97.2,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"Cajeros: Up time cajeros DIEBOLD",
							"porcentaje":95.6,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Up time cajeros DIEBOLD",
							"calculo":"Cantidad de cajeros: 170",
							"comentario":"up time semanal del 11 al 17 de agosto - las fallas de máquina y la baja gestión del proveedor continuan impactando el indicador - se escala con el proveedor y se hace reunión de seguimiento",
							"ponderado":96.3,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Cajeros: Up time Multifuncionales DIEBOLD",
							"porcentaje":95.2,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time Multifuncionales DIEBOLD",
							"calculo":"Cantidad de MF: 55",
							"comentario":"up time semanal del 11 al 17 de agosto",
							"ponderado":94.0,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Efectivo: Cumplimiento Saldo de Caja",
							"porcentaje":99.8,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"2. Yellow",
							"formula":"Total meta  / Total promedio semana (meta  para el 2021:  $660,000,000,000 promd)",
							"calculo":"Saldo promedio: $665.506.462.745",
							"comentario":"Semana 11 al 17 de Agosto 2022",
							"ponderado":98.9,
							"lgreen":100,
							"lyellow":"97",
							"lred":97}),
	"Indicador11": IndicadorInDB(**{"id_indicador": 11,
							"name":"Transferencias Electrónicas. Calidad lotes  aplicados",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Lotes aplicados / Lotes recibidos",
							"calculo":"Lotes aplicados: 36.986                                                             Valor Total $458.012.821.585.51",
							"comentario":"Semana del 12 al 18 de agosto",
							"ponderado":99.4,
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
							"calculo":"Centrales de Canje: 38. 8 Cedec, 17 CUD o delegadas teercerizadas y 13 propias delegadas. Valor Canje Rec.: $89.740.439.364.45 Valor Canje Env.: $66.473.691.779.17",
							"comentario":"Semana del 10 al 16 de agosto",
							"ponderado":100.0,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
	"Indicador9": IndicadorInDB(**{"id_indicador": 9,
							"name":"Oportunidad en la atención de Embargos-Desembargos",
							"porcentaje":98.1,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Atención Requerimientos de Entes Extern",
							"colorin":"3. Green",
							"formula":"Embargos-Desembargos atendidos oportunamente /  Total Embargos-Desembargos radicados *Fuente: Sistema de embargos",
							"calculo":"Identificaciones Capturadas 23.866 Identificaciones Oportunas (1-3 dias)  23.418 Identificaciones Inoportunas (4 ó mas dias ) 420 Identificaciones Pendientes 28",
							"comentario":"Semana del 8 al 14 agosto del 2022",
							"ponderado":96.7,
							"lgreen":96,
							"lyellow":"92",
							"lred":92}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"CSCB: Atención casos escalados por OMAT por correo (En construcción y validación con otras áreas)",
							"porcentaje":97.7,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte a Aplicaciones",
							"colorin":"2. Yellow",
							"formula":"# de casos atendidos / # casos asignados en Service Now Fuente: Notificaciones enviadas por Service Now  y registro de los casos atendidos en el grupo..",
							"calculo":"269 (# casos asignados en Service Now)",
							"comentario":"Semana del 12 al 18 de agosto",
							"ponderado":84.8,
							"lgreen":100,
							"lyellow":"76",
							"lred":76}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"COI: Cumplimiento de operaciones Clientes",
							"porcentaje":91.8,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Coordinación Moneda Extranjera",
							"colorin":"2. Yellow",
							"formula":"Operaciones para tramitar en el exterior/ Operaciones enviadas por oficinas.",
							"calculo":"Op. Recibidas de clientes 305 Op. Cumplidas 280 por valor de USD 4,154,343,55",
							"comentario":"El incumplimiento se debe a inconsisistencias presentadas en las operaciones que no lograron ser corregidas el mismo día en que las solicita el cliente, estas operaciones habitualmente se tramitan al día siguiente de su recepción",
							"ponderado":91.4,
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
							"calculo":"6,174 puntos conciliados  11,360 ajustes aplicados",
							"comentario":"Semana del 12 al 18 de agosto",
							"ponderado":99.2,
							"lgreen":100,
							"lyellow":"90",
							"lred":90}),
	"Indicador10": IndicadorInDB(**{"id_indicador": 10,
							"name":"CC: Partidas pendientes mayores a 30 días",
							"porcentaje":99.7,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Cuadre",
							"colorin":"3. Green",
							"formula":"Partidas conciliatorias mayores a 30 días sin ajustar resultado de la conciliación contable  mensual con corte al mes anterior / total partidas conciliatorias presentadas durante el  mes",
							"calculo":"19 por $ 10,439,449 con corte julio 31/2022",
							"comentario":"Semana del 12 al 18 de agosto",
							"ponderado":98.6,
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
							"calculo":"Solicitudes recibidas y tramitadas: 154 Total clientes atendidos: 154 Total productos activados: 298",
							"comentario":"Semana del 12 al 18 de agosto",
							"ponderado":99.5,
							"lgreen":100,
							"lyellow":"97",
							"lred":97}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"COE: Oportunidad transacciones atendidas en los tiempos definidos ANS",
							"porcentaje":94.4,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Centro Operación Empresarial  - Fiduciario",
							"colorin":"1. Red",
							"formula":"Transacciones cumplidas según ANS / solicitudes radicadas [Fuente: Excel - Inventario de solicitudes]",
							"calculo":"SEMANAL     Q  1,148    $ 415,494 Miles Mll",
							"comentario":"Semana del 12 al 18 de agosto",
							"ponderado":96.9,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador8": IndicadorInDB(**{"id_indicador": 8,
							"name":"CCB: DISPONIBILIDAD Transaccioalidad corresponsales bancarios modelo propio",
							"porcentaje":97.1,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"1 - (Número de transacciones Rechazadas / Número de transacciones Exitosas)",
							"calculo":"=1-(4607/161606)",
							"comentario":"Se detalla los rechazos operacionales de transaccionalidad en el canal, donde el mayor volumen o relevancia no son atribuibles a fallas del canal, sin embargo, se presentaron 113  trx con error inesperado en consulta: TRXW2 W2- FONDOS INSUFICIENTES P",
							"ponderado":99.9,
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
							"comentario":"Información suministrada por el aliado Carvajal a corte al 15  de agosto 2022. La información es generada por assenda red, el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas. No",
							"ponderado":98.3,
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
							"calculo":"Cantidad Operaciones: 574 Cantidad Operaciones cumplidas: 574",
							"comentario":"Semana del 12 al 18 de agosto",
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
