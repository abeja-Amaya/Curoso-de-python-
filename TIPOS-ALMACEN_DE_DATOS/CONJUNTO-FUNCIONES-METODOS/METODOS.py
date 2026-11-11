#Los conjuntos (set) son colecciones no ordenadas y sin elementos duplicados.
#Se usan en negocios para manejar datos únicos y operaciones de pertenencia.

# -------------------------------
# Métodos de conjuntos en Python
# -------------------------------

s = {1, 2, 3}

# add(x): Agrega un elemento al conjunto
s.add(4)  # → {1,2,3,4}

# remove(x): Elimina un elemento (error si no existe)
s.remove(2)  # → {1,3,4}

# discard(x): Elimina un elemento (no error si no existe)
s.discard(10)  # → {1,3,4}

# pop(): Elimina y devuelve un elemento aleatorio
print(s.pop())  # → elimina cualquiera

# clear(): Vacía el conjunto
s.clear()  # → set()

# copy(): Devuelve una copia del conjunto
s1 = {1,2,3}
s2 = s1.copy()  # → {1,2,3}

# union(): Une dos conjuntos
a = {1,2}; b = {2,3}
print(a.union(b))  # → {1,2,3}

# intersection(): Elementos comunes
print(a.intersection(b))  # → {2}

# difference(): Elementos en A que no están en B
print(a.difference(b))  # → {1}

# symmetric_difference(): Elementos en A o B pero no en ambos
print(a.symmetric_difference(b))  # → {1,3}

# issubset(): Verifica si A está contenido en B
print({1,2}.issubset({1,2,3}))  # → True

# issuperset(): Verifica si A contiene a B
print({1,2,3}.issuperset({1,2}))  # → True

# isdisjoint(): Verifica si no tienen elementos en común
print({1,2}.isdisjoint({3,4}))  # → True
