from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='9f4c8fdd79b24c4aa14ed9f3fec060e2')

model = app.public_models.general_model
response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
