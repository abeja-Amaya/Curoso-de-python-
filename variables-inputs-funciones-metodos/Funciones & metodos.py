

# upper() = convierte todo a masyuscula
# lower() = convierte todo a minuscula

# Capitalize() = convierte todo a minuscula exepto la primera letra.

# find() = encuentra y devuelve la posicion. 
# index() = buscamos una cadena en otra cadena si no hay concidencia devuelve false. 

# isnumeric() = devuelve true si es numero y false si no es numerico.
# count() = cuenta las concidencias que hay en todo una cadena, texto o numero.
# isalpha() = si es alfanumerico devuelve true de lo contrario false. 

# len() = cuenta cuantos caracteres hay en una cadena. 
# startswith() = verifica si una cadena dada es igual a la acdena que ya esta.

# endswith() = verificamos si termina con la misma caracter que le pasamos si es asi devuelve true.
# replace() = reemplaza la cadena que le pasamos por la que queremos.
# split() = separa la cadena por seárado y lo junta en una lista.


cadena = "yosoy"
cadena2 = "Batman"

cadena = "hola, yo soy, Pedro"
resultado = cadena.split(",")
print(resultado[2])

resultado = cadena2.replace("Batman", "Spiderman")
print(resultado)


resultado = cadena.endswith("y")
print(resultado)

resultado = cadena.startswith("y")
print(resultado)

resul = len(cadena2)
print(resul)

resu = cadena.count("deee")
print(resu)

resu = cadena2.isalpha()
print(resu)

resu = cadena.isnumeric()
print(resu)

cadenaa = "hola, yo soy Pedro"
resultado = cadenaa.index("yo soy")
print(resultado)

resultado = cadena.find("soy")
print(resultado)

mostrar = cadena.upper()
print(mostrar)

mostrar = cadena2.lower()
print(mostrar)

mostrar = cadena.capitalize()
print(mostrar)

mostrar = cadena.find("s") #devuelve -1 si no hay.
print(mostrar)

