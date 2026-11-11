#encontrnaod ell numero mayor de una lista 
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9,24]
n_mayor = max(lista) #mayor 
print(f"numero mayor {n_mayor}")

numero_minimo = min(lista) #minimo
print(f"nummero minimo {numero_minimo}")

# redondeando a 6 decimales con round() :
numero = round(31.242456, 2)
print(f"numero redondeado {numero}")

#return false -> 0 vacio, false, ninguno. de lo contrarrio devuelve True.
resultado = bool(0)
print(f"resultado {resultado}")

#return True si todo los valores son verdaderos. si hubiera un False dentro daria error.
resu = all([12, 13, "GAGA",[11,22]])
print(resu)

#suma todos los valores de un iterable 
sumatotal = sum(lista)
print(sumatotal)