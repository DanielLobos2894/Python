print("""
***MENU DE CATEGORIAS****
-------------------------
    1) LACTEOS.
    2) CARNES.
    3) BEBIDAS.
    4) FRUTAS.
-------------------------
""")
#entrada de dato convertida de sntring a int
categoria = int(input("ingresar opcion: "))
#opcion paso a paso podemos pedir la respuesta y luego llamarla para transformar a int; categoria = int(categoria)

print("+"*40)
match categoria :
    case 1: 
        print("yogurt","Leche","queso",sep="\n")
    case 2:
        print("huachalomo","pollo","cerdo",sep="\n")
    case 3:
        print("cocacola", "pepsi" ,"fanta",sep="\n")
    case 4:
        print("platano","naranja","pera",sep="\n")
    case _:
        print("categoria no valida")

print("+"*40)
