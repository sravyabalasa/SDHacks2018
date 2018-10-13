"""
EXTENSION #1
----------------
- Inputted vacation image: image URL 
- Displays images that have close percentages to the inputted vacation image
- Static website where things change !
- Create a dataset of images
- ASK: Difference between accessing data for predict and search! 

EXTENSION #2
----------------
- Display image back to the user
- Displays images that have close percentages to inputted vacation image

EXTENSION #3
----------------
- Choice out of 9-10 to click??
- User selects images they like
- Gives us images that are related to the user's new choice

EXTENSION #4
-------------
- Video
- Metadata

"""

#Import Clarifai
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

#Creates an "app" that runs Clarifai
CLARIFAI_API_KEY = '9f4c8fdd79b24c4aa14ed9f3fec060e2'
app = ClarifaiApp(api_key = CLARIFAI_API_KEY)

#Text file of image URLS
FILE_NAME = 'vacations_txt'
FILE_PATH = os.path.join(os.path.curdir, FILE_NAME)


#Training model for images, can be specified
model = app.models.get('travel-v1.0')

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

#Searching by image
search = app.inputs.search_by_image(url='https://japan-magazine.jnto.go.jp/jnto2wm/wp-content/uploads/1608_special_TOTO_main.jpg')

for search_result in search:
    print("Similarity: ", search_result.score, "| URL: ", search_result.url)

image = picPredict('https://japan-magazine.jnto.go.jp/jnto2wm/wp-content/uploads/1608_special_TOTO_main.jpg')

#Concepts in given image
print("Your image mostly has: ")
for i in image:
	print("Concept: " + i[0])
	print("Probability: " + i[1])
	print()

'''
#Search by multiple concepts with name

searchOne = app.inputs.search_by_predicted_concepts(concepts=[image[0][0], image[1][0], image[2][0], image[3][0], image[4][0]])
for search_result in searchOne:
	print("Similarity: ", search_result.score, "| URL: ", search_result.url)
'''
