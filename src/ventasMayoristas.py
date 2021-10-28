from datetime import datetime
import csv
from collections import namedtuple

Datos_ventas_mayorista = namedtuple('Datos_ventas_mayorista', 'medio_pedido,tipo_tienda,tipo_producto,producto,fecha_compra,uds_vendidas,pvp_unidad,margen_ganancia,libre_impuestos')

def lee_datos_ventasMayoristas(fichero):

    registros = []
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        for medio_pedido,tipo_tienda,tipo_producto,producto,fecha_compra,uds_vendidas,pvp_unidad,margen_ganancia,libre_impuestos in lector:

            medio_pedido=   str(medio_pedido)
            tipo_tienda=    str(tipo_tienda)
            tipo_producto=  str(tipo_producto)
            producto=   str(producto) 
            fecha_compra=   datetime.strptime(fecha_compra,"%d/%m/%Y").date()
            uds_vendidas=   int(uds_vendidas)
            pvp_unidad=     float(pvp_unidad)
            margen_ganancia=    float(margen_ganancia)
            libre_impuestos=    parse_bool(libre_impuestos)

            tuplaVentas= Datos_ventas_mayorista(medio_pedido,tipo_tienda,tipo_producto,producto,fecha_compra,uds_vendidas,pvp_unidad,margen_ganancia,libre_impuestos)
            registros.append(tuplaVentas)
    return registros

#----------------------------------------------------------------------------------
def parse_bool(fecha_compra):
        if fecha_compra == 'true':
            booleano = True
        else: 
            booleano = False
        return booleano

#----------------------------------------------------------------------------------
