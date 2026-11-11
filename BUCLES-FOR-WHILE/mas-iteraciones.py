


frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = {"THE WROLD"}
numeros = {2, 6, 10}
#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer una {fruta}')
    
    
#evitar que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == 'pera':
        break
print(f'Me voy a comer una {fruta} ')
print("bucle terminado")


#recorer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de codigo (duplicamos los numerosp
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)