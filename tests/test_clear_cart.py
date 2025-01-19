import unittest
from cart import Cart
from product import Product  

class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        print("\n[Setup] Création d'un panier pour les tests.")

    def test_clear_cart_when_empty(self):
        print("[Test] Test clear_cart quand le panier est vide...")
        self.cart.clear_cart() 
        self.assertEqual(len(self.cart.items), 0)  
        print("[Test] Test clear_cart quand le panier est vide passé.")

    def test_clear_cart_when_not_empty(self):
        print("[Test] Test clear_cart quand le panier contient des articles...")
        laptop = Product("Laptop", 1200.0, 10)
        smartphone = Product("Smartphone", 800.0, 10)
        self.cart.add_product(laptop, 1)
        self.cart.add_product(smartphone, 2)
        self.cart.clear_cart()  
        self.assertEqual(len(self.cart.items), 0)  
        print("[Test] Test clear_cart quand le panier contient des articles passé.")

    def test_clear_cart_with_non_list_items(self):
        
        print("[Test] Test clear_cart avec une structure non valide pour items...")
        self.cart.items = "Invalid type"  
        with self.assertRaises(TypeError):  
            self.cart.clear_cart()  
        print("[Test] Test clear_cart avec une structure non valide pour items passé.")

    def test_clear_cart_when_no_items_attribute(self):
        print("[Test] Test clear_cart sans attribut 'items'...")
        del self.cart.items  
        with self.assertRaises(AttributeError):  
            self.cart.clear_cart()  
        print("[Test] Test clear_cart sans attribut 'items' passé.")

if __name__ == "__main__":
    unittest.main(buffer=False)  