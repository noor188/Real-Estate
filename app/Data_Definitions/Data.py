## ====================
## Data definitions for property class
## ====================


class SquareFootage:
    ## SquareFootage is float
    ## interp. square footage of a property
        
    ## sf1  = SquareFootage(245.4)
        
    '''def fn_for_SquareFootage(sf):
            # ... sf
            pass

        ## Template rules used:
        ##  - atomic non-distinct:  float (Number)'''
    
    def __init__(self, squarefootage):
        self.set_squarefootage(squarefootage)    
    
    def set_squarefootage(self, squarefootage):
        
        try:
            if isinstance(squarefootage, str) or isinstance(squarefootage, bool): # string or boolean
                raise TypeError
            if squarefootage < 0 : # neg
                raise ValueError    
        except TypeError: # loggin the error, notifying the user, reverting to a defult value or other appropriate actions 
            raise TypeError
        except ValueError:
            raise ValueError 
        else:
            self.value = squarefootage


## ====================

class NumofBedrooms:
    ## numofBedrooms is Integer[0,10]    
    ## interp. The number of bedrooms in a property

    ## nb1 = NumofBedrooms(4)

    '''
    def fn_for_numofBedrooms(numofBedrooms):
        # ... numofBedrooms
        pass

    ## Template rules used:
    ##  - atomic non-distinct:  Integer[0,10]'''

    def __init__(self, numofbedrooms):
        self.set_numofBedrooms(numofbedrooms)

    def set_numofBedrooms(self, numofBedrooms):
            
            try:
                if isinstance(numofBedrooms, str) or isinstance(numofBedrooms, bool) or isinstance(numofBedrooms, float): # string or boolean
                    raise TypeError
                if numofBedrooms < 0 or numofBedrooms > 10  : # neg
                    raise ValueError    
            except TypeError: # loggin the error, notifying the user, reverting to a defult value or other appropriate actions 
                raise TypeError
            except ValueError:
                raise ValueError 
            else:
                self.value = numofBedrooms
## ====================

class NumofBathrooms:
    ## numofBathrooms is Integer[1,10] 
    ## interp. The number of bathrooms in a property

    ## nb1 = NumofBathrooms(2)

    '''
    def fn_for_numofBathrooms(numofBathrooms):
        ## ... numofBathrooms
        pass

    ## Template rules used:
    ##  - atomic non-distinct:  Integer[0,10]'''

    def __init__(self, numofbathrooms):
        self.set_numofBathrooms(numofbathrooms)

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
            self.value = numofBathrooms

## ====================

class CustomDict:
    '''interp. the (key,val) pairs of a dict'''

    def __init__(self):
        pass
    
    @staticmethod
    def prompt_dict(*keys: str) -> dict:
        '''Accepts a variable number of string arguments (keys) and returns a dictionary.
        The value for each key is obtained bt prompting the user for input'''
        values = dict()
        for key in keys:
            values[key] = input('Enter {} value'.format(key))
        
        return values










