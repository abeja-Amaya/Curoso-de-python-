# -------------------------------
# Métodos de las tuplas en Python
# -------------------------------

#Las tuplas tienen pcoos metodos porque son inmutables, pero nos permite consultarlos.
#Las tuplas estan diseñados para no ser modificados, ni agregar, solo leerlos, consultarlos esa es su funcion.

# count(x): Devuelve cuántas veces aparece un valor en la tupla
# index(x): Devuelve el índice de la primera ocurrencia de un valor


tupla = (10, 20, 30, 40, 50)

print(tupla.count(50))

print(tupla.index(30))

#print(dir(tupla))

print(tupla.__contains__(0)) #contains me dice si el valor pasado por parametro existe(true) o no existe(false).
