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

if __name__ == "__main__":
    unittest.main(buffer=False)
    
    
