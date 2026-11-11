# ----------------------------------------
# Funciones integradas que trabajan tuplas
# ----------------------------------------

t = (5, 10, 15, 20)

# len(): Devuelve la cantidad de elementos
print(len(t))  # → 4

# sum(): Suma todos los números
print(sum(t))  # → 50

# min(): Devuelve el menor valor
print(min(t))  # → 5

# max(): Devuelve el mayor valor
print(max(t))  # → 20

# sorted(): Devuelve una lista ordenada (no modifica la tupla)
print(sorted(t))  # → [5, 10, 15, 20]

# tuple(): Convierte un iterable en tupla
lista = [1, 2, 3]
print(tuple(lista))  # → (1, 2, 3)

# in: Verifica si un elemento está en la tupla
print(10 in t)  # → True

# iter(): Devuelve un iterador de la tupla
it = iter(t)
print(next(it))  # → 5
