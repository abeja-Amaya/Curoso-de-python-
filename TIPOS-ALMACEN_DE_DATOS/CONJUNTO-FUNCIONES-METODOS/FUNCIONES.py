# ----------------------------------------
# Funciones integradas que trabajan sets
# ----------------------------------------

s = {5, 10, 15, 20}

# len(): Cantidad de elementos
print(len(s))  # → 4

# sum(): Suma todos los números
print(sum(s))  # → 50

# min(): Devuelve el menor valor
print(min(s))  # → 5

# max(): Devuelve el mayor valor
print(max(s))  # → 20

# sorted(): Devuelve una lista ordenada
print(sorted(s))  # → [5,10,15,20]

# set(): Convierte un iterable en conjunto
lista = [1,2,2,3]
print(set(lista))  # → {1,2,3}

# in: Verifica si un elemento está en el conjunto
print(10 in s)  # → True

# iter(): Devuelve un iterador del conjunto
it = iter(s)
print(next(it))  # → 5 (o cualquier otro, porque no hay orden)
