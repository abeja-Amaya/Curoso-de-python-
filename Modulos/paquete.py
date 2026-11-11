#
#
# dato : para que sea considerado un paquete tiene que tener un archivo __init__.py, si no compildor de VS no lo reconoce como paquete. 
#
# asi se llama un paquete, q tiene varios modulos que podemos utilizar.
import paquete.suma_archivo    
import paquete.resta_archivo   
# llamamos a la funcion dentro del modulo suma_archivo:
print(paquete.suma_archivo.suma(10, 11)) # se llama al paquete -- > modulo --> funcioon


print(paquete.resta_archivo.resta(100, 31))