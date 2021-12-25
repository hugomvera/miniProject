import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        name1= "John"
        website = "amazon.com"
        p1 = loginCredentials(name1, website)
        print(p1.name)
        print(p1.website)
        print(p1.password)
        self.assertEqual(p1.name, name1)  # test out the name
        self.assertTrue(p1.password)



if __name__ == '__main__':
    unittest.main()
