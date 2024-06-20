from property import Property
## Stores data for a House that is a Property

## =================
## Constants:



## =================
## Data definitions

class House(Property):  
        
    def __init__(self, parking, private_pool, exterior_features):
        self.PARKING             = self.set_parking(parking)
        self.PRIVATE_POOL        = self.set_private_pool(private_pool)
        self.EXTERIOR_FEATURES   = self.set_exterior_features(exterior_features)
           
    def set_parking(self, parking):        
        pass
    
    def set_private_pool(self, private_pool):
        pass

    def set_exterior_features(self, exterior_features):
        pass

    def get_parking(self):
        pass
    
    def get_private_pool(self):
        pass

    def get_exterior_features(self):
        pass

   
    ## =================
    ## Methods:   

    def display(self):
        pass

    @staticmethod
    def prompt_init():
        pass


