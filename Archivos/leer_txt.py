
# consejos : 
# 1. Si el archvio txt tiene muchas demasidas lineas de codigo, este no es el procedimeinto ya que va consumir muchos recursos, CPU, MEMORIA.
# -- se debe utilizar otro metodo.
# 2. Es importante cerrar el archivo una vez ya leido.
#


#usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo = open("Archivos\\datos.txt",encoding="UTF-8")

#leer archivo completo
archivo = archivo.read()

#leer una sola linea
#linea = archivo.readline()

#leer linea por linea
#lineas = archivo.readlines()

#cerrar el archivo
# archivo.close() 
print(archivo)

