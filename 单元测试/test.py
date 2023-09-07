import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.first_word_upper(text)
        self.assertEqual(result,'Python')
    def text_many_word(self):
        text = "xlp's python"
        result = cap.first_word_upper(text)
        self.assertEqual(result,"Xlp's Python")

if __name__ == '__main__':
    unittest.main()