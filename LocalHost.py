# importing webapp libraries
import os
from flask import Flask, url_for, render_template, request, jsonify
from flask import *

# importing clarifai api + app setup
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='e0d4fa08067248beab61dbcab02f880d')
model = app.public_models.general_model

from Main import picPredict  # importing function

# local host app set up
app = Flask(__name__)
# localhost:5000 <-- put this in url bar

# https://www.telegraph.co.uk/content/dam/Travel/Destinations/Asia/Japan/cherry-blossom-hirosaki-park-japan.jpg?imwidth=450 <-- imageLink


@app.route('/')  # home page
def home():
    return render_template('<index class="htmL"></index>')


@app.route('/results')
def results():
    imageLink = request.args['inputname']
    results = picPredict(imageLink)
    print("these are results", str(results))
    printConcept = results[0]
    printPercentage = str(float(results[1]) * 100)
    return render_template('test.html', concept=printConcept, percentage=printPercentage)


'''@app.route('/', methods = ["GET", "POST"])
def background_process():
        if request.method == 'POST':
            try:
                imageLink = request.args['inputname']
                if imageLink:
                    results = picPredict( imageLink )
                    return render_template('test.html', results)
                else:
                    return render_template
            except:
                return'''


# run local host
if __name__ == "__main__":
    app.run()

''' <script type=text/javascript>
            $(function() {
              $('a#process_input').bind('click', function() {
                $.getJSON('/background_home', {
                  story: $('textarea[name="imageLink"]').val(),
                }, function(data) {
                  $('#results').text(data.result);
                });
                return false;
              });
            });
        </script>   '''
