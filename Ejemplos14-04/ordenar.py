peliculas = [
    "Mickey 17",
    "Superman",
    "The Fantastic Four: First Steps",
    "Avatar: Fire and Ash",
    "28 Years Later",
    "Thunderbolts*",
    "Jurassic World: Rebirth",
    "The Bride!",
    "Blade Runner 2099",
    "Mission: Impossible - Dead Reckoning Part Two"
]

#sort ordena de forma acendente
#sort(reverse=True) orden de forma decendente
#peliculas.sort(reverse=True)

#orden de la cantidad de caracteres
peliculas.sort(key=len)


#for indice,peli in enumerate(peliculas):
#   print(f"{indice + 1}) {peli}.")
    

#Creamos una copia ordenada a partir de otra lista
peliculas_ordenada = peliculas
peliculas.append("tu hermana")

print(peliculas_ordenada)
print(peliculas)
#for indice,peli in enumerate(peliculas_ordenada):
#   print(f"{indice + 1}) {peli}.")

#largo = len(peliculas)
#print(f"la cantidad de la lista es de {largo} titulos.")