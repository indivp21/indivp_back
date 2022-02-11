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
							"name":"Cajeros: Up time cajeros NCR",
							"porcentaje":96.9,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Up time cajeros NCR",
							"calculo":"Cantidad de cajeros: 453",
							"comentario":"Up time semanal del 03 al 09 de febrero - se han presentado retrasos en al atención oportuna de servicios por parte de los proveedores afectando la disponibilidad de las máquinas - se estima mejoría en la atención de los servicios en la siguiente sem",
							"ponderado":97.1,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Cajeros: Up time cajeros DIEBOLD",
							"porcentaje":96.9,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Up time cajeros DIEBOLD",
							"calculo":"Cantidad de cajeros: 171",
							"comentario":"Up time semanal del 03 al 09 de febrero - se han presentado retrasos en al atención oportuna de servicios por parte de los proveedores afectando la disponibilidad de las máquinas - se estima mejoría en la atención de los servicios en la siguiente sem",
							"ponderado":96.7,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"Cajeros: Up time Multifuncionales DIEBOLD",
							"porcentaje":93.6,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Up time Multifuncionales DIEBOLD",
							"calculo":"Cantidad de MF: 55",
							"comentario":"Up time semanal del 03 al 09 de febrero - se han presentado retrasos en al atención oportuna de servicios por parte de los proveedores afectando la disponibilidad de las máquinas - se estima mejoría en la atención de los servicios en la siguiente sem",
							"ponderado":94.0,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"Efectivo: Cumplimiento Saldo de Caja",
							"porcentaje":95.0,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Total meta  / Total promedio semana (meta  para el 2021:  $590,000,000,000 promd)",
							"calculo":"Saldo promedio: $620.986.812.656.",
							"comentario":"Semana del 03 al 09 Febrero 2022 Impacto en el saldo promedio, por incremento del billete de baja denominacion buen estado, el cual se encuentra restringido para depósito ante el Banco de la República. Se esta realizando gestión para su autorización.",
							"ponderado":98.1,
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
							"calculo":"Lotes aplicados: 35.109                                                                               Valor Total $477.062.461.925.92",
							"comentario":"Semana del 4 al 10 de febrero",
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
							"calculo":"Centrales de Canje: 38. 8 Cedec, 17 CUD o delegadas teercerizadas y 13 propias delegadas. Valor Canje Rec.: $777.546.532.604.51 Valor Canje Env.: $76.218.287.532.82",
							"comentario":"Semana del 03 al 09 Febrero",
							"ponderado":100.0,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
	"Indicador9": IndicadorInDB(**{"id_indicador": 9,
							"name":"Oportunidad en la atención de Embargos-Desembargos",
							"porcentaje":99.8,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Atención Requerimientos de Entes Extern",
							"colorin":"3. Green",
							"formula":"Embargos-Desembargos atendidos oportunamente /  Total Embargos-Desembargos radicados *Fuente: Sistema de embargos",
							"calculo":"Identificaciones Capturadas 19.211 Identificaciones Oportunas (1-3 dias) 19.181 Identificaciones Inoportunas (4 ó mas dias ) 14 Identificaciones Pendientes 16",
							"comentario":"Semana del 31 de Enero al 6 de Febrero del 2022",
							"ponderado":96.7,
							"lgreen":98,
							"lyellow":"92",
							"lred":92}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"CSCB: Atención casos escalados por OMAT por correo (En construcción y validación con otras áreas)",
							"porcentaje":78.8,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte a Aplicaciones",
							"colorin":"2. Yellow",
							"formula":"# de casos atendidos / # casos escalados por OMAT por correo Fuente: Correos enviados por OMAT y registro de los casos atendidos en el grupo.",
							"calculo":"260 (# casos escalados por OMAT por correo)",
							"comentario":"Semana del 04  al 10 de febrero",
							"ponderado":81.9,
							"lgreen":100,
							"lyellow":"76",
							"lred":76}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"COI: Cumplimiento de operaciones Clientes",
							"porcentaje":89.0,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Coordinación Moneda Extranjera",
							"colorin":"1. Red",
							"formula":"Operaciones para tramitar en el exterior/ Operaciones enviadas por oficinas.",
							"calculo":"Op. Recibidas de clientes 385 Op. Cumplidas 343 por valor de USD 4,915,113,57",
							"comentario":"El incumplimiento se debe a inconsisistencias presentadas en las operaciones que no lograron ser corregidas el mismo día en que las solicita el cliente, estas operaciones habitualmente se tramitan al día siguiente de su recepción",
							"ponderado":90.7,
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
							"calculo":"6,694 puntos conciliados  4,292 ajustes aplicados",
							"comentario":"Semana del 04  al 10 de febrero",
							"ponderado":99.3,
							"lgreen":100,
							"lyellow":"90",
							"lred":90}),
	"Indicador10": IndicadorInDB(**{"id_indicador": 10,
							"name":"CC: Partidas pendientes mayores a 30 días",
							"porcentaje":99.6,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Cuadre",
							"colorin":"3. Green",
							"formula":"Partidas conciliatorias mayores a 30 días sin ajustar resultado de la conciliación contable  mensual con corte al mes anterior / total partidas conciliatorias presentadas durante el  mes",
							"calculo":"31 por $ 24,614,661,46  corte diciembre 31/2021",
							"comentario":"Semana del 04  al 10 de febrero",
							"ponderado":99.2,
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
							"calculo":"153 Clientes 302 Productos",
							"comentario":"Semana del 04 al 10 de febrero de 2022",
							"ponderado":99.8,
							"lgreen":100,
							"lyellow":"97.9",
							"lred":97.9}),
	"Indicador8": IndicadorInDB(**{"id_indicador": 8,
							"name":"COE: Oportunidad transacciones atendidas en los tiempos definidos ANS",
							"porcentaje":98.8,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Centro Operación Empresarial  - Fiduciario",
							"colorin":"3. Green",
							"formula":"Transacciones cumplidas según ANS / solicitudes radicadas [Fuente: Excel - Inventario de solicitudes]",
							"calculo":"Semanal  Q 1324 $  586,929  Mil Millones",
							"comentario":"Semana del 04 al 10 de febrero de 2022",
							"ponderado":97.6,
							"lgreen":95,
							"lyellow":"90",
							"lred":90}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"CCB: Oportunidad en la disponibilidad del Canal Modelo Propio",
							"porcentaje":96.3,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"1 - (Número de transacciones Rechazadas / Número de transacciones Exitosas)",
							"calculo":"=1-(5571/158320)",
							"comentario":"Durante la semana se presentaron los siguientes rechazos con mayor relevancia: 1.750 trx fondos insuficientes para retiro con un 41,57%.",
							"ponderado":100.5,
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
							"calculo":"Sin informacion",
							"comentario":"Información suministrada por el aliado Carvajal a corte quincenal enero 2022 La información es generada por assenda red, el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas. No pr",
							"ponderado":98.2,
							"lgreen":98,
							"lyellow":"97",
							"lred":97}),
	"Indicador16": IndicadorInDB(**{"id_indicador": 16,
							"name":"BO: Oportunidad en el cumplimiento de operaciones del Piso Financiero y otras Áreas de las empresas",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "UAC Back Office",
							"colorin":"3. Green",
							"formula":"Número total operaciones cumplidas/ operaciones a cumplir.",
							"calculo":"Se atendieron 774 operaciones por un valor total de $ 5.290.886.319.677.15",
							"comentario":"Semana del 4 al 10 de febrero de 2022",
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
