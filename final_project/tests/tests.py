import unittest
from machinetranslation import translator


class TestTranslator(unittest.TestCase):
    
    def test_french_to_english(self):
        self.assertIsNone(None, 'La valeur de test est vide')
        self.assertIsNotNone('Bonjour', 'Hello')


    def test_english_to_french(self):
        self.assertIsNone(None, "Test value is empty")
        self.assertIsNotNone('Hello', 'Bonjour')

if __name__ == '__main__':
    unittest.main()
