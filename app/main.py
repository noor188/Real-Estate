# a real estate app, allows an agent to manage properties available for purchase or rent

## ===============================
## imports


## ===============================
## Classes

class Property:
    ## ====================
    '''
    numofRooms
    numofBathrooms
    squareFootage
    '''
    ## ====================
    ## functions
    def __init__(self):
        pass

    def display(self):
        pass

    def prompinit():
        pass     

class House(Property):
    ## ====================
    ## Data
    '''
    parking
    privatePool
    exteriorFeatures
    '''
    ## ====================
    ## functions
    def __init__(self):
        pass

    def display(self):
        pass

    def prompinit():
        pass     

class Apartment(Property):
    ## ====================
    ## Data
    '''
    balcony
    rentableStorageUnits
    fullyRenovatedHouse
    '''
    ## ====================
    ## functions
    def __init__(self):
        pass

    def display(self):
        pass

    def prompinit():
        pass     

class Rent:
    ## ====================
    ## Data
    '''
    price 
    duration
    utilities
    '''
    ## ====================
    ## functions
    def __init__(self):
        pass

    def display(self):
        pass

    def prompinit():
        pass     

class Purchase:
    ## ====================
    ## Data
    '''
    price
    furnished    
    '''
    ## ====================
    ## functions
    def __init__(self):
        pass

    def display(self):
        pass

    def prompinit():
        pass     

class HosueRent(House, Rent):
    pass

class HousePurchase(House, Purchase):
    pass

class ApartmentRent(Apartment, Rent):
    pass

class ApartmentPurchase(Apartment, Purchase):
    pass

