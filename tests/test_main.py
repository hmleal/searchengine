import unittest

from searchengine.main import SimpleTokenizer


class TestSimpleTokenizer(unittest.TestCase):
    def test_tokenizer(self):
        document = "Good save the Queen!"

        terms = SimpleTokenizer().tokenize(document)
        expected_terms = [("good", 0), ("save", 0), ("queen", 0)]

        self.assertEqual(expected_terms, terms)
