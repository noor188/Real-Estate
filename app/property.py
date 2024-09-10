''' Stores data for a property'''
from app.error import validators
## =================
## Constants:

## =================
## Data definitions

class Property:
    '''Creates a property with information describing it.'''
    
    # store the next available id for all properties
    Propert_ID = 0
    
    def __init__(self, address, square_footage, num_of_bedrooms, num_of_bathrooms):         
        self.id               = self.set_id()
        self.address          = address
        self.square_footage   = square_footage
        self.num_of_bedrooms  = num_of_bedrooms
        self.num_of_bathrooms = num_of_bathrooms
        self.status           = 'Available'

    def get_id(self) -> int:
        '''
        Returns: 
        int: assigned properites id
        ''' 
        return self.id
     
    def set_id(self) -> int:
        '''
        Automatically set the properties unique id.

        Parameters: 
        None
        '''
        Property.Propert_ID += 1
        self.id = Property.Propert_ID
        return self.id
    
    @property
    def address(self) -> dict:
        '''
        Returns:
        dict:  dictionary of Property address values 
        '''
        return self.address

    @address.setter  
    def address(self) -> None:
        '''
        assign the properties address

        Parameters:
        address (str) : The address of the property        
        '''        
        street_number   = validators.validate_street_number(input("Enter street number: "))
        street_name     = validators.validate_street_name(input("Enter street name: "))
        county          = validators.validate_county(input("Enter county: "))
        state           = validators.validate_state(input("Enter state: "))
        zip_code        = validators.validate_zip_code(input("Enter zip code: "))

        self.address = dict(street_number= street_number,
                            street_name  = street_name,
                            county       = county,
                            state        = state,
                            zip_code     = zip_code) 

    @property
    def square_footage(self) -> float:
        '''        
        Returns:
        float: the assigned square footage value
        '''
        return self.square_footage

    @square_footage.setter
    def square_footage(self) -> None:
        '''
        assign the properties square footage        
        ''' 
        self.square_footage = validators.validate_square_footage(input("Enter Square Footage"))

    @property
    def num_of_bedrooms(self) -> int:
        '''     
        Returns:
        int: assigned number of bedrooms
        ''' 
        return self.num_of_bathrooms
    
    @num_of_bedrooms.setter
    def num_of_bedrooms(self, num_of_bedrooms):
        '''
        assign the properties number of bedrooms

        Parameters:
        num_of_bedrooms (int)
        ''' 
        self.num_of_bedrooms = validators.validate_num_of_bedrooms(input("Enter number of bedrooms"))

    @property
    def num_of_bathrooms(self) -> int:
        '''
        Returns:
        int: assigned number of bathrooms
        '''
        return self.num_of_bathrooms
    
    @num_of_bathrooms.setter
    def num_of_bathrooms(self) -> None:
        '''
        assign the properties number of bathrooms

        Parameters:
        num_of_bathrooms (int)
        ''' 
        self.num_of_bathrooms = validators.validate_num_of_bathrooms(input("Enter number of bathrooms"))

    @property
    def status(self) -> str:
        '''
        Returns:
        one of: Available (default), Rented, sold
        ''' 
        return self.status
    
    @status.setter
    def status(self) -> None:
        '''
        assign the properties status
        
        one of: Available (default), Rented, sold        
        '''
        return 'available'
    
    ## =================
    ## Methods:
    def mark_as_sold(self) -> None:
        '''
        marks a property as sold
        status = 'sold'

        Returns: None
        ''' 
        self.status = 'sold'

    def mark_as_rented(self) -> None:
        '''
        mark a property as rented

        Returns: None
        ''' 
        self.status = 'rented'
    
    def mark_as_available(self) -> None:
        '''
        mark a property as available

        Returns: None
        '''
        self.status = 'available'

    def display(self) -> None:
        '''
        Displays the properties attributes

        Returns: None
        ''' 
        print("PROPERTY DETAILS")
        print("=================")
        print("square footage: {}".format(self.square_footage))
        print("bedrooms: {}".format(self.num_of_bedrooms))
        print("bathrooms: {}".format(self.num_of_bathrooms))
        print()

    @staticmethod
    def prompt_init() -> dict:
        '''
        uses python dict constructor to create a dictionary
        of values that can be passed into __init__. The value
        for each key is prompted with a call to input.

        Returns:
        dict: dictionary of Property __init__ arguments values 
        ''' #TODO
        return ''