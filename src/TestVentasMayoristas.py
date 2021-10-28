from ventasMayoristas import *


def main():

 datos= lee_datos_ventasMayoristas('data/ventas_mayorista.csv')
 print("Se han cargado", len(datos),"registros.")
 print("Mostrando los 3 primeros:")
 for r in datos[:3]: #Slising obteniendo un trozo de la linea.(En este caso los 3 primeros), si no ponemos el corchete recorre todos los datos.
        print("\t", r)
        
if __name__=='__main__':
     main()