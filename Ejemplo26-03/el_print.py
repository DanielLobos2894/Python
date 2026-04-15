nombre = "Daniel"
paterno = "Lobos"
materno = "Arriaza"

# dentro de un print si llamo una variable luego los uno con (+) este se suman sin caracteres, en cambio si separo por (,) este separara por un espacio
#  al definir un sep = separador podemos separar las variables por lo definido 
print(nombre,paterno,materno , sep="/")


#el end es la finalizacion de las varibles como predeterminado es un \n = enter.
print(nombre,paterno,materno)
print(nombre,paterno,materno , end = " ... ")
print(nombre,paterno,materno)


print("Buenas noches don ",nombre,paterno,materno)

# el formateo de texto
print("Buenas noches don  {} {} {} .".format(nombre,paterno,materno))  # se predifine el orden 0 1 2 .. 
print("-"*30)
print("Buenas noches don  {2} {1} {0} .".format(nombre,paterno,materno)) # podemos definir el indice ejemplo  2 1 0 ....
print(f"buenas noches don {nombre} {paterno} {materno} . ")