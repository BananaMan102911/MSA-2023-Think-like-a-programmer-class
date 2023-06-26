import flask
from flask import request, jsonify
import Student_Gen_v2

import flask


app = flask.Flask(__name__)


#Use student generator program as a base
#write a function to create and return a list of student dictionaries
#Create 2 routes
# Returns all students
# returns students by ID


#auto reloads server when changes made
app.config["DEBUG"] = True

#Load dictionaries
student_dictionaries = Student_Gen_v2.get_student_dictionaries()

@app.route('/', methods = ['GET'])
def index():
    return "<h1> My name is Mason Throm <h1>"

#create a route to return all student data
@app.route('/api/students/all', methods = ['GET'])

def api_all():
    return jsonify(student_dictionaries)

app.run()