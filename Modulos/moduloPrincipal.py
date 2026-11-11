
#nameSpace = modulo
#import llamamos al nameSpace del modulo
#import * llama a todas las fuciones dentro de un nameSpace
#utilizamos from para traer solo los metodos que queramos del nameSpace y no todo
# as sirve para renombrar a un nombre mas corto cuando el nombre de la funcon es mas largo. y tambien por nomenclatura esta copado la vrd
#----------------------------
#import sys
#-------------------------------
import nombre as name
import contraseña as password    # llama a todo el nameSpace con todos sus funciones.
from comp_datos import datos_uni # solo llama a una unica funcion y no a todos.
from comp_datos import Metas_for_ciclo as Metas, good_news as News # tambien se puede llamar a mas de una funcion.

nuevo = name.write_name(10, "Amaya")
nuevo = password.new_password(10, "deciGA", 2)

nuevo = datos_uni("UPN", "Ingieneria de Software", 4)

nuevo = Metas("Work for BCP", "Terminar la UNI siendo un verdadero Profesional", "Casarme con Cielo")

nuevo = News("Only 1.30 forerminar el curso de python con DALTO")