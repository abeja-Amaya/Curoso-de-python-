

with open("Archivos\\datos.csv",encoding="UTF-8") as archivo: 

    #leemos el archivo csv
    contenido = archivo.read() # es necesario el read para leer el archivo.

    #mostramos el archivo csv
    print(contenido)