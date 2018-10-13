from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
app = ClarifaiApp(api_key='9f4c8fdd79b24c4aa14ed9f3fec060e2')

model = app.models.get('general-v1.3')

model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg', min_value=0.97)
print
