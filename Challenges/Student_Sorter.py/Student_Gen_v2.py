import Student_info_v2

from datetime import datetime
"""
function to write to error file
input: error message
output: none
"""
def write_to_error_log(message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")
        #write an error to log file
        log_file.write(f"{datetime.now()} {message} \n") 
        #close log file
        log_file.close()
    except Exception as err: 
        print(err)
        return
    #return

'''
fuction to return list of student objects
input: none
output: list of student objects
'''

def load_students():
    #Create 2 instances of student
    list_of_students = []

    try:
        #create a file handeler
        file = open("Students.csv", "r")

        #Create a variable to keep track of the line in the file that we are reading
        line_number = 0
        #read file line by line in for loop
        for line_of_data in file:
            line_number += 1
            #skip first line in the file
            if line_number == 1:
                continue 

            #split the line of data at the comma
            student_data = line_of_data.split(",")
            
            #handle errors in data format. Line_of_data should have six item
            #if error in format then write a message to a log file
            try:
                if len(student_data) != 6:
                    raise Exception(f"There is an error in your data file on line {line_number}")
            except Exception as err:
                write_to_error_log(str(err))
                continue
            #get student data and create a student object for each student
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
            student_ID = student_data[5].strip()
            new_student = Student_info_v2.Student(first_name, last_name, major, credit_hours, gpa, student_ID)
            list_of_students.append(new_student)

    except Exception as err:
        print(err)

    return list_of_students


"""
Function to convert student object to student dictionary
Input: List of students
Output: List of student dictionaries
"""
def Student_to_dictionary(list_of_students):
    # create a list to store the dictionaries
    student_dictionary_list = []

    for student in list_of_students:
        student_dictionary = {}
        #set keys and values for first name, last name, ID, majhor, gpa, class level
        student_dictionary['id'] = student.get_ID_number()
        student_dictionary['first name'] = student.get_first_name()
        student_dictionary["last name"] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['GPA'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        
        #append to student dictionary list
        student_dictionary_list.append(student_dictionary)
    
    return student_dictionary_list

"""
Function to get student dictionaries
Input: none
Output: list of tsudent dictionaries
"""
def get_student_dictionaries():
    student_list = load_students()

    #get student dictionaries
    student_dictionaries = Student_to_dictionary(student_list)

    return student_dictionaries

get_student_dictionaries()