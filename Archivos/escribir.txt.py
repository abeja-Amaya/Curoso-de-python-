

with open('Archivos\\datos.txt', 'w',encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("Jajajajaa te la recontra teclee")

    #agregando 2 lineas con writelinls
    archivo.writelines([" - Hola maestro como andas\n"," - misericordia\n"])

    #gregando otras 2 lineas
    archivo.writelines([" - no se porque dijiste eso\n"," - yo tampoco"])