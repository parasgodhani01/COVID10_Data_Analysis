from flask import Flask, render_template_string, render_template
import sqlite3
from werkzeug.serving import run_simple


my_connection = sqlite3.connect(r'E:\St.Clair College\Intro to Python - 100\DAB 111-W024\DAB111_project_Group_8\Database\covid_19.db')
cursor = my_connection.cursor()
data = cursor.execute("SELECT * FROM covid_19").fetchall()
my_connection.close()
# print(data)

app = Flask(__name__)
@app.route('/')

def index():
    data_html = data.to_html(index=False) 

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <body>
            <h1>Covid 19 Data</h1>
            <h2>This is data Of Covid 19</h2>
            <p>My first <b>paragraph</b> .</p>
        {{data|safe}}
        </body>
        </html>
    ''', data = data_html)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)


# def index():    
#     return render_template("index.html") 

# @app.route("/about")
# def about():
#     return render_template("about.html")
        

