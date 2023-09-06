import unittest
from translator import frenchtoenglish, englishtofrench


class TestFrenchToEnglish(unittest.TestCase):
    def test_frenchtoenglish1(self):
        self.assertEqual(frenchtoenglish("bonjour"),"hello")
    def test_frenchtoenglish2(self):
        self.assertNotEqual(frenchtoenglish("bonjour"),"bonjour")      
class TestEnglishToFrench(unittest.TestCase):
    def test_englishtofrench1(self):
        self.assertEqual(englishtofrench("hello"),"bonjour")
    def test_englishtofrench2(self):
        self.assertNotEqual(englishtofrench("hello"),"hello")
        
if __name__ == '__main__':
    unittest.main()
        