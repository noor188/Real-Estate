from property import Property
## Stores data for an Apartment that is a Property

## =================
## Constants:



## =================
## Data definitions

class Apartment(Property):  
        
    def __init__(self, balcony, rentable_storage_unit, fully_renovated_house):
        self.BALCONY               = self.set_balcony(balcony)
        self.RENTABLE_STORAGE_UNIT = self.set_rentable_storage_unit(rentable_storage_unit)
        self.FULLY_RENOVATED_HOUSE = self.set_fully_renovated_house(fully_renovated_house)
           
    def set_balcony(self, balcony):        
        pass
    
    def set_rentable_storage_unit(self, rentable_storage_unit):
        pass

    def set_fully_renovated_house(self, fully_renovated_house):
        pass

    def get_balcony(self):
        pass
    
    def get_rentable_storage_unit(self):
        pass

    def get_fully_renovated_house(self):
        pass

   
    ## =================
    ## Methods:   

    def display(self):
        pass

    @staticmethod
    def prompt_init():
        pass


