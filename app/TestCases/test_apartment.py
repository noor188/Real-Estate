import unittest
from app.apartment import Apartment
from unittest.mock import patch

class TestSetBalcony(unittest.TestCase):

    # testcase 1
    def test_yes(self) -> None:
        '''Test for 'Yes' input value'''  
        p1 = Apartment(None, None, None)   
        p1.balcony = "Yes"    
        self.assertEqual(p1.balcony, "Yes")
    
    # testcase 2
    def test_no(self) -> None:
        '''Test for 'No' input value'''  
        p1 = Apartment(None, None, None)   
        p1.balcony = "No"    
        self.assertEqual(p1.balcony, "No")
  

class TestSetSquareFootage(unittest.TestCase):
    
    # testcase 1
    @patch('builtins.input', side_effect=[6573])
    def test_state_number(self, mock_input) -> None:
        '''Test for number input value''' 
        p1 = Property()  
        p1.set_square_footage()
        self.assertEqual(p1.get_square_footage(), 6573)         

    # testcase 2
    @patch('builtins.input', side_effect=["6573"])
    def test_state_str(self, mock_input) -> None:
        '''Test for string input value''' 
        p2 = Property()
        with self.assertRaises(ValueError):
            p2.set_square_footage()
    
    # testcase 3
    @patch('builtins.input', side_effect=[True])
    def test_state_boolean(self, mock_input) -> None:
        '''Test for boolean input value''' 
        p3 = Property()
        with self.assertRaises(ValueError):
            p3.set_square_footage()


class TestSetNumberOfBedrooms(unittest.TestCase):

    # testcase 1
    @patch('builtins.input', side_effect=[3])
    def test_zip_int(self, mock_input) -> None:
        '''Test for int input value'''  
        p1 = Property()        
        p1.set_num_of_bedrooms()         
        self.assertEqual(p1.get_num_of_bedrooms(), 3)

    # testcase 2
    @patch('builtins.input', side_effect=[3.5])
    def test_float(self, mock_input) -> None:
        '''Test for float input value''' 
        p2 = Property()             
        with self.assertRaises(TypeError):
            p2.set_num_of_bedrooms()

    # testcase 3
    @patch('builtins.input', side_effect=[True])
    def test_boolean(self, mock_input) -> None:
        '''Test for boolean input value''' 
        p3 = Property()
        with self.assertRaises(ValueError):
            p3.set_num_of_bedrooms()       

    # testcase 4
    @patch('builtins.input', side_effect=["3.5"])
    def test_zip_string(self, mock_input) -> None:
        '''Test for string input value'''                
        p4 = Property()
        with self.assertRaises(ValueError):
            p4.set_num_of_bedrooms()  


class TestSetNumberOfBathrooms(unittest.TestCase):

    # testcase 1
    @patch('builtins.input', side_effect=[3])
    def test_zip_int(self, mock_input) -> None:
        '''Test for int input value'''  
        p1 = Property()        
        p1.set_num_of_bathrooms()         
        self.assertEqual(p1.get_num_of_bathrooms(), 3)

    # testcase 2
    @patch('builtins.input', side_effect=[3.5])
    def test_float(self, mock_input) -> None:
        '''Test for float input value''' 
        p2 = Property()             
        with self.assertRaises(TypeError):
            p2.set_num_of_bathrooms()

    # testcase 3
    @patch('builtins.input', side_effect=[True])
    def test_boolean(self, mock_input) -> None:
        '''Test for boolean input value''' 
        p3 = Property()
        with self.assertRaises(ValueError):
            p3.set_num_of_bathrooms()       

    # testcase 4
    @patch('builtins.input', side_effect=["3.5"])
    def test_zip_string(self, mock_input) -> None:
        '''Test for string input value'''                
        p4 = Property()
        with self.assertRaises(ValueError):
            p4.set_num_of_bathrooms()  
    
            
class TestSetStatus(unittest.TestCase):
    status = ('available', 'rented', 'sold')

    # testcase 1
    @patch('builtins.input', side_effect=['available'])
    def test_right_value(self, mock_input) -> None:
        '''Test for right input value'''  
        p1 = Property()        
        p1.set_status()         
        self.assertEqual(p1.get_status(), 'available')

    # testcase 2
    @patch('builtins.input', side_effect=['None'])
    def test_wrong_input(self, mock_input) -> None:
        '''Test for wrong input value'''                
        p1 = Property()
        with self.assertRaises(ValueError):
            p1.set_status() 

class TestMarkAsSold(unittest.TestCase):
    
    # testcase 1    
    def test_right_value(self) -> None:
        '''Test for right input value'''  
        p1 = Property()        
        p1.mark_as_sold()         
        self.assertEqual(p1.status, 'sold')

class TestMarkAsRented(unittest.TestCase):
    
    # testcase 1    
    def test_right_value(self) -> None:
        '''Test for right input value'''  
        p1 = Property()        
        p1.mark_as_rented()         
        self.assertEqual(p1.status, 'rented')

class TestMarkAsAvailable(unittest.TestCase):
    
    # testcase 1    
    def test_right_value(self) -> None:
        '''Test for right input value'''  
        p1 = Property()        
        p1.mark_as_available()         
        self.assertEqual(p1.status, 'available')


        
if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetBalcony))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetSquareFootage))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetNumberOfBedrooms))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetNumberOfBathrooms))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMarkAsSold))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMarkAsRented))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMarkAsAvailable))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetStatus))
    unittest.TextTestRunner().run(suite)