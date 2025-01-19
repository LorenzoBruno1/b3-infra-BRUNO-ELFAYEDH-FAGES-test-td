import unittest
from product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        # Setup a product instance for testing
        self.product = Product(name="Laptop", price=1200.0, stock=5)
        print("\n[Setup] Created a Product instance for testing.")

    def test_product_initialization(self):
        print("[Test] Testing Product Initialization...")
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.price, 1200.0)
        self.assertEqual(self.product.stock, 5)
        print("[Test] Product Initialization passed.")

    def test_reduce_stock_success(self):
        print("[Test] Testing Reduce Stock (Success Case)...")
        print(f"Before reducing stock: {self.product.stock}")
        self.product.reduce_stock(2)
        print(f"After reducing stock: {self.product.stock}")
        self.assertEqual(self.product.stock, 3)
        print("[Test] Reduce Stock (Success Case) passed.")

    def test_reduce_stock_failure(self):
        print("[Test] Testing Reduce Stock (Failure Case)...")
        with self.assertRaises(ValueError) as context:
            self.product.reduce_stock(10)
        print(f"[Test] Caught exception: {context.exception}")
        self.assertEqual(str(context.exception), "Insufficient stock for Laptop. Available: 5")
        print("[Test] Reduce Stock (Failure Case) passed.")

    def test_str_representation(self):
        print("[Test] Testing String Representation...")
        result = str(self.product)
        print(f"String representation: {result}")
        self.assertEqual(result, "Laptop (1200.0€, Stock: 5)")
        print("[Test] String Representation passed.")

if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering to display prints