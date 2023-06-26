class Student():
    #1. Polymorphism
    #2. Inheritance
    #3. Encapsulation


    #Define a constructor
    #The constructor defines what happens when we create an automobile
    def __init__(self, Last_name, first_name, major, credit_hours, gpa, ID_number):
        #assign parameter values
        self.__last_name = Last_name
        self.__first_name = first_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__ID_number = ID_number
    #Create getter and setter methods for class atributes
    def get_last_name(self):
        return self.__last_name
    
    def get_first_name(self):
        return self.__first_name
    
    def get_major(self):
        return self.__major
    
    def get_gpa(self):
        return self.__gpa
    
    def get_credit_hours(self):
        return self.__credit_hours  
      
    def set_credit_hours(self, new_credit_hours):
        self.__credit_hours = new_credit_hours
    
    def set_owner(self, new_owner):
        self.__owner = new_owner

    def get_ID_number(self):
        return self.__ID_number
    
    def get_class_level(self):
        #get the surrent date
        credits = self.__credit_hours 
        if credits >=0 and credits <=30:
            class_level = "Freshman"
        elif credits <=60  and credits >= 31:
            class_level="Sophomore"
        elif credits <=90 and credits >=60:
            class_level = "Junior"
        elif credits >= 90:
            class_level = "Senior"

        #return the difference between the current year and the auto year as the age
        return class_level

    #create a method to print automobile data
    def print_data(self):
        print(f"First Name: {self.__first_name} Last Name: {self.__last_name} \n Student ID: {self.__ID_number}")
        print(f"Major: {self.__major} GPA: {self.__gpa}")
        print(f"Credit Hours: {self.__credit_hours}")
        print(F"Class: {self.get_class_level()}\n")
