# len(dic) → devuelve la cantidad de pares clave‑valor.
# sorted(dic) → devuelve las claves ordenadas alfabéticamente.
# sum(dic.values()) → suma todos los valores numéricos.
# max(dic.values()) → devuelve el valor máximo.
# min(dic.values()) → devuelve el valor mínimo.
# any(dic) → devuelve True si hay al menos una clave.
# all(dic) → devuelve True si todas las claves son “truthy” (no vacías, no 0, no False).

# dict() → crea un diccionario nuevo.

dic_alumno_nota = {
    "Mario": 10,
    "False" : 11,
    "Pedro": 20,
    "": 17
}
cantidad_de_pares = len(dic_alumno_nota)
print(f"Cantidad de pares del dic : {cantidad_de_pares}")

print("Ordenar Alfaveticamente:")
ordenarAlfaveticamente = sorted(dic_alumno_nota)
print(ordenarAlfaveticamente)

valores = dic_alumno_nota.values()
suma = sum(valores)
print(f"Suma total de valores : {suma}")

n_maximo = max(valores)
print(f"Valor maximo del dic {n_maximo}")

n_minimo = min(valores)
print(f"Valor minimo del dic : {n_minimo}")


True_si_hay_al_menos_una_clave = any(dic_alumno_nota)
print(f"Evaluar : {True_si_hay_al_menos_una_clave}")

evaluar2 = all(dic_alumno_nota)
print(f"evaluar : {evaluar2}")