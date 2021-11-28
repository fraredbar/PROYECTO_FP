from ventasMayoristas import *

def mostrar_numerado(datos):
       i=0
       for p in datos:
              i=i+1
              print(i,p)

 
datos= lee_datos_ventasMayoristas('data/ventas_mayorista.csv')
        

def test_leer_ventas():

 #LECTURA DE LOS 3 PRIMEROS.
 print("Mostrando los 3 primeros:")
 for r in datos[:3]: #Slising obteniendo un trozo de la linea.(En este caso los 3 primeros), si no ponemos el corchete recorre todos los datos.
        print('\n',r,'\n')

 #LECTURA DE LOS 3 ÚLTIMOS.
 print("Mostrando los 3 ultimos:")
 for r in datos[-3:]: #Slising obteniendo un trozo de la linea.(En este caso los 3 ultimos), si no ponemos el corchete recorre todos los datos.
        print('\n',r,'\n')
 print(Datos_ventas_mayorista)

#BLOQUE 1´

def filtrar_por_mediopedido_test(medio_pedido):
      listuki= filtrar_por_mediopedido(datos,medio_pedido)
      for d in listuki:
             print('\n',d,'\n')


def calcular_margen_ganancia_medio_test(total):
       print('La ganancia media libre de impuestos es:')
       media= sum(total)/len(total)
       print('%.5f' %media)




#BLOQUE 2

def producto_mas_barato_test(productos_con_precio):
       minimo= min(productos_con_precio)
       print('El producto mas barato es',minimo[0],'y cuesta',minimo[1])
       print('La tupla que busca el enunciado es', minimo)

def productos_mas_vendidos_test(filtro):
       print('Hay',len(filtro), 'productos con mas de 3000 uds vendidas')
       print('Las 10 más vendidas son:')
       print(mostrar_numerado(sorted(filtro[:10],reverse=True, key=lambda p:p[1])))

def compras_por_web_con_mas_unidades_vendidas_test(datos):
       compras_por_web= compras_por_web_con_mas_unidades_vendidas(datos,'Web')
       print('Compras por medio del pedido Web:',sorted(compras_por_web,reverse=True))
        
def agrupa_por_uds_vendidas_test(dicc):
       print(dicc)



###########################################################################
##BLOQUE 1

filtrar_por_mediopedido_test('Fax')
calcular_margen_ganancia_medio_test(total= calcular_margen_ganancia_medio(datos))

#BLOQUE 2

producto_mas_barato_test(productos_con_precio=producto_mas_barato(datos))
productos_mas_vendidos_test(filtro=producto_mas_vendido(datos))
compras_por_web_con_mas_unidades_vendidas_test(datos)
agrupa_por_uds_vendidas_test(dicc=agrupa_por_uds_vendidas(datos))
compras_por_web_con_mas_unidades_vendidas_test(datos)


