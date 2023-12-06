from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
    first_name = "Ray"
    stuff = "This is not bold text"

    favorite_pizza = ['pepperoni', 'cheese', 'sausage', 41]
    return render_template('index.html', first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)
#     return "<h1>Hello World</h1>"

# localhost:5000/user/<name> Will say hello Ray or whatever is in variable name
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# Create custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# Internal serger error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html")