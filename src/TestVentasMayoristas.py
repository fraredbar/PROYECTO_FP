from ventasMayoristas import *

def mostrar_numerado(datos):
       i=0
       for p in datos:
              i=i+1
              print(i,p)

def main():

 datos= lee_datos_ventasMayoristas('data/ventas_mayorista.csv')
 print("Se han cargado", len(datos),"registros.")
 
 #LECTURA DE LOS 3 PRIMEROS.
 print("Mostrando los 3 primeros:")
 for r in datos[:3]: #Slising obteniendo un trozo de la linea.(En este caso los 3 primeros), si no ponemos el corchete recorre todos los datos.
        print("\t", r)

 #LECTURA DE LOS 3 ÚLTIMOS.
 print("Mostrando los 3 ultimos:")
 for r in datos[-3:]: #Slising obteniendo un trozo de la linea.(En este caso los 3 ultimos), si no ponemos el corchete recorre todos los datos.
        print("\t", r)
 #print(mostrar_numerado(Datos_ventas_mayorista)) 
 
        
if __name__=='__main__':
     main()