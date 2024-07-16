#TODO 
# handle exceptions
from property import Property
## Allows an agent to manage properties  

## =================
## Constants:



## =================
## Data definitions

class Agent:  
        
    def __init__(self, id, name, contact_details):
        self.id, self.name, self.contact_details = None, None, None
        self.set_id(id)
        self.set_name(name)
        self.set_contact_details(contact_details)
        self.properties      = list() # composition
           
    def set_id(self, id: int) -> None:
        '''
        assign the Agent ID

        Parameters:
        id (int): Agent ID
        ''' #TODO             
        pass
    
    def set_name(self, name: str) -> None:
        '''
        assign the Agent name

        Parameters:
        name (str): Agent name
        ''' #TODO    
        pass

    def set_contact_details(self, contact_details: dict) -> None:
        '''
        assign the Agent contact details

        Parameters:
        contact_details (dict): Agent contact details
        ''' #TODO   
        pass

    def get_id(self) -> int:
        '''
        Returns:
        int : Agent ID
        ''' #TODO
        pass
    
    def get_name(self) -> str:
        '''
        Returns:
        str : Agent name
        ''' #TODO
        pass

    def get_contact_details(self) -> str:
        '''
        Returns:
        str : Agent contact details
        ''' #TODO
        pass

   
    ## =================
    ## Methods:    

    def create_property(self) -> None:
        '''
        Creates a new property
        ''' #TODO            
        pass

    def mark_property(self, property: Property, mark: str) -> None:
        '''
        Marks a property as rented or sold

        Parameters:
        property (Property): the selected property
        mark (str): one of : sold, rented
        ''' #TODO
        pass

    def list_properties(self) -> list:
        '''
        List all the properties for the connected agent

        Returns:
        list of the connected Agent properties 
        ''' #TODO
        pass

    


