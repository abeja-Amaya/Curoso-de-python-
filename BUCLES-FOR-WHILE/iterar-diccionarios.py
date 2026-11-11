diccionario = {
    "nombre": "Lucas",
    "apellido":"Dalto",
    "subs": 1000000
}

#recorrer diccionario por sus claves
for key in diccionario:
    key
    print(f"dato es : {key}")
    

#Para recorrer diccionarios con el metodo items() mostrando sus keys y su valores.
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"El indice es : {key} ; y su valor es : {value}")