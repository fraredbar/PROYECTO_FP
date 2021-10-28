ESTRUCTURA DE LAS CARPETAS DEL PROYECTO:

/src: Contiene los diferentes modulos de Python que conforman el proyecto.
    -ventasMayoristas.py : Contiene funciones para usar los datos de ventas mayoristas.
    - TestVentasMayoristas.py : Contiene funciones de test para probar las funciones del módulo ventasMayoristas.py .
/data:Contiene el dataset del proyecto.
    - ventas_mayorista.csv: Archivo con datos de b¡ventas mayoristas que vamos a usar.

ESTRUCTURA DEL DATASET:
-El dataset está compuesto por 9 columnas,cada columna corresponde con un dato, por lo tanto son 9 datos aquellos que nos aportan información acerca de las ventas mayoristas .
    -medio_pedido:tipo str, indica el medio por el que se realizó el pedido.
    -tipo_tienda: tipo str, indica el tipo de tienda en la que se realizó el pedido
    -tipo_producto: tipo str, indica el tipo producto comprado.
    -producto:tipo str, indica el producto comprado.
    -fecha_compra: tipo date, indica la fecha en la que se realizó la compra.
    -uds_vendidas:tipo int, indica el numero de unidades vendidas.
    -pvp_unidad:tipo float, indica el precio de cada unidad. 
    -margen_ganancia:tipo float, indica el margen de ganancia.
    -libre_impuestos: tipo boolean, indica si tiene impestos o no.

TIPOS IMPLEMENTADOS:
- Hemos implementado la siguiente tupla con nombre: Datos_ventas_mayorista = namedtuple('Datos_ventas_mayorista', 'medio_pedido,tipo_tienda,tipo_producto,producto,fecha_compra,uds_vendidas,pvp_unidad,margen_ganancia,libre_impuestos').
en la que los tipos de cada campo son los siguientes:
Datos_ventas_mayorista(str,str,str,str,date,int,float,float,boolean)

FUNCIONES IMPLEMENTADAS:
-MODULO ventasMayoristas:
  ENTREGA 1
     -Bloque 0:
           -lee_datos_ventasMayoristas(fichero):lee los datos del fichero csv y devuelve una lista de tuplas de tipo Datos_ventas_mayorista con los datos del fichero. Para implementar esta función se han definido las siguientes funciones auxiliares:
            parse_bool(libre_impuestos): Función para convertir de cadena a booleano.
-MODULO TestVentasMayoristas:
    En el modulo de pruebas se han definido las siguientes funciones de prueba, para probar la funcion :
        -main()