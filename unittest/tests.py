import hello
import unittest

class HelloTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.hi = hello.Hello(50)

    def test_a(self):
        self.assertEqual(self.hi.m(), 5)

    def test_b(self):
        self.assertEqual(self.hi.m(), 5)

    def test_c(self):
        self.assertTrue(self.hi.b(51))

    def test_d(self):
        self.assertFalse(self.hi.b(2))





