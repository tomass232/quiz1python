inventario = {
    "zapatos": 30,
    "camisas": 10,
    "blusas": 10,
    "gorras": 15,
    "pantalonetas": 20
}
def menu():
    while True:     
        print("1. Ver productos")
        print("2. Editar producto")
        print("3. Eliminar producto")
        print("4. Salir")
        opcion = input("Elija una opcion:")

        if opcion =="1":
            for productos in inventario:
                print(productos)
        elif opcion =="2":
            editar()
        elif opcion =="3":
            eliminar()
        elif opcion =="4":
            print("Gracias por venir")
            break
def editar():
    nombre_llave = input("Ingrese el nombre de la llave que desea editar: ")
    valor_llave = input ("Ingrese el valor de la llave: ")
    inventario[nombre_llave]=valor_llave
    print(inventario)
def eliminar():
    nombre_llave = input ("Ingrese el nombre de la llave que quiere eliminar: ")
    del inventario[nombre_llave]
    print(inventario)
menu()