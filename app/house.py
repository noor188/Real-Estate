from property import Property
## Stores data for a House that is a Property

## =================
## Constants:



## =================
## Data definitions

class House(Property):  
        
    def __init__(self, parking, private_pool, exterior_features):
        self.parking, self.private_pool, exterior_features = None, None, None
        self.set_parking(parking)
        self.set_private_pool(private_pool)
        self.set_exterior_features(exterior_features)
           
    def set_parking(self, parking) -> None: 
        '''
        assign the House parking status

        Parameters:
        parking (str): one of: Yes, No
        ''' #TODO       
        pass
    
    def set_private_pool(self, private_pool) -> None:
        '''
        assign the House private pool status

        Parameters:
        private_pool (str): one of: Yes, No
        ''' #TODO
        pass

    def set_exterior_features(self, exterior_features) -> None:
        '''
        assign House exterior features 

        Parameters:
        exterior_features (str): Value is prompted with a call to input
        ''' #TODO
        pass

    def get_parking(self) -> str:
        '''
        Returns:
        str : parking status
        ''' #TODO
        pass
    
    def get_private_pool(self) -> str:
        '''
        Returns:
        str : private_pool status
        ''' #TODO
        pass

    def get_exterior_features(self) -> str:
        '''
        Returns:
        str : house exterior features
        ''' #TODO
        pass

   
    ## =================
    ## Methods:   

    def display(self) -> None:
        '''
        Display the House attributes        
        ''' #TODO
        pass

    @staticmethod
    def prompt_init() -> dict:
        '''
        uses python dict constructor to create a dictionary
        of values that can be passed into __init__. The value
        for each key is prompted with a call to input.

        Returns:
        dict: dictionary of House __init__ arguments values 
        ''' #TODO
        pass


