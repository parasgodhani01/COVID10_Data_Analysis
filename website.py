{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template_string, render_template\n",
    "# library is run_simple\n",
    "from werkzeug.serving import run_simple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__,template_folder='.')\n",
    "\n",
    "@app.route('/')\n",
    "\n",
    "def index():\n",
    "    data_html = df.to_html(index=False) \n",
    "\n",
    "    return render_template_string('''\n",
    "        <!DOCTYPE html>\n",
    "        <html>\n",
    "        <body>\n",
    "            <h1>Covid 19 Data</h1>\n",
    "            <h2>This is data Of Covid 19</h2>\n",
    "            <h3>Definition of Each Variable</h3>\n",
    "            <h4>country: The name of the country or region.</h4>\n",
    "            <h5/>continent: The continent where the country or region is located.\n",
    "         </body>\n",
    "        </html>\n",
    "    ''', data = data_html)\n",
    "\n",
    "@app.route('/about')\n",
    "def about():\n",
    "    return render_template('aboutcolor.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://localhost:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "run_simple('localhost',5000, app, use_reloader=False, use_debugger=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
