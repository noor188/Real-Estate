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
    ''' #TODO
    return ''

def validate_county(county: str) -> None:
    '''
    checks that the county input is str

    Parameters:
    county (str): the street county
    ''' #TODO
    return ''

def validate_state(state: str) -> None:
    '''
    checks that the state input str

    Parameters:
    state (int): the state
    ''' #TODO
    return ''

def validate_zip_code(zip_code: int) -> None:
    '''
    checks that the zip code input is an int

    Parameters:
    zip code (int): the zip code
    ''' #TODO
    return 0