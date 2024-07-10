''' Stores data for a property'''
## =================
## Constants:

## =================
## Data definitions

class Property:
    '''Creates a property with information describing it.'''
    
    # store the next available id for all properties
    Propert_ID = 0
    
    def __init__(self, address, square_footage, num_of_bedrooms, num_of_bathrooms):
        self.set_id( )
        self.set_address(address)
        self.set_square_footage(square_footage)
        self.set_num_of_bedrooms(num_of_bedrooms)
        self.set_num_of_bathrooms(num_of_bathrooms)
        self.status           = 'Available'
        
    def set_id(self) -> None:
        '''
        Automatically set the properties unique id.

        Parameters: 
        None
        ''' #TODO
        Property.Propert_ID += 1
        
    
    def set_address(self, address):
        '''
        assign the properties address

        Parameters:
        address (str) : The address of the property        
        ''' #TODO
        pass

    def set_square_footage(self, square_footage):
        '''
        assign the properties square footage

        Parameters:
        square_footage (float) : the square footage of a property
        ''' #TODO
        pass

    def set_num_of_bedrooms(self, num_of_bedrooms):
        '''
        assign the properties number of bedrooms

        Parameters:
        num_of_bedrooms (int)
        ''' #TODO
        pass

    def set_num_of_bathrooms(self, num_of_bathrooms):
        '''
        assign the properties number of bathrooms

        Parameters:
        num_of_bathrooms (int)
        ''' #TODO
        pass

    def set_status(self, status):
        '''
        assign the properties status

        Parameters:
        status (string) : one of: Available (default), Rented, sold        
        ''' #TODO
        return 'Available'

    def get_id(self):
        '''
        Returns: 
        int: assigned properites id
        ''' #TODO
        return 0
    
    def get_address(self) -> str:
        '''
        Returns:
        str: assigned properties address
        '''
        return ''

    def get_square_footage(self) -> float:
        '''        
        Returns:
        float: the assigned square footage value
        ''' #TODO
        return 0

    def get_num_of_bedrooms(self) -> int:
        '''     
        Returns:
        int: assigned number of bedrooms
        ''' #TODO
        pass
        

    def get_num_of_bathrooms(self) -> int:
        '''
        Returns:
        int: assigned number of bathrooms
        ''' #TODO
        pass

    def get_status(self):
        '''
        Returns:
        one of: Available (default), Rented, sold
        ''' #TODO
        pass

    ## =================
    ## Methods:
    def mark_as_sold(self) -> None:
        '''
        marks a property as sold

        Returns: None
        ''' #TODO
        pass

    def mark_as_rented(self) -> None:
        '''
        mark a property as rented

        Returns: None
        ''' #TODO
        pass

    def display(self) -> None:
        '''
        Displays the properties attributes

        Returns: None
        ''' #TODO
        pass

    @staticmethod
    def prompt_init() -> dict:
        '''
        uses python dict constructor to create a dictionary
        of values that can be passed into __init__. The value
        for each key is prompted with a call to input.

        Returns:
        dict: dictionary of Property __init__ arguments values 
        ''' #TODO
        pass


