from almacenamiento import pokemons
from util import clear_console


def mostrar_menu_inicial():
        print("")
        print("POKEDEX")
        print(" ")
        print("Presiona un número para seleccionar una acción.")
        print(" ")
        print("1. Ver lista de Pokemons")
        print("2. Añadir un nuevo Pokemon")
        print("3. Editar un Pokemon")
        print("4. Borrar un Pokemon")
        print(" ")
        print("0. Salir")
        print("")
        opcion_menu_inicial = int(input("> "))
        for pokemon in pokemons:
            if opcion_menu_inicial == 0:
                clear_console()
                break

            if opcion_menu_inicial == 1:
                clear_console()
                mostrar_menu()
                break

            if opcion_menu_inicial == 2:
                clear_console()
                break

            if opcion_menu_inicial == 3:
                clear_console()
                break

            if opcion_menu_inicial == 4:
                clear_console()
                break

def mostrar_pokemons():
    for pokemon in pokemons:
        nombre_pokemon = str(pokemon[0]) + " " + pokemon[1]
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
        print(" ")
        numero_pokemon = int(input("Elija numero de pokemon para detalles o pulse 0 para salir del programa > "))

        if numero_pokemon == 0:
            clear_console()
            break

        clear_console()

        mostrar_detalles_pokemon(numero_pokemon)

        print("0.Cerrar el programa.")
        print("1.Volver al menu de pokemons.")
        print("")
        opcion_menu = int(input("> "))
        clear_console()
        if opcion_menu == 0:
            break

        if opcion_menu == 1:
            continue