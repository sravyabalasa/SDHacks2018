#importing webapp libraries
import os
from flask import Flask, url_for, render_template, request
from flask import session

app = Flask(_name_)
#http://127.0.0.1:5000/
app.secret_key='w98fw9ef8hwe98fhwee'

@app.route('/')  #home page
def render_home():
    return render_template('home.hmtL')

#run local host
if __name__== "__main__":
    app.run(debug=False)
