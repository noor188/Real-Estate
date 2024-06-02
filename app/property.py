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
        def __init__(self, squareFootage: float, numofBedrooms: int = 0, numofBathrooms: int= 1) -> None:
            self.set_squareFootage(squareFootage)
            self.numofBedrooms  = numofBedrooms
            self.numofBathrooms = numofBathrooms      

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
    """
    def display(self) -> None:
        ''' display the property data values'''       
        pass """

    def prompinit():
        pass    