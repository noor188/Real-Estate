## Design and test property methods

## ===============================
## imports
import unittest
import sys 
from app.property import Property

## ====================
## functions

## Object squareFootage numofBedrooms numofBathrooms -> None
## Initializes an object instance of the Property class

class PropertyTest: # stub
    def __init__(self, squareFootage, numofBedrooms, numofBathrooms):
        self.squareFootage  = 0
        self.numofBedrooms  = 1
        self.numofBathrooms = 1

class testinitMethod(unittest.TestCase):

    #1 Test case for valid values 
    def test_valid_values(self):
        squareFootage, numofBedrooms, numofBathrooms = 245.7, 4, 3
        property = PropertyTest(squareFootage, numofBedrooms, numofBathrooms)  
        self.assertEqual(property.squareFootage,  squareFootage ) 
        self.assertEqual(property.numofBedrooms,  numofBedrooms ) 
        self.assertEqual(property.numofBathrooms, numofBathrooms) 

    #2 Test case for negative values
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            PropertyTest(-100, 3, 2) # negative squareFootage

    #3 Test case for string values
    #4 Test case for float values
    #5 Test case for missing or incomplete input

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




    


