from flask import Flask, render_template_string, render_template
import sqlite3
from werkzeug.serving import run_simple
import pathlib

my_connection = sqlite3.connect(r'E:\St.Clair College\Intro to Python - 100\DAB 111-W024\DAB111_project_Group_8\Database\covid_19.db')
cursor = my_connection.cursor()
data = cursor.execute("SELECT * FROM covid_19").fetchall()
my_connection.close()
# print(data)

# cwd = pathlib.Path.cwd()
# base_path = pathlib.Path(r'E:\St.Clair College\Intro to Python - 100\DAB 111-W024\DAB111_project_Group_8\Database\covid_19.db')
# db_name = "covid_19.db"
# db_path = base_path / db_name
# print(db_path)


app = Flask(__name__)
@app.route("/")
def index():    
    return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    covid = cursor.execute("SELECT * FROM covid_19").fetchall()
    con.close()

    columns = ['row_number', 'invoice_id', 'branch', 'customer_id', 'gender', 'age',
       'customer_type', 'credit_score', 'product_category',
       'number_of_products', 'tax_amount', 'price', 'total_amount', 'ratings',
       'customer_churn']
    
    return render_template("about.html", columns=columns, covid=covid)
        

if __name__=="__main__":
    app.run(debug=True)