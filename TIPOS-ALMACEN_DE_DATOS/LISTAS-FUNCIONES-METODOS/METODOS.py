# ================================
# Métodos más usados en listas Python
# ================================

# append(x) → Agrega un elemento al final
# Ejemplo: a=[1,2]; a.append(3) → [1,2,3]

# extend(iterable) → Agrega varios elementos (une otra lista)
# Ejemplo: a=[1,2]; a.extend([3,4]) → [1,2,3,4]

# insert(i,x) → Inserta en posición específica
# Ejemplo: a=[1,3]; a.insert(1,2) → [1,2,3]

# remove(x) → Elimina la primera ocurrencia de x
# Ejemplo: a=[1,2,2,3]; a.remove(2) → [1,2,3]

# pop(i) → Elimina y devuelve elemento (último si no se indica índice)
# Ejemplo: a=[1,2,3]; a.pop() → [1,2]

# clear() → Vacía la lista
# Ejemplo: a=[1,2,3]; a.clear() → []

# index(x) → Devuelve posición de la primera ocurrencia
# Ejemplo: a=[10,20,30]; a.index(20) → 1

# count(x) → Cuenta cuántas veces aparece x
# Ejemplo: a=[1,2,2,3]; a.count(2) → 2

# sort() → Ordena la lista (ascendente por defecto)
# Ejemplo: a=[3,1,2]; a.sort() → [1,2,3]

# reverse() → Invierte el orden de la lista
# Ejemplo: a=[1,2,3]; a.reverse() → [3,2,1]

# copy() → Devuelve una copia superficial de la lista
# Ejemplo: a=[1,2]; b=a.copy() → [1,2]

# ================================
# Funciones útiles con listas
# ================================

# len(lista) → cantidad de elementos
# sum(lista) → suma de números
# min(lista), max(lista) → mínimo y máximo
# sorted(lista) → nueva lista ordenada (no modifica la original)
# reversed(lista) → iterador en orden inverso

################################ print(dir(nm)) devuelve todos los metodos y especiales de una lista. #################################

listaN = ["Francia", "Diaz", "Ale"]

listaN.append("Oscar")
print(f"Agregando un elemento al final : {listaN}")

listaN.extend(["Nicole", "Julia", "Adriana"])
print(f"Agregando dos elementos mas : {listaN}")

listaN.insert(0,"Bri")
print(f"Insertando un elemento al inicio por su indice : {listaN}")

listaN.remove("Julia")  # se elimina por elemento
print(f"Eliminamos a Julia : {listaN}")

listaN.pop(2)  # se elimina por indice
print(f"Eliminamos a Diaz: {listaN}")

