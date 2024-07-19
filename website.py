from flask import Flask, render_template_string, render_template
import sqlite3
from werkzeug.serving import run_simple

app = Flask(__name__,template_folder='.')


@app.route('/')
def index():
    my_connection = sqlite3.connect('covid_19.db')
    cursor = my_connection.cursor()
    data = cursor.execute("SELECT * FROM covid_19").fetchall()
    my_connection.close()

    data = data.to_html(index=False) 

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <body>
            <h1>Covid 19 Data</h1>
        {{data|safe}}
        </body>
        </html>
    ''', data = data)

@app.route('/about')
def about():
    return render_template('about.html')


run_simple('localhost',5000, app, use_reloader=False, use_debugger=False)