import json, os, time

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
INVENTORY_PATH = os.path.join(BASE_PATH, "inventory.json")


class Product:
    def __init__(self, name, category, stock, price):
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "stock": self.stock,
            "price": self.price,
        }

    @staticmethod
    def from_dict(data):
        return Product(data["name"], data["category"], data["stock"], data["price"])


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for i in self.products:
            if i.name == product.name and i.category == product.category:
                print(
                    f"Ya existe el producto '{product.name}' en la categoría '{product.category}'."
                )
                return
        self.products.append(product)
        print(f"Producto '{product.name}' agregado correctamente.")

    def show_products(self):
        if not self.products:
            print("Inventario vacío.")
            time.sleep(1)
        for i, p in enumerate(self.products, 1):
            print(f"{i}. {p.name} - {p.category} - Stock: {p.stock} - ${p.price}")
            time.sleep(1)

    def change_stock(self, name, category, stock):
        for i in self.products:
            if i.name == name and i.category == category:
                i.stock = stock
                print(
                    f"Stock actualizado para '{name}' en categoría '{category}' a {stock} unidades."
                )
                return
        print(f"No se encontró el producto '{name}' en la categoría '{category}'.")

    def change_price(self, name, category, price):
        for i in self.products:
            if i.name == name and i.category == category:
                i.price = price
                print(
                    f"Precio actualizado para '{name}' en categoría '{category}' a ${price}."
                )
                return
        print(f"No se encontró el producto '{name}' en la categoría '{category}'.")

    def remove_product(self, name, category):
        for i, producto in enumerate(self.products):
            if producto.name == name and producto.category == category:
                del self.products[i]
                print(f"Producto '{name}' en categoría '{category}' eliminado.")
                return
        print(f"No se encontró el producto '{name}' en la categoría '{category}'.")

    def save(self):
        with open(INVENTORY_PATH, "w", encoding="utf-8") as f:
            data = [p.to_dict() for p in self.products]
            json.dump(data, f, indent=2)
        print("Inventario guardado.")
        time.sleep(1)

    def load(self):
        if not os.path.exists(INVENTORY_PATH):
            print("No hay inventario guardado aún.")
            time.sleep(1)
            return
        with open(INVENTORY_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.products = [Product.from_dict(p) for p in data]
        print("Inventario cargado.")
        time.sleep(1)