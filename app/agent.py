from property import Property
## Allows an agent to manage properties  

## =================
## Constants:



## =================
## Data definitions

class Agent:  
        
    def __init__(self, id, name, contact_details):
        self.ID              = self.set_id(id)
        self.NAME            = self.set_name(name)
        self.CONTACT_DETAILS = self.set_contact_details(contact_details)
        self.Properties      = list() # composition
           
    def set_id(self, id):        
        pass
    
    def set_name(self, name):
        pass

    def set_contact_details(self, contact_details):
        pass

    def get_id(self):
        pass
    
    def get_name(self):
        pass

    def get_contact_details(self):
        pass

   
    ## =================
    ## Methods:   

    def create_property(self, property):
        pass

    def mark_property(self, property, mark):
        pass

    def list_properties(self):
        pass

    


