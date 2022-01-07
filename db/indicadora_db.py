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
							"porcentaje":97.1,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time cajeros NCR",
							"calculo":"Cantidad de cajeros: 453",
							"comentario":"Up time semanal del 30 de diciembre al 05 de enero",
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
							"calculo":"Cantidad de cajeros: 171",
							"comentario":"Up time semanal del 30 de diciembre al 05 de enero - proveedor Diebold con baja capacidad de respuesta en los servicios en la primera semana del mes - se escala al proveedor para  mayor oportunidad de respuesta",
							"ponderado":96.7,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"Cajeros: Up time Multifuncionales DIEBOLD",
							"porcentaje":93.5,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Up time Multifuncionales DIEBOLD",
							"calculo":"Cantidad de MF: 55",
							"comentario":"Up time semanal del 30 de diciembre al 05 de enero - proveedor Diebold con baja capacidad de respuesta en los servicios en la primera semana del mes - se escala al proveedor para  mayor oportunidad de respuesta",
							"ponderado":94.0,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Efectivo: Cumplimiento Saldo de Caja",
							"porcentaje":97.6,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"2. Yellow",
							"formula":"Total meta  / Total promedio semana (meta  para el 2021:  $590,000,000,000 promd)",
							"calculo":"Saldo promedio: $725.149.448.438. Por temporada se maneja un saldo de $708.000.000.000",
							"comentario":"Semana del 30 Diciembre 2021 - 05 Enero 2022",
							"ponderado":98.5,
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
							"calculo":"Lotes aplicados: 39.362                                                                               Valor Total $564,050,981,667.66",
							"comentario":"Semana del 30 de diciembre al 6 de enero.",
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
							"calculo":"Centrales de Canje: 38. 8 Cedec, 17 CUD o delegadas teercerizadas y 13 propias delegadas. Valor Canje Rec.: $63.529.695.999.40 Valor Canje Env.: $77.393.397.200.01",
							"comentario":"Semana del 30 diciembre al 05 de Enero",
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
							"calculo":"Identificaciones Capturadas 10.445 Identificaciones Oportunas (1-3 dias) 10.427 Identificaciones Inoportunas (4 ó mas dias ) 10 Identificaciones Pendientes 8",
							"comentario":"Semana: 27 diciembre 2021 - 2 enero 2022",
							"ponderado":96.5,
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
							"calculo":"258 (# casos escalados por OMAT por correo)",
							"comentario":"Semana del 30 diciembre al 06 de Enero",
							"ponderado":81.7,
							"lgreen":100,
							"lyellow":"76",
							"lred":76}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"COI: Cumplimiento de operaciones Clientes",
							"porcentaje":91.7,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Coordinación Moneda Extranjera",
							"colorin":"2. Yellow",
							"formula":"Operaciones para tramitar en el exterior/ Operaciones enviadas por oficinas.",
							"calculo":"Op. Recibidas de clientes 243 Op. Cumplidas 223 por valor de USD 1,964,046.53",
							"comentario":"Semana del 1 de enero al 06 de enero",
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
							"calculo":"6,694 puntios conciliados 7,788 ajustes aplicados",
							"comentario":"Semana del 30 diciembre al 06 de Enero",
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
							"calculo":"31 por $ 24,614,661,46 corte noviembre 30/2021",
							"comentario":"Semana del 30 diciembre al 06 de Enero",
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
							"calculo":"106 Clientes",
							"comentario":"Semana del 30 diciembre al 06 de Enero",
							"ponderado":99.8,
							"lgreen":100,
							"lyellow":"97.9",
							"lred":97.9}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"COE: Oportunidad transacciones atendidas en los tiempos definidos ANS",
							"porcentaje":94.0,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Centro Operación Empresarial  - Fiduciario",
							"colorin":"2. Yellow",
							"formula":"Transacciones cumplidas según ANS / solicitudes radicadas [Fuente: Excel - Inventario de solicitudes]",
							"calculo":"Semanal  Q 896  $ 159.400 Mil Millones",
							"comentario":"Semana del 30 diciembre 2021 al 06 de enero 2022",
							"ponderado":97.6,
							"lgreen":95,
							"lyellow":"90",
							"lred":90}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"CCB: Oportunidad en la disponibilidad del Canal Modelo Propio",
							"porcentaje":96.4,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"1 - (Número de transacciones Rechazadas / Número de transacciones Exitosas)",
							"calculo":"=1-(5571/158320)",
							"comentario":"Durante la semana se presentaron los siguientes rechazos con mayor relevancia:  Fondos insuficientes para retiro 49%, cuenta es cuenta recaudadora con el 4,23%, error inesperado en la consulta 4%",
							"ponderado":100.8,
							"lgreen":95,
							"lyellow":"93",
							"lred":93}),
	"Indicador15": IndicadorInDB(**{"id_indicador": 15,
							"name":"CCB: DISPONIBILIDAD Disponibilidad tráfico de comunicación",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "CCB: DISPONIBILIDAD Disponibilidad tráfico de comu",
							"colorin":"3. Green",
							"formula":"Comunicación",
							"calculo":"Sin Informacion",
							"comentario":"Durante la semana no presento novedad o fallo en comunicación.  Indicador proporcionado por Movistar Empresas, tipo de indicador es por enlace de nivel one, que emite comunicación al rauter. Cuentan con dos reguladores en caso de falla en un rauter p",
							"ponderado":99.7,
							"lgreen":99.6,
							"lyellow":"98",
							"lred":98}),
	"Indicador16": IndicadorInDB(**{"id_indicador": 16,
							"name":"CCB: Oportunidad en la disponibilidad del Canal Carvajal",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"La información es generada por el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas.",
							"calculo":"Sin Informacion",
							"comentario":"Información suministrada por el aliado Carvajal cierre Diciembre La información es generada por assenda red, el monitoreo realizado en el mes sobre la VPN, la plataforma transaccional, ventanas programadas y incidencias presentadas. No presentó afect",
							"ponderado":98.0,
							"lgreen":98,
							"lyellow":"97",
							"lred":97}),
	"Indicador17": IndicadorInDB(**{"id_indicador": 17,
							"name":"BO: Oportunidad en el cumplimiento de operaciones del Piso Financiero y otras Áreas de las empresas",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "UAC Back Office",
							"colorin":"3. Green",
							"formula":"Número total operaciones cumplidas/ operaciones a cumplir.",
							"calculo":"Se atendieron 492 operaciones por un valor total de $6.893.363.019.334.54",
							"comentario":"Sin Informacion",
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
