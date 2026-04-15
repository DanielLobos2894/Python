#declarar una tupla
tupla = ()

#acceder a una tajada dentro de la tupla

frutas = ("manzana" , "pera " , "naranjas","piña","platano","coco")

#
print(frutas[1:6:2])

print(len(frutas))

print("piña" in frutas)

print("maracuya" not in frutas)

verduras = ("lechuga" , "tomates", "cebollas")
nueva_tupla = frutas + verduras
print(nueva_tupla)

print(min(frutas))
print(max(frutas))