"""
Initialize your Flask app. This is what will run your server.

Don't forget to install your dependencies from requirements.txt!
This is a doc string! It's a special kind of comment that is expected
in Python files. Usually, you use this at the top of your code and in
every function & class to explain what the code does.
"""
from flask import Flask, request, render_template, url_for
from guests import Guest
from datetime import datetime, date
from pprint import PrettyPrinter
import requests
import os

API_KEY = os.getenv('API_KEY')


app = Flask(__name__)

# Define global variables (stored here for now)

guest_list = []

pp = PrettyPrinter(indent=4)

today = date.today()
# Get month as a number:
month = today.strftime('%m')
# get current year:
year = today.strftime('%Y')


@app.route('/')
def homepage():
    """Return template for home."""
    return render_template('index.html')


@app.route('/about')
def about_page():
    """Show user party information."""
    # Sometimes, a cleaner way to pass variables to templates is to create a
    # context dictionary, and then pass the data in by dictionary key

    url = 'https://calendarific.com/api/v2/holidays'
    today = date.today()
    # Get month as a number:
    month = today.strftime('%m')
    # get current year:
    year = today.strftime('%Y')

    params = {
        'api_key': API_KEY,
        'country': 'US',
        'year': year,
        'month': month,
        
    }
    result_json = requests.get(url, params=params).json()
    pp.pprint(result_json)
    #trim down json to include response and holiday
    new_result = result_json["response"]["holidays"]

    holidays = []
    for holiday in new_result:
        new_holiday = { 
            "name" : holiday["name"],
            "date" : holiday["date"]["iso"],
            "description" : holiday["description"]
        }
        holidays.append(new_holiday)

    
        
    
    
    # HINT: in holidays, we'll probably need a way to store key-value pairs.
    # Think about the format we receive the response in
    # dates = #access data from your response
    # descriptions = ''#access data from your response
    context = {
        "holidays": holidays,
        # "date": dates,
        # "description": descriptions
    }

    return render_template('about.html', **context)


@app.route('/guests', methods=['GET', 'POST'])
def show_guests():
    """
    Show guests that have RSVP'd.

    Add guests to RSVP list if method is POST.
    """
    if request.method == "GET":
        return render_template("guests.html", guests=guest_list)
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        plus_one = request.form.get("plus-one")
        phone = request.form.get("phone")
        guest_list.append(Guest(name, email, plus_one, phone))
        return render_template("guests.html", guests=guest_list)


@app.route('/rsvp')
def rsvp_guest():
    """Show form for guests to RSVP for events."""
    return render_template('rsvp.html')


if __name__ == "__main__":
    app.run(debug=True)
