#creando una funcion simple 

#def indica al programam q vamos a crear una funcion.
"""def saludar():
    print("Hola lucas, brotheerrr; how are you?")
    
saludar() #inprime

"""

#crear una funcion que tenga parametros.
def saludar(nombre, sexo): 
    sexo = sexo.upper()
    if(sexo == "MUJER"):
        print(f"Hola {nombre}, mi maestra como estas?")
    else:
        print(f"Hola {nombre}, mi maestro como estas?")
saludar("Juan", "HOMBRE")

#crear una funcion que nos retorne valores.
def crearContraseña(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}" 
    print(contraseña)
crearContraseña(3)

#con return podemos retornar valores de una funcion  que se fuarda, y luego podemos utilizarlo
# no como con print.

#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num



# copia y pega del codigo de dalto: 

#desempaquetando la funciòn
password, primer_numero = crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizapos para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")

#utilizando el operador * como argumento (*args)
def suma(nombre,*numeros) :
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

print("____________________________________________________")
resultado = suma("Lucas", 5,3,9,10,20,3)
print(resultado)