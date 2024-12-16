import unittest
from cart import Cart


class TestCart(unittest.TestCase):
    def test_apply_discount(self):

        self.cart.add_product(self.product1, 1)  
        self.cart.add_product(self.product2, 2)  
        self.assertEqual(self.cart.apply_discount(100), 1000)
        self.assertEqual(self.cart.apply_discount(1100), 0)
        self.assertEqual(self.cart.apply_discount(1200), 0)

        with self.assertRaises(ValueError):
            self.cart.apply_discount(-50)
            
            
class TestCartAddProduct(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.product1 = Product("Laptop", 1000, 5)
        self.product2 = Product("Mouse", 50, 10)

    def test_add_product_success(self):
        # Ajouter un produit dans le stock disponible
        self.cart.add_product(self.product1, 2)
        self.assertEqual(self.cart.items[self.product1], 2)

        # Ajouter un autre produit
        self.cart.add_product(self.product2, 3)
        self.assertEqual(self.cart.items[self.product2], 3)

    def test_add_product_insufficient_stock(self):
        # Essayer d'ajouter une quantité supérieure au stock disponible
        with self.assertRaises(ValueError) as context:
            self.cart.add_product(self.product1, 6)  # Stock = 5
        self.assertEqual(str(context.exception), "Cannot add 6 of Laptop. Only 5 left.")

    def test_add_product_update_quantity(self):
        # Ajouter un produit plusieurs fois (quantité mise à jour)
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product1, 1)
        self.assertEqual(self.cart.items[self.product1], 3)  # Total : 2 + 1 = 3

    def test_add_product_limit_exceeded(self):
        # Ajouter des produits jusqu'à dépasser la limite de 50
        self.cart.MAX_ITEMS = 10  # Limite temporaire pour tester
        self.cart.add_product(self.product1, 5)
        with self.assertRaises(ValueError) as context:
            self.cart.add_product(self.product2, 6)  # Dépassement de la limite (5 + 6 > 10)
        self.assertEqual(
            str(context.exception),
            "Cannot add 6 of Mouse. Cart limit (10 items) exceeded."
        )

if __name__ == "__main__":
    unittest.main(buffer=False)
    
    
