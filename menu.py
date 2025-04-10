lista_nombres = ["Dilii","Maripaz","Tomás"]
def menu():
    while True:
        print("1. Mensaje motivacional")
        print("2. Lista de nombres")
        print("3. Salir")
        opcion = input("Digite una opcion:")

        if opcion =="1":
            print("Tranquilo algún día alguien te va a amar como Tomás ama a Mari")
        elif opcion =="2":
            for nombre in lista_nombres:
                print(nombre)
        elif opcion =="3":
            print("Gracias por venir")
            break

menu()