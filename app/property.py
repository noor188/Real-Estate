## Stores data for a property 

## =================
## Constants:



## =================
## Data definitions

class Property:  
    # store the next available id for all properties
    Propert_ID = 0  
    
    def __init__(self, id, address, square_footage, num_of_bedrooms, num_of_bathrooms):
        self.ID               = self.set_id(id)
        self.ADDRESS          = self.set_address(address)
        self.SQUARE_FOOTAGE   = self.set_square_footage(square_footage)
        self.NUM_OF_BEDROOMS  = self.set_num_of_bedrooms(num_of_bedrooms)
        self.NUM_OF_BATHROOMS = self.set_num_of_bathrooms(num_of_bathrooms)
        self.Status           = 'Available' 
    
    def set_id(self, id):        
        Propert.Propert_ID += 1
    
    def set_address(self, address):
        pass

    def set_square_footage(self, square_footage):
        pass

    def set_num_of_bedrooms(self, num_of_bedrooms):
        pass

    def set_num_of_bathrooms(self, num_of_bathrooms):
        pass

    def set_status(self, status):
        pass

    def get_id(self):
        pass
    
    def get_address(self):
        pass

    def get_square_footage(self):
        pass

    def get_num_of_bedrooms(self):
        pass

    def get_num_of_bathrooms(self):
        pass

    def get_status(self):
        pass

    ## =================
    ## Methods:
    def mark_as_sold(self):
        pass

    def mark_as_rented(self):
        pass

    def display(self):
        pass

    @staticmethod
    def prompt_init():
        pass


