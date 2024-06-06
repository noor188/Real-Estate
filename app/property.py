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
        def __init__(self, squarefootage= 0, numofBedrooms= 0, numofBathrooms= 1) -> None:
            self.squarefootage  = SquareFootage(squarefootage)
            self.numofBedrooms  = NumofBedrooms(numofBedrooms)   
            self.numofBathrooms = NumofBathrooms(numofBathrooms)    

        ## ====================
        ## functions 
                
        def get_squareFootage(self):
            return self.squarefootage.value

        def get_numofBedrooms(self):
            return self.numofBedrooms.value

        def get_numofBathrooms(self):
            return self.numofBathrooms.value
        
        def display(self) -> None:            
            print("## ======== ##")
            print("Properties Characterisitcs:")
            print("Square Footage: {}".format(self.squareFootage) )
            print("Num of bedrooms: {}".format(self.numofBedrooms))
            print("Num of bathrooms: {}".format(self.numofBathrooms))

        def prompinit():
            pass    