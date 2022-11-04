import unittest
from translator import english_to_french,french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual('','')
        self.assertNotEqual(english_to_french('Hello'),'Hello')
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_french_to_english(self):
        self.assertEqual('','')
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__=='__main__':
    unittest.main()
