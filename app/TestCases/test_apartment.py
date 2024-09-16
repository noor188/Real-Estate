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

class TestSetRentableStorageUnit(unittest.TestCase):

    # testcase 1
    def test_yes(self) -> None:
        '''Test for 'Yes' input value'''  
        p1 = Apartment(None, None, None)   
        p1.rentable_storage_unit = "Yes"    
        self.assertEqual(p1.rentable_storage_unit, "Yes")
    
    # testcase 2
    def test_no(self) -> None:
        '''Test for 'No' input value'''  
        p1 = Apartment(None, None, None)   
        p1.rentable_storage_unit = "No"    
        self.assertEqual(p1.rentable_storage_unit, "No")

class TestSetFullyRenovatedHouse(unittest.TestCase):

    # testcase 1
    def test_yes(self) -> None:
        '''Test for 'Yes' input value'''  
        p1 = Apartment(None, None, None)   
        p1.fully_renovated_house = "Yes"    
        self.assertEqual(p1.fully_renovated_house, "Yes")
    
    # testcase 2
    def test_no(self) -> None:
        '''Test for 'No' input value'''  
        p1 = Apartment(None, None, None)   
        p1.fully_renovated_house = "No"    
        self.assertEqual(p1.fully_renovated_house, "No")
  

        
if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetBalcony))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetRentableStorageUnit))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetFullyRenovatedHouse))
    unittest.TextTestRunner().run(suite)