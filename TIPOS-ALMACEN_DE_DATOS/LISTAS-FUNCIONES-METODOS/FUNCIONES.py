# ================================
# Funciones útiles con listas
# ================================

# help() te muestra documentación completa del objeto
#lista = [1, 2, 3]##################################################################################
#help(lista) ################################################################################## 


# len(lista) → cantidad de elementos
# sum(lista) → suma de números
# min(lista), max(lista) → mínimo y máximo
# sorted(lista) → nueva lista ordenada (no modifica la original)
# reversed(lista) → iterador en orden inverso


nm = [10, 13, 27, 31, 11]

print(len(nm))

print(sum(nm))

print(min(nm))

print(max(nm))

print(sorted(nm)) # ordena de mayor a menor

for n in reversed(nm): #muestra de atras a delante-
    print(n)