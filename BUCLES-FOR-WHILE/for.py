animales = ["pez", "caballo", "pulga"]
numeros = [100,20,11]

for animal in animales : 
    print(animal)

#Se puede iterar haciendo una anidacion de bulces jutnos.
#Si queremos iterar ambas listas juntas con zip 
#primero regla: mabas listas deben tener la misma cantidad de datos. 

for numero, animal in zip(animales, numeros):
    print(f"lista 1 : {animal}")
    print(f"list 2 :  {numero}")
    
#iterar con un range 
for num in range(10,21):
    print(num)

#itera solo los numeros de 0 - 5.
for num in range(5):
    print(num)
    
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
print(f'el indice es: {indice} y el valor es: {valor}')


#usando el else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
    """
El programa debe calcular:

El promedio de cada estudiante.

Quién tiene la mejor nota promedio.
"""

Alumnos = { 
    "Pedro": [12, 17, 15, 11, 19],
    "Diego": [13, 17, 17, 19, 18]
    }

#como es diccionario, estamos tratando con keys y value.
for nombre, notas in Alumnos.items():
    suma = sum(notas)
    promedio = suma / len(notas)
    print(f"{nombre} tiene un promedio de: {promedio}")

