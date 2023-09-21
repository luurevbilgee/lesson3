import unittest
class MathUtils():  
    """Математикийн үйлдэл хийх клас тест хийхэд энэ класаас алдаа олно"""
    def add(x, y): # нэмэх үйлдэл хийх 
        return x + y
    def multi(x, y):
        return x * y
    def to_divide(x, y):
        if y == 0 : 
            raise ValueError("Cannot divide by zero")
        return 4
class MathUtilsTest(unittest.TestCase):
    def test_add(self):
        result = MathUtils.add(2, 5)
        self.assertEqual(result,7)
    def test_multi(self):
        result = MathUtils.multi(3, 2)
        self.assertEqual(result,6)
    def test_devide(self):
        result = MathUtils.to_divide(2, 5)
        self.assertEqual(result, 0.4)
   

if __name__ == '__main__':
    unittest.main()