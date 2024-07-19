from flask import Flask, render_template_string, render_template
import sqlite3
from werkzeug.serving import run_simple

app = Flask(__name__,template_folder='.')

@app.route('/')
def index():
    my_connection = sqlite3.connect('Covid_19.db')
    cursor = my_connection.cursor()
    cursor.execute("SELECT * FROM covid_19")
    data = my_connection.fetchall()
    my_connection.close()


    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <body>
            <h1>Covid 19 Data</h1>
            <h2>This is data Of Covid 19</h2>
            <h3>Definition of Each Variable</h3>
            <h4>country: The name of the country or region.</h4>
            <h5/>continent: The continent where the country or region is located.
            population: The total population of the country or region.
            day: The date in the format DD-MM-YYYY.
            time: The timestamp when the data was recorded, in ISO 8601 format (YYYY-MM-DDTHH:MM+00:00).
            Cases: The total number of reported cases (likely referring to a specific disease or condition).
            Recovered: The total number of individuals who have recovered from the condition.
            Deaths: The total number of deaths attributed to the condition.
            Tests: The total number of tests conducted for the condition.</h4>
            <p>My first <b>paragraph</b> .</p>
        {{data|safe}}
        </body>
        </html>
    ''', data = data)

@app.route('/about')
def about():
    return render_template('about.html')


run_simple('localhost',5000, app, use_reloader=False, use_debugger=False)