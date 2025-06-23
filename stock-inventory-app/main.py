from data.inventory import Inventory, Product


def menu():
    print("\n==== SISTEMA DE INVENTARIO ====")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Modificar Stock")
    print("4. Cambiar Precio")
    print("5. Eliminar Producto")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("0. Salir")
    return input("Selecciona una opción: ")


def ask_for_data(basics=False):
    name = input("Nombre del producto: ")
    category = input("Categoría: ")
    if basics:
        return name, category
    stock = int(input("Cantidad en stock: "))
    price = float(input("Precio: "))
    return name, category, stock, price


def main():
    inventory = Inventory()
    try:
        inventory.load()
    except Exception:
        pass

    while True:
        option = menu()
        if option == "1":
            inventory.show_products()

        elif option == "2":
            name, category, stock, price = ask_for_data()
            inventory.add_product(Product(name, category, stock, price))
            inventory.save()

        elif option == "3":
            name, category = ask_for_data(basics=True)
            stock = int(input("Nuevo stock: "))
            inventory.change_stock(name, category, stock)
            inventory.save()

        elif option == "4":
            name, category = ask_for_data(basics=True)
            price = float(input("Nuevo precio: "))
            inventory.change_price(name, category, price)
            inventory.save()

        elif option == "5":
            name, category = ask_for_data(basics=True)
            if input("Seguro de esta acción (y/N): ").lower() == "y":
                inventory.remove_product(name, category)
                inventory.save()

        elif option == "6":
            inventory.save()

        elif option == "7":
            try:
                inventory.load()
            except Exception:
                inventory.save()

        elif option == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
