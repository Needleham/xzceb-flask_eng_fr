import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        # Test Hello does not return Bonjour
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        #Test None returns empty string
        self.assertEqual(english_to_french(None), "")
        #Test empty string returns empty string
        self.assertNotEqual(english_to_french(0),0)
    def test_french_to_english(self):
        #Test Bonjour returns Hello
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        #Test Bonjour does not return Bonjour
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')
        #Test None returns empty string
        self.assertEqual(french_to_english(None),"")
        #Test empty string returns empty string
        self.assertNotEqual(french_to_english(0),0)


if __name__=='__main__':
    unittest.main()
