# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions

# default route or 'URL'
@app.route("/index")
def home():

        name = "Aarti" # write your name
        age = "15" # write your age

        return render_template('index.html' , name = name , age = age)

    # define the route to father webpage
@app.route("/father")

    # define the route to mother webpage
@app.route("/mother")

    # define the route to friends webpage
@app.route("/friend")

# add other routes, if you want



app.run(debug=True)
