# importaciones
# desde la libreria colorama importa las funciones para la fuente y fondo
from colorama import Fore,Back

productos = ["Churrasco Italiano","Completo"]

# Implementación
def menu():
    print(Fore.GREEN +"""
***** Mantenedor de Productos *****
-----------------------------------
    1) Mostrar todos los Productos.
    2) Buscar Producto
    3) Agregar Producto
    4) Modificar Producto
    5) Eliminar un Producto
    6) Salir
-----------------------------------
***********************************
""")
    opcion = input("Ingrese el número de la opción seleccionada: ")
    return opcion

def mostrar_todos(lista):
    print(Fore.CYAN + "*** LISTADO DE PRODUCTOS ****")
    print("-----------------------------")
    for num,elemento in enumerate(lista,1):
        print(f"{num}) {elemento}")    
    print("-----------------------------")





# ------------------------------- EJECUCIÓN DE L CÓDIGO ----------------
# Llamada
resultado = menu()

if resultado=="1":
    mostrar_todos(productos)
elif resultado=="2":
    pass # buscar()
elif resultado == "3":
    pass # agregar()
elif resultado == "4":
    pass # modificar():
elif resultado == "5":
    pass # eliminar()
elif resultado == "6":
    pass # salir()
else:
    print("Solo se permiten opciones entre 1 y 6")


"""
inventario = [
    ["Churrasco",4500,5],
    ["Completo",1900,20,["Tomate","Palta","Chucrut","Salchicha","Pan"]],
]
"""
