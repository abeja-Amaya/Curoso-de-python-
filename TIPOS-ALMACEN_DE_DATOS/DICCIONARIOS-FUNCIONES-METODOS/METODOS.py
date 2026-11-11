#
#
# Un diccionario se trabaja con sus keys y values, se puede agergar, modificar, buscar, eliminar.
"""
keys() → devuelve todas las claves.

values() → devuelve todos los valores.

items() → devuelve pares (clave, valor).

get(clave, valor_defecto) → obtiene el valor de una clave sin error si no existe.

update({...}) → agrega o modifica claves/valores.

pop(clave) → elimina una clave específica y devuelve su valor.


popitem() → elimina y devuelve el último par insertado.

clear() → borra todo el diccionario.

setdefault(clave, valor_defecto) → obtiene valor de una clave o la crea si no existe.
"""
#------------------------------------------------------------------------------------------------
################################ print(dir(dic_autos)) devuelve todos los metodos y especiales de una lista. #################################

dic_autos = {
    "Marca": "Toyota",
    "Motor": "22R / 22R-E",
    "Tipo": "Sport",
    "MODELO": "CAR"
}

print(dic_autos.keys())
print(dic_autos.values())
print(dic_autos.items())

print(dic_autos.get("Tipo"))
print(dic_autos.get("Motor"))

print(dic_autos.update({"AÑO: ": 2007})) #se crea un nuevo keys/value.
print(dic_autos.update({"Motor": "224-7777"})) #se modifica el value.


print(dic_autos.pop("Tipo"))
print(dic_autos.pop("MODELO"))

print(dic_autos.setdefault("Marca", "23123"))
print(dic_autos)



