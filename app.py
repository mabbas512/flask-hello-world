# ---- Flask Hello World ---- #

# import the Flask class from flask module
from flask import Flask

# Create the application object
app = Flask(__name__)

# enable/disable debugging
app.config['DEBUG'] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!?!?!?!?"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

# testing integer
@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"

# testing float
@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "correct"

# testing path
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"

# testing status code
@app.route("/name/<name>")
def index(name):
	if name.lower() == "michel":
		return "Hello, {}".format(name)
	else:
		return "Not Found", 404

# start the development server using run method
if __name__ == ("__main__"):
	app.run()
