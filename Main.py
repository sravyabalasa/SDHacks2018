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
    response = model.predict_by_url(url= imageLink)
    concepts = response['outputs'][0]['data']['concepts']

    for concept in concepts:
        results = (concept['name'], concept['value'])

    return results

<<<<<<< HEAD
#Passing cherry blossom through model
=======

'''
>>>>>>> d0df7b4dbc480a3a70bd890da3c5cac3e284d29c
response = model.predict_by_url(url='https://www.telegraph.co.uk/content/dam/Travel/Destinations/Asia/Japan/cherry-blossom-hirosaki-park-japan.jpg?imwidth=450')
concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])

print('--------')

#Passing through model
response2 = model.predict_by_url(url='https://static.tripzilla.com/thumb/7/e/102014_800x.jpg')
concepts = response2['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])
'''
