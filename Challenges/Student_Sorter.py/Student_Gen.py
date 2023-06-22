import Student_Info
students = open("Students.txt", "r")
Student_info_list = []
for line_of_data in students:
    Student_info_list.append(line_of_data.split(","))
print(Student_info_list)



student1 = Student_Info.Student ("Throm", "Mason", "Geology", 20, 3.5, 4321)
student2 = Student_Info.Student ("Miller", "Steven", "Engeneering", 50, 3.96, 1234)

student_list = []
student_list.append(student1)
student_list.append(student2)



for student in student_list:
    student.print_data()
