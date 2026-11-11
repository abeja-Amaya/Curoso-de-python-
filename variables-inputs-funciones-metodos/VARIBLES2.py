#CREAR VARIABLES DE MANERA AVANZADA.


#CONJUNTO CON SET() 
# FROZENSET : Congela un conjunto para meter un conjunto dentro de otro conjunto.

#Metiendo un conjutno dentro de otro conjunto
conjunto1 = frozenset(["dato1, dato2"])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)

#Teoria de conjunto : 
conjunto3 = {1,3,5,7}
conjunto4 = {6,3,4}

#verificamo si es un supconjunto : 
resultado = conjunto4.issubset(conjunto3) 
resultado = conjunto4 <= conjunto3


#verificamos si es superconjunto : 
resultado = conjunto4.issuperset(conjunto3)
resultado = conjunto4 > conjunto3

#verifcar si en un conjunto hay un dato igual al que esta en el otro conjunto
resultado = conjunto4.isdisjoint(conjunto3)
print(resultado)

