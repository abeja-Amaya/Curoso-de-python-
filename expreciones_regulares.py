

#Para que sirve Import re? 
#import re sirve para importar el módulo re (Regular Expressions) de Python.
#Sin import re, no puedes usar funciones como:
#
import re

texto = """
Mi correo es martin@gmail.com
Mi teléfono es 987654321
Nací en 2001
La web es https://python.org
Mi código es ABC123
"""

# . -> cualquier carácter excepto salto de línea
print(re.findall(r"a.c", "abc axc a7c"))

# ^ -> inicio de una cadena
print(re.findall(r"^Mi", texto, re.MULTILINE))

# $ -> final de una cadena
print(re.findall(r"com$", texto, re.MULTILINE))

# * -> cero o más repeticiones
print(re.findall(r"ab*c", "ac abc abbc abbbc"))

# + -> una o más repeticiones
print(re.findall(r"ab+c", "ac abc abbc abbbc"))

# ? -> cero o una repetición
print(re.findall(r"ab?c", "ac abc abbc"))

# {n} -> exactamente n repeticiones
print(re.findall(r"\d{4}", texto))

# {n,m} -> entre n y m repeticiones
print(re.findall(r"\d{3,5}", texto))

# [] -> conjunto de caracteres permitidos
print(re.findall(r"[aeiou]", "python aprende regex"))

# [^] -> caracteres NO incluidos
print(re.findall(r"[^0-9]", "abc123"))

# | -> operador OR
print(re.findall(r"gato|perro", "perro gato pájaro"))

# \d -> cualquier dígito (0-9)
print(re.findall(r"\d", texto))

# \D -> cualquier cosa que NO sea dígito
print(re.findall(r"\D", "abc123"))

# \w -> letras, números y _
print(re.findall(r"\w+", "Hola_mundo 123"))

# \W -> caracteres especiales
print(re.findall(r"\W", "Hola_mundo!@#"))

# \s -> espacios, tabulaciones o saltos de línea
print(re.findall(r"\s", "Hola mundo"))

# \S -> cualquier cosa que NO sea espacio
print(re.findall(r"\S+", "Hola mundo"))

# \b -> límite de palabra
print(re.findall(r"\bHola\b", "Hola amigo HolaMundo"))

# () -> grupo de captura
print(re.findall(r"(\d{4})", texto))

# Buscar un email simple
print(re.findall(r"\w+@\w+\.\w+", texto))

# Buscar números de teléfono de 9 dígitos
print(re.findall(r"\d{9}", texto))

# Buscar URLs simples
print(re.findall(r"https?://\S+", texto))

# Buscar solo letras mayúsculas
print(re.findall(r"[A-Z]+", texto))

# Buscar letras minúsculas
print(re.findall(r"[a-z]+", texto))

# Buscar códigos tipo ABC123
print(re.findall(r"[A-Z]{3}\d{3}", texto))
