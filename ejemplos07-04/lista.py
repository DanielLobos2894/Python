proteinas= [] # lista vacia pero aun es una lista
print(type(proteinas)) # dame el tipo de lo llamado 
print(proteinas)

proteinas.append("Carne") # .append agregar elemento
print(proteinas)

proteinas.append("Pollo")

print(proteinas)

# CRUD

# Crear
verduras = ["lechuga","tomate","palta"]

#Mostrar
print(verduras)

#Actualizar
verduras.append("pepinillos")#agregar
verduras[2]= "Paltita Hass" # Modificar
verduras.insert(1,"potorotos verdes")
#Borrar
#del verduras[1]
print(verduras)
victima = verduras.pop()
print("eliminaste", victima)
#Mostrar resultado
print(verduras)

#verificar si no esta hacer
if "zapallo" not in verduras:
    verduras.append("zapallo")
else:
    print("si esta Zapallo")

print(verduras)

if "zapallo" not in verduras:
    verduras.append("zapallo")
else:
    print("si esta Zapallo")


#verificar si esta hacer
if "zapallo" in verduras:
    print("Si esta")
else:
    verduras.append("zapallo")

print(verduras)

if "zapallo" in verduras:
    print("si esta")
else:
    verduras.append("zapallo")
