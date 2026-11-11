#
#
#

#----------------------EJERCICIOS : -----------------------------------
dic_alumno_nota = {
    "Mario": 10,
    "Juan": 17,
    "Pedro": 20
}

pares = dic_alumno_nota.items()
for nombre, nota in pares:
    print(f"Alumno {nombre} tiene nota {nota}")

dic_alumno_nota.clear()
print(dic_alumno_nota)   



#------------------------ 01 --------------------------------------
dic_nombre_numero = {
    "Mario": 15,
    "Juan": 17,
    "Pedro": 11
}

print(dic_nombre_numero.get("Pedro"))       # 11
dic_nombre_numero.setdefault("Persi", 21)
print(dic_nombre_numero)

#------------------------ 02 -------------------------------------


dic_product_precio = {
    "Audiculares": 20,
    "Laptop": 800,
    "Celar": 500
}

dic_product_precio.update({"Mauz": 30})
dic_product_precio.pop("Audiculares")

print(dic_product_precio.keys())
