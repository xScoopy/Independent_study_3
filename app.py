"""
Initialize your Flask app. This is what will run your server.

Don't forget to install your dependencies from requirements.txt!
This is a doc string! It's a special kind of comment that is expected
in Python files. Usually, you use this at the top of your code and in
every function & class to explain what the code does.
"""
from flask import Flask, render_template, request
from guests import Guest

# This is a comment, and it's also used to explain what your code is doing.
# However, comments are more general, and can be used to denote different
# sections, give yourself or your team TODO items, or give some general information
# (for example: main routes serve static HTML files OR login routes provide access
# to protected sections of the site)
# It's good practice and helpful to teammates to ALWAYS comment your code and ALWAYS
# include docstrings!


# This code initializes a basic flask application.

app = Flask(__name__)

#name definition
my_name = 'Scoop'

#party day and time definitions
party_day = 'Saturday, Oct. 31st'
party_time = '2pm'

#guest list
guest_list = []

@app.route('/')
def homepage():
    """Return template for home."""
    # TODO: Using Jinja2 templating, pass your name in to
    # The home page so that the page reads "Happy halloween <your name>!"

    return render_template('index.html', name=my_name)

# TODO: write a route for '/about'. Define a view function that renders a template 'about.html'
# pass in the DAY and TIME of your halloween party as parameters, and render these dynamically in your templates.
@app.route('/about')
def aboutpage():
    """Return template for about page"""
    return render_template('about.html', day=party_day, time=party_time)

# TODO: write a route for '/guests'. Create a list of "dummy" guests, and pass these into your 'guests.html' template.
# HINT: create an <ul> tag  and use a Jinja for loop to render each "guest" in "guests" as an <li> element.
@app.route('/guests', methods=['GET', 'POST'])
def guests():
    """Return template for guest page with guest list passed to it"""
    if request.method == 'POST':
        guest_name = request.form.get('name')
        guest_email = request.form.get('email')
        guest_plus_one = request.form.get('plus-one')
        guest_phone = request.form.get('phone')
        guest_costume = request.form.get('costume')
        guest = Guest(guest_name, guest_email, guest_plus_one, guest_phone, guest_costume)
        guest_list.append(guest)
        return render_template('guests.html', guest_list = guest_list)
    elif request.method == 'GET':
        return render_template('guests.html', guest_list = guest_list)

# TODO: write a route for '/rsvp'. We aren't working on forms yet, but create a variable "rsvp" and set it to either True
# or False. Then, in your 'rsvp.html' template, create an <h2> tag that shows IF a guest is rsvp'd, and another that will show
# if they are NOT rsvp'd.
@app.route('/rsvp')
def rsvppage():
    """Return template for rsvp page with t/f passed to it """
    return render_template('rsvp.html', guest_list = guest_list)


# TODO: Using your resources, try finishing this code so that you can run your app!
if __name__ == "__main__":
    app.run(debug=True)
