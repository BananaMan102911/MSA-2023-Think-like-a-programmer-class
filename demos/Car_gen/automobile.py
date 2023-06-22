import datetime
class Automoblie():
    #1. Polymorphism
    #2. Inheritance
    #3. Encapsulation


    #Define a constructor
    #The constructor defines what happens when we create an automobile
    def __init__(self, make, model, vin, engine_size, owner, year):
        #assign parameter values
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine_size = engine_size
        self.__owner = owner
        self.__year = year
    #Create getter and setter methods for class atributes
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_vin(self):
        return self.__vin
    
    def get_engine_size(self):
        return self.__engine_size
    
    def set_engine_size(self, new_size):
        self.__engine_size = new_size
    
    def get_owner(self):
        return self.__owner
    
    def set_owner(self, new_owner):
        self.__owner = new_owner

    def get_year(self):
        return self.__year
    
    def get_age(self):
        #get the surrent date
        the_date = datetime.datetime.now()
        this_year = the_date.year
        
        #return the difference between the current year and the auto year as the age
        return this_year - self.__year

    #create a method to print automobile data
    def print_data(self):
        print(f"{self.__year} {self.__make} {self.__model}")
        print(f"VIN: {self.__vin} Engine size: {self.__engine_size}")
        print(f"Owner: {self.__owner}\n")
