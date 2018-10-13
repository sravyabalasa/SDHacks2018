#importing webapp libraries

import os
from flask import Flask, url_for, render_template, request
from flask import session

#importing clarifai api + app setup 
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='9f4c8fdd79b24c4aa14ed9f3fec060e2')
model = app.public_models.general_model

from Main.py import picPredict #importing function

#local host app set up
app = Flask(_name_)
#http://127.0.0.1:5000/ <-- put this in url bar

#'https://www.telegraph.co.uk/content/dam/Travel/Destinations/Asia/Japan/cherry-blossom-hirosaki-park-japan.jpg?imwidth=450' <-- imageLink

@app.route('/')  #home page
def render_home():
    picture = picPredict( imageLink )
    return render_template('home.hmtL', picture)

#run local host
if __name__== "__main__":
    app.run(debug=False)
