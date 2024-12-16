# cart.py

from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # {product: quantity}

    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product.name}. Only {product.stock} left.")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product: Product):
        if product in self.items:
            del self.items[product]
        else:
            raise KeyError(f"{product.name} is not in the cart.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def display_cart(self):
        if not self.items:
            return "Your cart is empty."
        return "\n".join([f"{product.name} x {quantity} - {product.price * quantity}€"
                          for product, quantity in self.items.items()])
    
    def apply_discount(self, discount: float):
        """Apply a fixed discount to the total cart value. Returns the new total."""
        total = self.calculate_total()
        if discount < 0:
            raise ValueError("Discount cannot be negative")
        new_total = max(total - discount, 0)  # Total minimum est 0
        return new_total
    
    def delivery_estimate(self):
  
        category_delivery_times = {
            "Électronique": 5,
            "Bureau": 2,
            "Mode": 3
        }
        max_delivery_time = 0

        for product in self.items.keys():
            category = product.category
            max_delivery_time = max(max_delivery_time, category_delivery_times.get(category, 7))

        return f"Estimated delivery time: {max_delivery_time} days."
    
    def delivery_estimate(self):
        """Calculate the estimated delivery time based on the products in the cart."""
        category_delivery_times = {
            "Électronique": 5,
            "Bureau": 2,
            "Mode": 3
        }
        max_delivery_time = 0

        for product in self.items.keys():
            category = product.category
            max_delivery_time = max(max_delivery_time, category_delivery_times.get(category, 7))

        return f"Estimated delivery time: {max_delivery_time} days."