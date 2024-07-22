import unittest
from app.property import Property

class TestSetId(unittest.TestCase):
    
    # testcase 1
    def test_id_one(self):
        ''''''
        p1 = Property()
        self.assertEqual(p1.get_id(), 1)

    # testcase 2
    def test_id_two(self):
        p2 = Property()
        self.assertEqual(p2.get_id(), 2)

class TestSetAddress(unittest.TestCase):

    # street_number

    # testcase 1
    def test_int(self):
        pass
        
if __name__ == '__main__':
    unittest.main()
