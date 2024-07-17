'''Validates the input values'''
import app.error.exceptions

## =================
## Data definitions

def validate_street_number(number: int) -> int:
    '''
    checks that the street number input is an int

    Parameters:
    number (int): the street number
    '''
    if not isinstance(number, int):
        raise exceptions.InvalidStreetNumber(number)
    return number

def validate_street_name(name: str) -> None:
    '''
    checks that the street name input is str

    Parameters:
    name (str): the street name
    ''' #TODO
    pass

def validate_county(county: str) -> None:
    '''
    checks that the county input is str

    Parameters:
    county (str): the street county
    ''' #TODO
    pass

def validate_state(state: str) -> None:
    '''
    checks that the state input str

    Parameters:
    state (int): the state
    ''' #TODO
    pass

def validate_zip_code(zip_code: int) -> None:
    '''
    checks that the zip code input is an int

    Parameters:
    zip code (int): the zip code
    ''' #TODO
    pass