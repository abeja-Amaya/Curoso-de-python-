# pedirle un dato al usuario 

#nombre = input ("che what is your name: ")
#print(f"His name is : {nombre}")


#num = input ("capi su numero favorio?")
#print(num)

# EJERCICIOS PRACTICOS : 
# De todo lo que vamos a realizar:

pedirPalabra = input("Ingrese tu frase che: ")
partes = pedirPalabra.split(" ")

cantidad = len(partes)
if cantidad >= 120:
    print("Te pedi una frase no un testamento bro.")
else:
    print("Buena che")
