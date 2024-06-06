## ===============================
## imports
from app.Data_Definitions.Data import SquareFootage, NumofBedrooms, NumofBathrooms

## ===============================
## Classes
    
class Property: 
        ## ====================
        ## Data/ Attributes
        '''
        squareFootage
        numofBedrooms
        numofBathrooms    
        '''        
        def __init__(self, squarefoot= 0, numofBed= 0, numofBath= 1) -> None:
            self.squarefoot     = SquareFootage(squarefoot)
            self.numofBed       = NumofBedrooms(numofBed)   
            self.numofBath      = NumofBathrooms(numofBath)

        ## ====================
        ## functions                 

        def get_squareFootage(self):
            return self.squarefoot.value

        def get_numofBedrooms(self):
            return self.numofBed.value

        def get_numofBathrooms(self):
            return self.numofBath.value
        
        def display(self) -> None:            
            print("## ======== ##")
            print("Properties Characterisitcs:")
            print("Square Footage: {}".format(self.squareFootage) )
            print("Num of bedrooms: {}".format(self.numofBedrooms))
            print("Num of bathrooms: {}".format(self.numofBathrooms))

        def prompinit():
            pass    