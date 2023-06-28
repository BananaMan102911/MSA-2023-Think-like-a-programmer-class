from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a Flask name
app = Flask(__name__)
app.config["DEBUG"] = True

#set secret key
app.config["SECRET_KEY"] = 'your secret key'


#Functioin to request student data from the api
#input: url
#Output: JSON student data
def get_student_data(url):
    #make a request
    response = requests.get(url)

    #convert format to json
    response_json = response.json()
    return response_json


#Create route for site index. Will display all of the student data
@app.route('/', methods = ['GET'])
def index():
    #make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'
    #get student data
    student_data = get_student_data(url)
    return render_template('index.html', student_data = student_data)

#create a route for the majors search page
@app.route('/majors', methods=['GET', 'POST'])
def majors():
    #make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'

    #get student data
    student_data = get_student_data(url)
    major_list = []
    # write code that gets the unique majors from the student_data list
    for student in student_data:
        student_major = student['major']
        if student_major not in major_list:
            major_list.append(student_major)

    if request.method == 'POST':
        #get for data
        major = request.form['major'].strip()
        # create list to store results in
        results_list = []
        
        #validate form data
        if not major: 
            flash('YOU MUST SELECT A MAJOR >:(')
        else:
            #get students with a selected major and put in results list
                for student in student_data:
                    student_major = student['major']
                    if student_major == major:
                        results_list.append(student)
                return render_template('majors.html', major_list = major_list, results_list = results_list)
    return render_template('majors.html', major_list = major_list)
    


#run the flask application
app.run(port=5007)
