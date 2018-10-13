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
- Train the model 

"""

#Import Clarifai
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

#Creates an "app" that runs Clarifai
CLARIFAI_API_KEY = '9f4c8fdd79b24c4aa14ed9f3fec060e2'
app = ClarifaiApp(api_key = CLARIFAI_API_KEY)


#Training model for images, can be specified
model = app.models.get('travel-v1.0')

#Adding image to search index
img1 = ClImage(url="https://www.telegraph.co.uk/content/dam/Travel/Destinations/Asia/Japan/cherry-blossom-hirosaki-park-japan.jpg?imwidth=450")
img2 = ClImage(url="https://samples.clarifai.com/puppy.jpeg")
img3 = ClImage(url="https://keyassets-p2.timeincuk.net/wp/prod/wp-content/uploads/sites/50/2017/04/J1GDDB-920x614.jpg")
img4 = ClImage(url="https://www.tahiti.com/images1/thumbs/Borabora-LeMeridien_600x360.jpg")

app.inputs.bulk_create_images([img1, img2])


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

'''
#Searching by image
search = app.inputs.search_by_image(url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12224412/Shiba-Inu-On-White-01.jpg')

for search_result in search:
    print("Similarity: ", search_result.score, "| URL: ", search_result.url)
'''

#Search by concepts
image = picPredict('https://www.telegraph.co.uk/content/dam/Travel/Destinations/Asia/Japan/cherry-blossom-hirosaki-park-japan.jpg?imwidth=450')

#Concepts in given image
print("Your image mostly has: ")
for i in cherryBlossom:
	print("Concept: " + i[0])
	print("Percentage Similarity: " + float(i[1])*100)
	print()

#Search by multiple concepts with name
searchOne = app.inputs.search_by_predicted_concepts(concepts=[image[0][0], image[1][0], image[2][0], image[3][0], image[4][0]])

for search_result in searchOne:
	print("Similarity: ", search_result.score, "| URL: ", search_result.url)

