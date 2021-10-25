from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            return [product for product in self.products if product.name == product_name][0]
        except IndexError:
            pass

    def remove(self, product_name):
        try:
            product_to_remove = [product for product in self.products if product.name == product_name][0]
            self.products.remove(product_to_remove)
        except IndexError:
            pass

    def __repr__(self):
        result = '\n'.join([f'{product.name}: {product.quantity}' for product in self.products])
        return result

