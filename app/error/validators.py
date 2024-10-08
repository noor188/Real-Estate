'''Validates the input values'''
from app.error import exceptions

## =================
## Data definitions

def validate_street_number(number) -> int:
    '''
    checks that the street number input is an int

    Parameters:
    number : the street number
    '''
    if isinstance(number, float):
        raise TypeError()
    elif isinstance(number, bool) or isinstance(number, str) :
        raise ValueError()
    return number

def validate_street_name(name: str) -> None:
    '''
    checks that the street name input is str

    Parameters:
    name (str): the street name
    '''
    if not isinstance(name, str):
        raise ValueError()
    return name

def validate_county(county: str) -> None:
    '''
    checks that the county input is str

    Parameters:
    county (str): the street county
    '''
    if not isinstance(county, str):
        raise ValueError()
    return county

def validate_state(state: str) -> None:
    '''
    checks that the state input str

    Parameters:
    state (int): the state
    ''' 
    if not isinstance(state, str):
        raise ValueError()
    return state

def validate_zip_code(zip_code: int) -> int:
    '''
    checks that the zip code input is an int

    Parameters:
    zip code (int): the zip code
    ''' 
    if isinstance(zip_code, float):
        raise TypeError()
    elif isinstance(zip_code, bool) or isinstance(zip_code, str) :
        raise ValueError()
    return zip_code

def validate_square_footage(square_footage: float)-> float :
    '''
    Checks that square_footage input is a number

    Parameters:
    square_footage (float):  the square footage
    '''
    if isinstance(square_footage, bool) or isinstance(square_footage, str):
        raise ValueError()
    return square_footage

def validate_num_of_bedrooms(num_of_bedrooms: int)-> int :
    '''
    Checks that num of bedrooms input is a int

    Parameters:
    num_of_bedrooms (int):  the number of bedrooms
    '''
    if isinstance(num_of_bedrooms, float):
        raise TypeError()
    if isinstance(num_of_bedrooms, bool) or isinstance(num_of_bedrooms, str):
        raise ValueError()
    return num_of_bedrooms

def validate_num_of_bathrooms(num_of_bathrooms: int) -> int:
    '''
    Checks that num of bathrooms input is a int

    Parameters:
    num_of_bathrooms (int):  the number of bathrooms
    '''
    if isinstance(num_of_bathrooms, float):
        raise TypeError()
    if isinstance(num_of_bathrooms, bool) or isinstance(num_of_bathrooms, str):
        raise ValueError()
    return num_of_bathrooms


    