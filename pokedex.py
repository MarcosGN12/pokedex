from almacenamiento import pokemons
from util import clear_console

def mostrar_pokemons():
    for pokemon in pokemons:
        nombre_pokemon =  str(pokemon[0]) + " " + pokemon[1]
        print(nombre_pokemon)
        
def mostrar_detalles_pokemon(numero_pokemon):
    for pokemon in pokemons:
        if numero_pokemon == pokemon[0]:
            print(f"Num. {pokemon[0]}")
            print(f"Nombre: {pokemon[1]}")
            print(f"Tipo: {pokemon[2]} ")
            print(f"HP: {pokemon[3]}")
            print(f"AT: {pokemon[4]}")
            print(f"DEF: {pokemon[5]}")
            print(f"Vel: {pokemon[6]}")
            print(f"Altura: {pokemon[7]}")
            print(f"Peso: {pokemon[8]}")
            print("")
        

def mostrar_menu():



    while True:
        mostrar_pokemons()
        opcion = int(input("¿Que Pokemon quieras ver? Introduzca su número: "))
        clear_console()
        mostrar_detalles_pokemon(opcion)
        opcion1 = int(input("0.Cerrar el programa, 1.Volver al menu de pokemons "))
        
        if opcion1 == 0:
            break

        if opcion1 == 1:
            continue
