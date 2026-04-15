#un diccionario se compone de elementos.
#clientes = {elem1,elm2.elem3... n}
#cada elemento se compone de clave:valor
#cliente = {"run": "24.625.985-8" , "nombre" : "alan".....}



clientes = {
    101:{"run":"18.888.791-7","Nombre":"Daniel","Apellido":"lobos","edad":31},
    102:{"run":"18.251.794-1","Nombre":"Barbara","Apellido":"Soto","edad":33}
}

print(clientes[102]["Nombre"])

for c in clientes.values() :

    print(c["Nombre"])
