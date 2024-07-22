import unittest
from app.property import Property
from unittest.mock import patch

class TestSetId(unittest.TestCase):
    
    # testcase 1
    def test_id_one(self):        
        p1 = Property()
        self.assertEqual(p1.get_id(), 1)

    # testcase 2
    def test_id_two(self):
        p2 = Property()
        self.assertEqual(p2.get_id(), 2)

class TestSetAddress(unittest.TestCase):

    # street_number

    # testcase 1
    @patch('builtins.input', side_effect=[6573, '', '', '', 0])
    def test_int(self, mock_inputcls) -> None:
        '''Test for int input value'''  
        p1 = Property()        
        p1.set_address()
        expected = {'street_number': 6573, 'street_name': '', 'county': '', 'state': '', 'zip_code': 0}     
        self.assertEqual(p1.get_address(), expected)

    # testcase 2
    @patch('builtins.input', return_value=[6.573, '', '', '', 0])
    def test_float(self, mock_input) -> None:
        '''Test for float input value''' 
        p2 = Property()             
        with self.assertRaises(TypeError):
            p2.set_address() # float numofBedrooms numofBathrooms        

    # testcase 3
    @patch('builtins.input', side_effect=[True, '', '', '', 0])
    def test_boolean(self, mock_input) -> None:
        '''Test for boolean input value''' 
        p3 = Property()
        with self.assertRaises(ValueError):
            p3.set_address()       

    # testcase 4
    @patch('builtins.input', side_effect=['String', '', '', '', 0])
    def test_string(self, mock_input) -> None:
        '''Test for string input value'''                
        p4 = Property()
        with self.assertRaises(ValueError):
            p4.set_address()       
        
if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetAddress))
    unittest.TextTestRunner().run(suite)