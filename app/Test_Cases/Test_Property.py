## ===============================
## imports
import unittest
import sys 
from io import StringIO
from app.property import Property

## Design and test property methods

## ====================
## functions

## Object squareFootage numofBedrooms numofBathrooms -> None
## Initializes an object instance of the Property class

class testinitMethod(unittest.TestCase):

    #1 Test case for valid values 
    def test_valid_values(self):
        squarefootage, numofBedrooms, numofBathrooms = 245.7, 4, 3
        property = Property(squarefootage, numofBedrooms, numofBathrooms)  
        self.assertEqual(property.squarefootage.value,  squarefootage ) 
        self.assertEqual(property.numofBedrooms.value,  numofBedrooms ) 
        self.assertEqual(property.numofBathrooms.value, numofBathrooms) 

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
        self.assertEqual(property.squarefootage.value ,  squareFootage ) 
        self.assertEqual(property.numofBedrooms.value ,  0) 
        self.assertEqual(property.numofBathrooms.value, 1) 

    #5 Test case for out of limit values    ValueError
    def test_boolean_values(self):
        with self.assertRaises(ValueError):
            Property(245.5, 100, 0)     

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





    


