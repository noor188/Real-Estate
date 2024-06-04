## ===============================
## imports
import unittest
import sys 
from io import StringIO
#from app.property import Property

## Design and test property methods

## ====================
## functions

## Object squareFootage numofBedrooms numofBathrooms -> None
## Initializes an object instance of the Property class

class testinitMethod(unittest.TestCase):

    #1 Test case for valid values 
    def test_valid_values(self):
        squareFootage, numofBedrooms, numofBathrooms = 245.7, 4, 3
        property = Property(squareFootage, numofBedrooms, numofBathrooms)  
        self.assertEqual(property.squareFootage,  squareFootage ) 
        self.assertEqual(property.numofBedrooms,  numofBedrooms ) 
        self.assertEqual(property.numofBathrooms, numofBathrooms) 

    #2 Test case for negative values
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            Property(-100, 3, 2) # negative squareFootage

    #3 Test case for string  values
    def test_string_values(self):
        with self.assertRaises(TypeError):
            Property("a", "b", "c")
    
    #4 Test case for float values 
    def test_float_values(self):
        with self.assertRaises(TypeError):
            Property(245.7, 2.5, 4.6) # float numofBedrooms numofBathrooms

    #5 Test case for boolean values    TypeError
    def test_boolean_values(self):
        with self.assertRaises(TypeError):
            Property(False, True, True)
            
    #6 Test case for missing or incomplete input 
    def test_missing_values(self):
        squareFootage= 245.7
        property = Property(squareFootage)  
        self.assertEqual(property.squareFootage,  squareFootage ) 
        self.assertEqual(property.numofBedrooms,  0) 
        self.assertEqual(property.numofBathrooms, 1) 

    #5 Test case for out of limit values    ValueError
    def test_boolean_values(self):
        with self.assertRaises(ValueError):
            Property(245.5, 100, 0)

## <template for Data.py>

class Property: # stub
    def __init__(self, squareFootage: float = 0, numofBedrooms: int = 0, numofBathrooms: int= 1) -> None:
        self.set_squareFootage (squareFootage)
        self.set_numofBedrooms (numofBedrooms)        
        self.set_numofBathrooms(numofBathrooms)      

    def set_squareFootage(self, squareFootage):
        
        try:
            if isinstance(squareFootage, str) or isinstance(squareFootage, bool): # string or boolean
                raise TypeError
            if squareFootage < 0 : # neg
                raise ValueError    
        except TypeError: # loggin the error, notifying the user, reverting to a defult value or other appropriate actions 
            raise TypeError
        except ValueError:
            raise ValueError 
        else:
            self.squareFootage = squareFootage
    
    def set_numofBedrooms(self, numofBedrooms):
        
        try:
            if isinstance(numofBedrooms, str) or isinstance(numofBedrooms, bool) or isinstance(numofBedrooms, float): # string or boolean
                raise TypeError
            if numofBedrooms < 0 or 10 < numofBedrooms: # neg, out of bound
                raise ValueError    
        except TypeError: # loggin the error, notifying the user, reverting to a defult value or other appropriate actions 
            raise TypeError
        except ValueError:
            raise ValueError 
        else:
            self.numofBedrooms = numofBedrooms
    
    def set_numofBathrooms(self, numofBathrooms):
        
        try:
            if isinstance(numofBathrooms, str) or isinstance(numofBathrooms, bool) or isinstance(numofBathrooms, float): # string or boolean
                raise TypeError
            if numofBathrooms < 1 or 10 < numofBathrooms: # neg or out of bound
                raise ValueError    
        except TypeError: # loggin the error, notifying the user, reverting to a defult value or other appropriate actions 
            raise TypeError
        except ValueError:
            raise ValueError 
        else:
            self.numofBathrooms = numofBathrooms
    
    def display(self) -> None:
        ## ... self
        print("## ======== ##")
        print("Properties Characterisitcs:")
        print("Square Footage: {}".format(self.squareFootage) )
        print("Num of bedrooms: {}".format(self.numofBedrooms))
        print("Num of bathrooms: {}".format(self.numofBathrooms))  
       

## ====================

## Object -> String
## Display the property characteristic (squareFootage, numofBedrooms, numofBathrooms)
    

class testDisplayMethod(unittest.TestCase):
    
    #1 
    def test_case_one(self):
        p1 = Property(245.5, 3, 2)
        captrued_output = StringIO()
        sys.stdout      = captrued_output
        p1.display()
        sys.stdout = sys.__stdout__
        captured_output_value = captrued_output.getvalue()
        self.assertEqual(captured_output_value, "## ======== ##\nProperties Characterisitcs:\nSquare Footage: {}\nNum of bedrooms: {}\nNum of bathrooms: {}\n".format(p1.squareFootage, p1.numofBedrooms, p1.numofBathrooms))

    #2
    def test_case_two(self):
        p1 = Property(601.9, 4, 3)
        captrued_output = StringIO()
        sys.stdout      = captrued_output
        p1.display()
        sys.stdout = sys.__stdout__
        captured_output_value = captrued_output.getvalue()
        self.assertEqual(captured_output_value, "## ======== ##\nProperties Characterisitcs:\nSquare Footage: {}\nNum of bedrooms: {}\nNum of bathrooms: {}\n".format(p1.squareFootage, p1.numofBedrooms, p1.numofBathrooms))

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    # test __init__ 
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testinitMethod))
    # test display method
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testDisplayMethod))
    unittest.TextTestRunner().run(suite)





    


