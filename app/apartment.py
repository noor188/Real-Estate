from property import Property
## Stores data for an Apartment that is a Property

## =================
## Constants:



## =================
## Data definitions

class Apartment(Property):  
        
    def __init__(self, balcony, rentable_storage_unit, fully_renovated_house):
        self.balcony, self.rentable_storage_unit, self.fully_renovated_house = None, None, None
        self.set_balcony(balcony)
        self.set_rentable_storage_unit(rentable_storage_unit)
        self.set_fully_renovated_house(fully_renovated_house)
           
    def set_balcony(self, balcony: bool)-> None:
        '''
        assign the Apartment balcony status

        Parameters:
        balcony (bool): one of: Yes, No
        ''' #TODO           
        pass
    
    def set_rentable_storage_unit(self, rentable_storage_unit: bool) -> None:
        '''
        assign the Apartment rentable storage unit status

        Parameters:
        rentable_storage_unit (bool): one of: Yes, No
        ''' #TODO  
        pass

    def set_fully_renovated_house(self, fully_renovated_house: bool) -> None:
        '''
        assign the Apartment renovate status

        Parameters:
        fully_renovated_house (bool): one of: Yes, No
        ''' #TODO          
        pass

    def get_balcony(self) -> bool:
        '''
        Returns:
        bool : balcony status
        ''' #TODO
        pass
    
    def get_rentable_storage_unit(self) -> bool:
        '''
        Returns:
        bool : rentable storage status
        ''' #TODO
        pass

    def get_fully_renovated_house(self) -> bool:
        '''
        Returns:
        bool : renovated house status
        ''' #TODO
        pass

   
    ## =================
    ## Methods:   

    def display(self) -> None:
        '''
        Display the Apartment attributes        
        ''' #TODO
        pass

    @staticmethod
    def prompt_init() -> dict:
        '''
        uses python dict constructor to create a dictionary
        of values that can be passed into __init__. The value
        for each key is prompted with a call to input.

        Returns:
        dict: dictionary of Apartment __init__ arguments values 
        ''' #TODO
        pass


