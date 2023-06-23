import Student_info

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



def main():
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
            new_student = Student_info.Student(first_name, last_name, major, credit_hours, gpa, student_ID)
            list_of_students.append(new_student)

    except Exception as err:
        print(err)




    student1 = Student_info.Student ("Throm", "Mason", "Geology", 20, 3.5, 4321)
    student2 = Student_info.Student ("Miller", "Steven", "Engeneering", 50, 3.96, 1234)

    student_list = []
    student_list.append(student1)
    student_list.append(student2)



    for student in list_of_students:
        student.print_data()

main()
