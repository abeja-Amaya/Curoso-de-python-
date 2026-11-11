animales = ("pez", "caballo", "pulga")
numeros = (100,20,11)

for animal in animales : 
    print(animal)

#Se puede iterar haciendo una anidacion de bulces juntos.
#Si queremos iterar ambas conjuntos juntas con zip 
#primero regla: mabas conjuntos deben tener la misma cantidad de datos. 

for numero, animal in zip(animales, numeros):
    print(f"conjunto 1 : {animal}")
    print(f"list 2 :  {numero}")
    
#iterar con un range 
for num in range(10,21):
    print(num)

#itera solo los numeros de 0 - 5.
for num in range(5):
    print(num)
    
    
#forma correcta de recorrer una conjunto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
print(f'el indice es: {indice} y el valor es: {valor}')


#usando el else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")


#AL IGUAL QU ELISTAS Y CONJUTNO TAMBIEN ES LA MSIMA LOGICA PARA ITERAR TUPLAS.
#Los diccioanrio si tienen otra manera de iterar.