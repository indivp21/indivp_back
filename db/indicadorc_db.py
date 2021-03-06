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
	"Indicador11": IndicadorInDB(**{"id_indicador": 11,
							"name":"Negociaciones aplicadas oportunamente",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación de Operaciones e Información de Exóge",
							"colorin":"3. Green",
							"formula":"(Negociaciones devueltas + Negociaciones aplicadas)/Número total de negociaciones",
							"calculo":"(24+288)/312",
							"comentario":"Sin informacion",
							"ponderado":87.6,
							"lgreen":98,
							"lyellow":"95",
							"lred":95}),
	"Indicador12": IndicadorInDB(**{"id_indicador": 12,
							"name":"Atención oportuna de reclamos",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación de Operaciones e Información de Exóge",
							"colorin":"3. Green",
							"formula":"Reclamos atendidos oportunamente * 1 / Total de reclamos a solucionar",
							"calculo":"65*1/65",
							"comentario":"Sin informacion",
							"ponderado":99.8,
							"lgreen":98,
							"lyellow":"95",
							"lred":95}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Atención oportuna de PQR",
							"porcentaje":99.3,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación de Operaciones e Información de Exóge",
							"colorin":"3. Green",
							"formula":"Requerimientos atendidos oportunamente * 1 / Total de requerimientos a solucionar",
							"calculo":"2770*1/2788",
							"comentario":"Indicador mensual transmitido por la Gerencia de calidad de Servicio (Resultado corresponde a cierre Marzo)",
							"ponderado":99.3,
							"lgreen":98,
							"lyellow":"99",
							"lred":99}),
	"Indicador13": IndicadorInDB(**{"id_indicador": 13,
							"name":"Entrega de reportes (SIF) a tiempo",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación de Operaciones e Información de Exóge",
							"colorin":"3. Green",
							"formula":"Informes entes externos en el tiempo / Total Informes entes externos",
							"calculo":"3/3",
							"comentario":"Sin informacion",
							"ponderado":100.0,
							"lgreen":98,
							"lyellow":"95",
							"lred":95}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"Devolución de Acreedores",
							"porcentaje":9.0,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación de Operaciones e Información de Exóge",
							"colorin":"1. Red",
							"formula":"(Reintegros [constituidos mes] + reintegros [constituidos meses anteriores]) / ( Reintegros [constituidos mes] + Pendientes [constituidos mes)",
							"calculo":"(50+80)/(50+1385)",
							"comentario":"Acreedores mensuales que se generan posterior a la aplicación de pagos, se aplican reintegros a los titulares con cuentas del Banco o externas, o a través de oficinas por excedente disponible durante el mes, se monitorea el total generado versus lo r",
							"ponderado":74.2,
							"lgreen":90,
							"lyellow":"95",
							"lred":95}),
	"Indicador14": IndicadorInDB(**{"id_indicador": 14,
							"name":"Operaciones de Libranzas Giradas ofc 350",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación de Operaciones e Información de Exóge",
							"colorin":"3. Green",
							"formula":"(Compras de cartera + Abonos a cuenta) / Total Operaciones Giradas",
							"calculo":"(18+2)/30",
							"comentario":"Sin informacion",
							"ponderado":99.8,
							"lgreen":98,
							"lyellow":"95",
							"lred":95}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Trámite y aplicación oportuna de Cartas de Compromiso radicadas",
							"porcentaje":99.6,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Operativa Constructor",
							"colorin":"3. Green",
							"formula":"Aplicaciones automaticas / (aplicaciones automaticas + aplicaciones manuales)",
							"calculo":"16432/(16432+52)",
							"comentario":"Indicador se registra una vez al mes, las aplicaciones se realizan antes del vencimiento de los convenios",
							"ponderado":99.9,
							"lgreen":98,
							"lyellow":"97",
							"lred":97}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"Trámite oportuno en liberación parcial de hipoteca en mayor extensión",
							"porcentaje":96.7,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Operativa Constructor",
							"colorin":"3. Green",
							"formula":"Descuentos rechazados primera vez / Descuentos reportados primera vez",
							"calculo":"3291/(112+3291)",
							"comentario":"El indicador es mensual: Descuentos no girados por las pagadurías al reportarlos por primera vez por causales: Sin capacidad de descuento, error operativo y de plataformas y novedades sin identificar que se continuan reportando de acuerdo a las fecha",
							"ponderado":99.3,
							"lgreen":95,
							"lyellow":"97",
							"lred":97}),
	"Indicador15": IndicadorInDB(**{"id_indicador": 15,
							"name":"Oportunidad en la atención de desembolsos",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Operativa Constructor",
							"colorin":"3. Green",
							"formula":"Cartas de compromiso gestionadas / (Cartas de compromiso tramitadas + Cartas de compromiso devueltas)",
							"calculo":"44 / ( 44 +0 )",
							"comentario":"Indicadores con corte al jueves 05 de mayo, en razón a que el cierre del sistema se realiza el viernes al finalizar la operación, por lo tanto no es posible obtener informción al corte del viernes",
							"ponderado":99.6,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador16": IndicadorInDB(**{"id_indicador": 16,
							"name":"Oportunidad en la atención de pagos",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Operativa Constructor",
							"colorin":"3. Green",
							"formula":"Liberaciones parciales de hipoteca gestionadas / (Liberaciones parciales tramitadas + Liberaciones parciales devueltas)",
							"calculo":"298 / (255 + 43 )",
							"comentario":"Indicadores con corte al jueves 05 de mayo, en razón a que el cierre del sistema se realiza el viernes al finalizar la operación, por lo tanto no es posible obtener informción al corte del viernes",
							"ponderado":100.0,
							"lgreen":98,
							"lyellow":"N/A",
							"lred":98}),
	"Indicador17": IndicadorInDB(**{"id_indicador": 17,
							"name":"Oportunidad en la atención de subrogaciones",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Operativa Constructor",
							"colorin":"3. Green",
							"formula":"Desembolsos atendidos oportunamente * 1 / Desembolsos pendientes de trámite",
							"calculo":"8*1 / 0",
							"comentario":"Indicadores con corte al jueves 05 de mayo, en razón a que el cierre del sistema se realiza el viernes al finalizar la operación, por lo tanto no es posible obtener informción al corte del viernes",
							"ponderado":99.8,
							"lgreen":100,
							"lyellow":"98",
							"lred":98}),
	"Indicador18": IndicadorInDB(**{"id_indicador": 18,
							"name":"Partidas pendientes de pagos por aplicar con fecha efectiva",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Operativa Constructor",
							"colorin":"3. Green",
							"formula":"Pagos atendidos oportunamente * 1 / Pagos pendientes de trámite",
							"calculo":"141*1 / 0",
							"comentario":"Indicadores con corte al jueves 05 de mayo, en razón a que el cierre del sistema se realiza el viernes al finalizar la operación, por lo tanto no es posible obtener informción al corte del viernes",
							"ponderado":99.0,
							"lgreen":100,
							"lyellow":"97",
							"lred":97}),
	"Indicador19": IndicadorInDB(**{"id_indicador": 19,
							"name":"Trámite de ajustes valor de intereses",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Operativa Constructor",
							"colorin":"3. Green",
							"formula":"Subrogaciones gestionadas / (Subrogaciones tramitadas + subrogaciones detenidas)",
							"calculo":"107 / (68 + 39)",
							"comentario":"Indicadores con corte al jueves 05 de mayo, en razón a que el cierre del sistema se realiza el viernes al finalizar la operación, por lo tanto no es posible obtener informción al corte del viernes",
							"ponderado":83.7,
							"lgreen":98,
							"lyellow":"95",
							"lred":95}),
	"Indicador20": IndicadorInDB(**{"id_indicador": 20,
							"name":"Oportunidad en el giro diario del recaudo,las interfaces del recaudo y envío y recepción de cuentas",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Cartera Administradas",
							"colorin":"3. Green",
							"formula":"Ajustes realizados * 1 / Ajustes pendientes",
							"calculo":"2*1 / 0",
							"comentario":"Indicadores con corte al jueves 05 de mayo, en razón a que el cierre del sistema se realiza el viernes al finalizar la operación, por lo tanto no es posible obtener informción al corte del viernes",
							"ponderado":100.0,
							"lgreen":98,
							"lyellow":"80",
							"lred":80}),
	"Indicador21": IndicadorInDB(**{"id_indicador": 21,
							"name":"Cumplimiento en la atención de solicitudes de Recursos a Bancoldex",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Cartera Administradas",
							"colorin":"3. Green",
							"formula":"Ajustes realizados * 1 / Ajustes pendientes",
							"calculo":"6*1 / 0",
							"comentario":"Indicadores con corte al jueves 05 de mayo, en razón a que el cierre del sistema se realiza el viernes al finalizar la operación, por lo tanto no es posible obtener informción al corte del viernes",
							"ponderado":100.0,
							"lgreen":98,
							"lyellow":"90",
							"lred":90}),
	"Indicador22": IndicadorInDB(**{"id_indicador": 22,
							"name":"Cumplimiento en el registro semanal de garantías ante el FNG y en el pago de facturas de comisiones",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Cartera Administradas",
							"colorin":"3. Green",
							"formula":"Promedio (Días con incumplimiento/días hábilies del mes), (Cuentas de cobro pagadas oportunamente por TC  /  Ttal cuentas de cobro generadas por BCS a la TC)",
							"calculo":"1*Promedio (5/5), (2/2)",
							"comentario":"Una parte del indicador tiene componente mensual que se mantiene con la información de la semana anterior",
							"ponderado":100.0,
							"lgreen":95,
							"lyellow":"90",
							"lred":90}),
	"Indicador23": IndicadorInDB(**{"id_indicador": 23,
							"name":"Efectividad en cargue y creación de operaciones compradas",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Cartera Administradas",
							"colorin":"3. Green",
							"formula":"Días con incumplimiento / días hábilies del mes en que se solicitaron recursos",
							"calculo":"1*(5/5)",
							"comentario":"Sin informacion",
							"ponderado":96.5,
							"lgreen":100,
							"lyellow":"90",
							"lred":90}),
	"Indicador24": IndicadorInDB(**{"id_indicador": 24,
							"name":"Monitoreo al portafolio disponible para ATL",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Cartera Administradas",
							"colorin":"3. Green",
							"formula":"No de eventos confirmados oportunamente  /  No de eventos presentados en el mes",
							"calculo":"1*Promedio(7/7),(83/83)",
							"comentario":"Sin informacion",
							"ponderado":99.9,
							"lgreen":100,
							"lyellow":"99.3",
							"lred":99.3}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"Oportunidad en el traslado de recaudos a la PIC",
							"porcentaje":93.4,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Cartera Administradas",
							"colorin":"2. Yellow",
							"formula":"No de obligaciones compradas y cargadas oportunamente  /  No total de obligaciones compradas",
							"calculo":"1*(1286/1376)",
							"comentario":"Para la compra de cartera del 05 de mayo a Refinancia Satr Clientes generó rechazo para la creación 90 clientes; el cargue se encuentra en reproceso.",
							"ponderado":98.6,
							"lgreen":95,
							"lyellow":"90",
							"lred":90}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"Oportunidad en la transmisión de reportes de registro y cuentas de cobro de la cartera FRECH al Banc",
							"porcentaje":99.8,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Cartera Administradas",
							"colorin":"3. Green",
							"formula":"1- el porcentaje de variación del día de la semana que mas variación se haya presentado",
							"calculo":"1 - 0.11%",
							"comentario":"Sin informacion",
							"ponderado":99.9,
							"lgreen":99.5,
							"lyellow":"90",
							"lred":90}),
	"Indicador25": IndicadorInDB(**{"id_indicador": 25,
							"name":"Atención oportuna y completa de requerimientos por Custodios",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Central de Garantías",
							"colorin":"3. Green",
							"formula":"Días con incumplimiento en el traslado del recaudo/días con recaudo en el mes",
							"calculo":"1*(7/7)",
							"comentario":"Sin informacion",
							"ponderado":100.0,
							"lgreen":95,
							"lyellow":"98",
							"lred":98}),
	"Indicador26": IndicadorInDB(**{"id_indicador": 26,
							"name":"Oportunidad trámite de Cancelación Hipotecas",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Central de Garantías",
							"colorin":"3. Green",
							"formula":"Un registro o cuenta de cobro que no se transmita oportunamente o con inconsistencia 95% Dos registros o cuentas de cobro que no se transmitan oportunamente o con inconsistencia 90% Tres registros o cuenta de cobro que no se transmita oportunamente o",
							"calculo":"0 registros inoportunos =100%",
							"comentario":"Indicador mensual se mantiene la información de la semana anterior",
							"ponderado":99.4,
							"lgreen":100,
							"lyellow":"98",
							"lred":98}),
	"Indicador8": IndicadorInDB(**{"id_indicador": 8,
							"name":"Efectividad en la atenció de garantías para  alistamiento proceso jurídico",
							"porcentaje":99,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Central de Garantías",
							"colorin":"3. Green",
							"formula":"total garantías recibidas,correctas y atendidas a tiempo / total garantias entregadas y solicitadas",
							"calculo":"0",
							"comentario":"El Indicador mensual  con corte Abril Resultado  es el promedio del año  2022",
							"ponderado":99.8,
							"lgreen":99,
							"lyellow":"98",
							"lred":98}),
	"Indicador10": IndicadorInDB(**{"id_indicador": 10,
							"name":"Atención oportuna PQR,s",
							"porcentaje":99,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Central de Garantías",
							"colorin":"3. Green",
							"formula":"(total  casos atendidos de 1 a 6 días/ Total casos radicados)+ ( total casos con inconsistencia/ total casos radicados)/2",
							"calculo":"(396/396)+(0/396) Notaria  62  (391/391)+(16/391) Notaria  51",
							"comentario":"El Indicador mensual  con corte Abril Resultado  es el promedio del año  2023",
							"ponderado":99.8,
							"lgreen":99,
							"lyellow":"98",
							"lred":98}),
	"Indicador27": IndicadorInDB(**{"id_indicador": 27,
							"name":"Conciliación de inventario de polizas Vida e IRT",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Central de Garantías",
							"colorin":"3. Green",
							"formula":"total garantías recibidas,correctas y a tiempo / total garantias solicitadas",
							"calculo":"237/237",
							"comentario":"El Indicador es mensual con corte  Abril Resultado es el promedio del año 2022",
							"ponderado":99.4,
							"lgreen":99,
							"lyellow":"98",
							"lred":98}),
	"Indicador28": IndicadorInDB(**{"id_indicador": 28,
							"name":"Partidas con antigüedad Menor ó igual a 30 días.",
							"porcentaje":100,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación de Cuadre",
							"colorin":"3. Green",
							"formula":"Requerimientos atendidos oportunamente * 1 / Total de requerimientos a solucionar",
							"calculo":"763*2/765",
							"comentario":"Indicador mensual transmitido por la Gerencia de calidad de Servicio  con corte Marzo Resultado es el promedio del año 2022",
							"ponderado":60.9,
							"lgreen":99,
							"lyellow":"80",
							"lred":80}),
	"Indicador10": IndicadorInDB(**{"id_indicador": 10,
							"name":"Atención oportuna PQR,s",
							"porcentaje":99,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Central de Garantías",
							"colorin":"3. Green",
							"formula":"total de polizas sin novedad/ total de polizas vigentes colmena seguros total de polizas sin novedad/ total  de polizas vigentes Liberty seguros",
							"calculo":"(593.827/593.917 ) Colmena Deudores (158,256/158,262) Liberty",
							"comentario":"Indicador  de oportunidad y calidad   a Marzo de 2022 Resultado es el promedio de lo corrido del  año",
							"ponderado":99.2,
							"lgreen":99,
							"lyellow":"98",
							"lred":98}),
	"Indicador27": IndicadorInDB(**{"id_indicador": 27,
							"name":"Conciliación de inventario de polizas Vida e IRT",
							"porcentaje":34,
							"gerencia":"Gerencia Cartera Operativa",
							"central": "Coordinación Central de Garantías",
							"colorin":"1. Red",
							"formula":"Total Partidas menores  o igual a 30 días / Total Partidas Pendientes",
							"calculo":"8.071/24.069",
							"comentario":"Informe con corte Abril 29  de 2022,  Actualmente el area se encuentra trabajando un plan de Acción  en proceso de depuración de las partidas antiguas, producto de la implementación de estrategias para atender Emergencia Sanitaria y negociaciones de",
							"ponderado":86.2,
							"lgreen":90,
							"lyellow":"98",
							"lred":98}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None
