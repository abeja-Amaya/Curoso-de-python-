#abriendo el archivo con with open
with open("Archivos\\datos.txt",encoding="UTF-8") as archivo: 

    #leemos el archivo
    contenido = archivo.read() # es necesario el read para leer el archivo.

    #mostramos el archivo
    print(contenido)

#no es necesario cerrarlo al usar with open