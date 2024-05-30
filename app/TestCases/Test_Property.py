## Design and test properties methods

## ===============================
## imports
import unittest
import sys 
from app.property import Property

## ====================
## functions

## Object -> None
## display the property characteristic

def display(obj): # stub
    print(" ")
    
class testDisplayFunction(unittest.TestCase):

    # 1
    def test_display(self):
        p1 = Property(200.0, 3, 2)
        result = display(Property)
        self.assertEqual(result, (print("## ====================\n"), print(" Square Footage: ", p1.squareFootage, end="\n"), print("Num of Bedrooms: ", p1.numofBedrooms, end="\n"), print("Num of Bathrooms: ", p1.numofBathrooms, end="\n") ))

if __name__ == "__main__":
    unittest.main()




    


