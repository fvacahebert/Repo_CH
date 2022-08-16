#La idea de estos argumentos es que sean usados dentro de un Script (Archivo) y no dentro de una funcion
#P para eso se importa la libreria SYS
import sys

#print(sys.argv) #Cuando haga la impresion sys.argv en el primer lugar siempre va a traer 
#dentro de una lista el nombre del archivo, es por eso que vamos a empezar a tomar desde la segunda posicion
#SYS.ARGV no hace mas que guardar todos los parametros que le pase en una lista


# El sys tendra 2 argumentos Palabra y Cantidad
if len (sys.argv)==3:
    palabra = sys.argv[1]
    cantidad = int(sys.argv[2])

    for i in range(cantidad):
        print(palabra)
else:
    print("Ingrese 2 argumentos")



