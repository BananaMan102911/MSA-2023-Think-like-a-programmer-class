import flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
    return "<h1> My name is Mason. This is really weird. I don't know how I feel about this. I have access to the web now?</h1>"

app.run()