"""
Filename: Main.py
Date: 10/13/18
Users: Sravya, Titan, Jill, Stanley
"""

"""
MVP
--------
WebApp that displays Clarifai's normal results in classifying images of vacations

"""

#Import Clarifai
from clarifai.rest import ClarifaiApp

#Creates an "app" that runs Clarifai
CLARIFAI_API_KEY = '9f4c8fdd79b24c4aa14ed9f3fec060e2'
app = ClarifaiApp(api_key = CLARIFAI_API_KEY)

#Training model for images, can be specified
model = app.public_models.general_model

#PREDICT API
#Returns a list of concepts in an image based on model
#Used for access in localHost to imageLink
def picPredict( imageLink ): #URL should be a string for process
    #All data given by model
    response = model.predict_by_url(url= imageLink)
    #Accessing the concepts from all the data returned by predict_by_url
    concepts = response['outputs'][0]['data']['concepts']
    results = []

    for concept in concepts:
        results.append((concept['name'], str(concept['value'])))

    return results

#Passing URL through model
cherryBlossom = picPredict('https://www.telegraph.co.uk/content/dam/Travel/Destinations/Asia/Japan/cherry-blossom-hirosaki-park-japan.jpg?imwidth=450')
print("Your image mostly has: ")
for i in cherryBlossom:
	print("Concept: " + i[0])
	print("Percentage Similarity: " + str(float(i[1])*100))


