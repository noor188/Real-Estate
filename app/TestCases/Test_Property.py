## Design and test property methods

## ===============================
## imports
import unittest
import sys 
#from app.property import Property

## ====================
## functions

## Object squareFootage numofBedrooms numofBathrooms -> None
## Initializes an object instance of the Property class
""" 
class Property: # stub
    def __init__(self, squareFootage: float, numofBedrooms: int = 0, numofBathrooms: int= 1) -> None:
        self.squareFootage  = 0
        self.numofBedrooms  = 0
        self.numofBathrooms = 1 """

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

## <template for Data.py>

class Property: # stub
    def __init__(self, squareFootage: float, numofBedrooms: int = 0, numofBathrooms: int= 1) -> None:
        self.set_squareFootage(squareFootage)
        self.numofBedrooms  = numofBedrooms
        self.numofBathrooms = numofBathrooms      

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

## ====================

## Object -> None
## display the property characteristic

def display(obj): # stub
    print(" ")
    
""" class testDisplayMethod(unittest.TestCase):

    # 1
    def test_display(self):
        p1 = Property(200.0, 3, 2)
        result = display(Property)
        self.assertEqual(result, (print("## ====================\n"), print(" Square Footage: ", p1.squareFootage, end="\n"), print("Num of Bedrooms: ", p1.numofBedrooms, end="\n"), print("Num of Bathrooms: ", p1.numofBathrooms, end="\n") ))
 """
if __name__ == "__main__":
    unittest.main()




    


