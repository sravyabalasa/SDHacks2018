"""
EXTENSION #1
----------------
- Inputted vacation image: image URL choice out of 9-10 to click
- Displays images that have close percentages to the inputted vacation image
- Static website where things change !
- Create a dataset of images

EXTENSION #2
----------------
- Display image back to the user
- Displays images that have close percentages to inputted vacation image

EXTENSION #3
----------------
- User selects images they like
- Gives us images that are related to the user's new choice

EXTENSION #4
-------------
- Video
- Metadata

"""

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as C1Image

#Creates an "app" that runs Clarifai
CLARIFAI_API_KEY = '9f4c8fdd79b24c4aa14ed9f3fec060e2'
app = ClarifaiApp(api_key = CLARIFAI_API_KEY)


search = app.inputs.search_by_image(url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12224412/Shiba-Inu-On-White-01.jpg')

for search_result in search:
    print("Score:", search_result.score, "| URL:", search_result.url)
