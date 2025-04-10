inventario = {
    "zapatillas": 120,
    "camisetas": 85,
    "gorras": 40,
    "pantalones": 60
}
print("INVENTARIO INICIAL:")
print(inventario)
print("-" * 40)

clave_secreta = input("Por favor, ingresa la clave para poder modificar o eliminar artículos: ").strip()

if clave_secreta == "maripaz":
    clave_modificar = input("Ingresa el nombre del artículo que deseas modificar: ").strip()

    if clave_modificar in inventario:
        nuevo_valor = input(f"Ingrese el nuevo valor para '{clave_modificar}': ").strip()

        if nuevo_valor.isdigit():
            inventario[clave_modificar] = int(nuevo_valor)
            print(f"'{clave_modificar}' actualizado correctamente.")
        else:
            print("El valor ingresado no es válido. Debe ser un número.")
    else:
        print(f"El artículo '{clave_modificar}' no se encuentra en el inventario.")

    print("\nINVENTARIO DESPUÉS DE LA MODIFICACIÓN:")
    print(inventario)
    print("-" * 40)

    clave_eliminar = input("Ingresa el nombre del artículo que deseas eliminar: ").strip()

    if clave_eliminar in inventario:
        del inventario[clave_eliminar]
        print(f"'{clave_eliminar}' fue eliminado del inventario.")
    else:
        print(f"No se encontró el artículo '{clave_eliminar}', no se realizó ningún cambio.")

    print("\nINVENTARIO FINAL:")
    print(inventario)
    print("-" * 40)

else:
    print("Clave incorrecta. No tienes permiso para modificar ni eliminar artículos.")
