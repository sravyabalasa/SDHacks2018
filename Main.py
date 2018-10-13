from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='9f4c8fdd79b24c4aa14ed9f3fec060e2')
model = app.public_models.general_model


def picPredict( imageLink ): #url should be a string
    response = model.predict_by_url(url= imageLink)
    concepts = response['outputs'][0]['data']['concepts']

    for concept in concepts:
        results = (concept['name'], concept['value'])

    return results


'''
response = model.predict_by_url(url='https://www.telegraph.co.uk/content/dam/Travel/Destinations/Asia/Japan/cherry-blossom-hirosaki-park-japan.jpg?imwidth=450')
concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])

print('--------')

response2 = model.predict_by_url(url='https://static.tripzilla.com/thumb/7/e/102014_800x.jpg')
concepts = response2['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])
'''
