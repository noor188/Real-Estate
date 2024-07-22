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
    def test_int(self, mock_input) -> None:
        '''Test for int input value'''  
        p1 = Property()        
        p1.set_address()
        expected = {'street_number': 6573, 'street_name': '', 'county': '', 'state': '', 'zip_code': 0}     
        self.assertEqual(p1.get_address(), expected)

    # testcase 2
    @patch('builtins.input', side_effect=[6.573, '', '', '', 0])
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

    # street name

    # testcase 1
    @patch('builtins.input', side_effect=[6573, 'steet name', '', '', 0])
    def test_name_str(self, mock_input) -> None:
        '''Test for int input value'''  
        p1 = Property()        
        p1.set_address()
        expected = {'street_number': 6573, 'street_name': 'steet name', 'county': '', 'state': '', 'zip_code': 0}     
        self.assertEqual(p1.get_address(), expected)

    # testcase 2
    @patch('builtins.input', side_effect=[6573, 25, '', '', 0])
    def test_name_number(self, mock_input) -> None:
        '''Test for number input value''' 
        p2 = Property()             
        with self.assertRaises(ValueError):
            p2.set_address() # float numofBedrooms numofBathrooms        

    # testcase 3
    @patch('builtins.input', side_effect=[6573, True, '', '', 0])
    def test_name_boolean(self, mock_input) -> None:
        '''Test for boolean input value''' 
        p3 = Property()
        with self.assertRaises(ValueError):
            p3.set_address()   

    # county

    # testcase 1
    @patch('builtins.input', side_effect=[6573, 'steet name', 'El Paso', '', 0])
    def test_county_str(self, mock_input) -> None:
        '''Test for int input value'''  
        p1 = Property()        
        p1.set_address()
        expected = {'street_number': 6573, 'street_name': 'steet name', 'county': 'El Paso', 'state': '', 'zip_code': 0}     
        self.assertEqual(p1.get_address(), expected)

    # testcase 2
    @patch('builtins.input', side_effect=[6573, 'steet name', 35, '', 0])
    def test_county_number(self, mock_input) -> None:
        '''Test for number input value''' 
        p2 = Property()             
        with self.assertRaises(ValueError):
            p2.set_address() # float numofBedrooms numofBathrooms        

    # testcase 3
    @patch('builtins.input', side_effect=[6573, 'steet name', True, '', 0])
    def test_county_boolean(self, mock_input) -> None:
        '''Test for boolean input value''' 
        p3 = Property()
        with self.assertRaises(ValueError):
            p3.set_address()   

    # state

    # testcase 1
    @patch('builtins.input', side_effect=[6573, 'steet name', 'El Paso', 'Tx', 0])
    def test_state_str(self, mock_input) -> None:
        '''Test for int input value'''  
        p1 = Property()        
        p1.set_address()
        expected = {'street_number': 6573, 'street_name': 'steet name', 'county': 'El Paso', 'state': 'Tx', 'zip_code': 0}     
        self.assertEqual(p1.get_address(), expected)

    # testcase 2
    @patch('builtins.input', side_effect=[6573, 'steet name', 'El Paso', 35, 0])
    def test_state_number(self, mock_input) -> None:
        '''Test for number input value''' 
        p2 = Property()             
        with self.assertRaises(ValueError):
            p2.set_address() # float numofBedrooms numofBathrooms        

    # testcase 3
    @patch('builtins.input', side_effect=[6573, 'steet name', 'El Paso', True, 0])
    def test_state_boolean(self, mock_input) -> None:
        '''Test for boolean input value''' 
        p3 = Property()
        with self.assertRaises(ValueError):
            p3.set_address()   



    
        
if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetAddress))
    unittest.TextTestRunner().run(suite)