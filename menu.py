nombres = ["Maripaz", "Tomás", "Sofía", "Gabriel"]

while True:
    print("\n -menu-")
    print("1. Mostrar un mensaje motivacional")
    print("2. Mostrar una lista de nombres")
    print("3. Salir del programa")

    opcion = input("Elige una opción (1, 2 o 3): ").strip()

    if opcion == "1":
        print("\nAlgún día vas a encontrar alguien que te ame como Tomás ama a Maripaz")
    elif opcion == "2":
        print("\nLista de nombres:")
        for nombre in nombres:
            print("-", nombre)
    elif opcion == "3":
        print("\nGracias por usar el programa")
        break
    else:
        print("\nOpción no válida. Por favor elige 1, 2 o 3.")
