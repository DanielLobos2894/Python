
#la funcion input() muestra un mensaje intuitivo
# para que el usuario ingrese por teclado un valor que sera asignado a la variable que precede al =
nombre = input("ingresa tu nombre: ")

print(f"buenas noches {nombre} .")

genero = input("ingrese su genero (masculino , femenino u otro)")

# (=) define ejemplo uno = 1 el imprimir uno saldria 1 en terminal, 
# (==) comparar ambos datos ejemplo 1 == 1 para cumplir una condicion en este caso se cumple.
if genero == "masculino":
    saludo = "Don "
elif genero == "famenino":
    saludo = "doña "
elif genero == "otro":
    saludo = ""
else :
    saludo="Sin informacion"


print(f"buenas noches {saludo}{nombre}.")