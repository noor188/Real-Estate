from app.property import Property
## Stores data for an Apartment that is a Property

## =================
## Constants:



## =================
## Data definitions

class Apartment(Property):  
        
    def __init__(self, balcony, rentable_storage_unit, fully_renovated_house):
        self._balcony               = balcony
        self._rentable_storage_unit = rentable_storage_unit
        self._fully_renovated_house = fully_renovated_house
    
    @property
    def balcony(self) -> str:
        '''
        Returns:
        str : balcony status
        One of: Yes, No
        ''' #TODO
        return self._balcony

    @balcony.setter
    def balcony(self, value: str)-> None:
        '''
        assign the Apartment balcony status

        Parameters:
        balcony (str): one of: Yes, No
        ''' #TODO           
        self._balcony = value
    
    @property
    def rentable_storage_unit(self) -> bool:
        '''
        Returns:
        bool : rentable storage status
        ''' #TODO
        return self._rentable_storage_unit

    @rentable_storage_unit.setter
    def rentable_storage_unit(self, value: bool) -> None:
        '''
        assign the Apartment rentable storage unit status

        Parameters:
        rentable_storage_unit (bool): one of: Yes, No
        ''' #TODO  
        self._rentable_storage_unit = value

    @property
    def fully_renovated_house(self) -> bool:
        '''
        Returns:
        bool : renovated house status
        ''' #TODO
        return self._fully_renovated_house

    @fully_renovated_house.setter
    def fully_renovated_house(self, value: bool) -> None:
        '''
        assign the Apartment renovate status

        Parameters:
        fully_renovated_house (bool): one of: Yes, No
        ''' #TODO          
        self._fully_renovated_house = value
   
   
    ## =================
    ## Methods:   

    def display(self) -> None:
        '''
        Displays the Apartment attributes

        Returns: None
        ''' 
        print("APARTMENT DETAILS")
        print("=================")
        print("balcony: {}".format(self._balcony))
        print("rentable storage unit: {}".format(self._rentable_storage_unit))
        print("fully renovated house: {}".format(self._fully_renovated_house))
        print()

    @staticmethod
    def prompt_init() -> dict:
        '''
        uses python dict constructor to create a dictionary
        of values that can be passed into __init__. The value
        for each key is prompted with a call to input.

        Returns:
        dict: dictionary of Apartment __init__ arguments values 
        ''' #TODO
        return 


