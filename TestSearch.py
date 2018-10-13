from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as C1Image

#Creates an "app" that runs Clarifai
CLARIFAI_API_KEY = '9f4c8fdd79b24c4aa14ed9f3fec060e2'
app = ClarifaiApp(api_key = CLARIFAI_API_KEY)


search = app.inputs.search_by_image(url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12224412/Shiba-Inu-On-White-01.jpg')

for search_result in search:
    print("Score:", search_result.score, "| URL:", search_result.url)
