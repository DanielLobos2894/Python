productos = ["churrasco italinao" , "Completo "]

# Implementacion
def menu ():
    print("""
        ******** Mantenedor de Productos ********
        -----------------------------------------
            1) Mostrar todos los produtos.
            2) Buscar producto
            3) Agregar producto
            4) Modificar producto
            5) Eliminar un producto
            6) Salir
        -----------------------------------------
        *****************************************
          
          """)
    opcion = int(input("ingrese el numero de la opcion seleccionada"))
    return opcion

def mostrar_todo(lista):
    print("**** Listado de Productos ****")
    print("------------------------------")
    for num,elemento in enumerate(lista, 1):
        print(f"{num}) {elemento}")
    print("------------------------------")



# Llamada
resultado = menu()

match resultado:
    case 1:
        mostrar_todo(productos)
    case 2:
        pass 
    case 3:
        pass
    case 4:
        pass
    case 5:
        pass
    case 6:
        print("adios")
    case _:
        print("categoria no valida")
    


