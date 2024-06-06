## ===============================
## imports


## ===============================
## Classes

class Property:
    ## ====================
    ## Data
    '''
    squareFootage
    numofBedrooms
    numofBathrooms    
    '''
    ## ====================
    ## functions
    class Property: # stub
        def __init__(self, squareFootage: float = 0, numofBedrooms: int = 0, numofBathrooms: int= 1) -> None:
            self.set_squareFootage (squareFootage)
            self.set_numofBedrooms (numofBedrooms)        
            self.set_numofBathrooms(numofBathrooms)      

        def set_squareFootage(self, squareFootage):
            
            try:
                if isinstance(squareFootage, str) or isinstance(squareFootage, bool): # string or boolean
                    raise TypeError
                if squareFootage < 0 : # neg
                    raise ValueError    
            except TypeError: # loggin the error, notifying the user, reverting to a defult value or other appropriate actions 
                raise TypeError
            except ValueError:
                raise ValueError 
            else:
                self.squareFootage = squareFootage
        
        def set_numofBedrooms(self, numofBedrooms):
            
            try:
                if isinstance(numofBedrooms, str) or isinstance(numofBedrooms, bool) or isinstance(numofBedrooms, float): # string or boolean
                    raise TypeError
                if numofBedrooms < 0 or numofBedrooms > 10 : # neg
                    raise ValueError    
            except TypeError: # loggin the error, notifying the user, reverting to a defult value or other appropriate actions 
                raise TypeError
            except ValueError:
                raise ValueError 
            else:
                self.numofBedrooms = numofBedrooms
        
        def set_numofBathrooms(self, numofBathrooms):
            
            try:
                if isinstance(numofBathrooms, str) or isinstance(numofBathrooms, bool) or isinstance(numofBathrooms, float): # string or boolean
                    raise TypeError
                if numofBathrooms < 1 or numofBathrooms > 10  : # neg and 0 
                    raise ValueError    
            except TypeError: # loggin the error, notifying the user, reverting to a defult value or other appropriate actions 
                raise TypeError
            except ValueError:
                raise ValueError 
            else:
                self.numofBathrooms = numofBathrooms
        
        def get_squareFootage(self):
            return self.squareFootage

        def get_numofBedrooms(self):
            return self.numofBedrooms

        def get_numofBathrooms(self):
            return self.numofBathrooms
    """
    def display(self) -> None:
        ''' display the property data values'''       
        pass """

    def prompinit():
        pass    