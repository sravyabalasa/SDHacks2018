# upload.py
import os
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
app = ClarifaiApp(api_key='a0a2a1f7c1db46dd90e600257188a7d3')
FILE_NAME = 'vacations_url.txt'
FILE_PATH = os.path.join(os.path.curdir, FILE_NAME)

def testSearch():
	# Counter variables
	current_batch = 0
	counter = 0
	batch_size = 32
	with open(FILE_PATH) as data_file:
		images = [url.strip() for url in data_file]
		row_count = len(images)
		print("Total number of images:", row_count)


	while(counter < row_count):
		print("Processing batch: #", (current_batch+1))
		imageList = []
		for current_index in range(counter, counter+batch_size - 1):
			try:
				imageList.append(ClImage(url=images[current_index], allow_dup_url=True))
			except IndexError:
				break

		app.inputs.bulk_create_images(imageList)
		counter = counter + batch_size
		current_batch = current_batch + 1
	
	search = app.inputs.search_by_image(url='https://handluggageonly.co.uk/wp-content/uploads/2016/09/Hand-Luggage-Only-5.jpg')
	
	result = ()
	for search_result in search:
		result = (search_result.url)
	return ( result )


ans = testSearch()
for i in ans:
	print (i)


"""
EXTENSION #1
----------------
- Displays 3 images that have close percentages to the inputted vacation image

EXTENSION #3
----------------
- Adds users input to the dataset

EXTENSION #4
-------------
- Video
- Metadata

"""

"""

#Import Clarifai
import os
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

#Creates an "app" that runs Clarifai
CLARIFAI_API_KEY = '9f4c8fdd79b24c4aa14ed9f3fec060e2'
app = ClarifaiApp(api_key = CLARIFAI_API_KEY)

#Text file of image URLS
FILE_NAME = 'food_URL.txt'
FILE_PATH = os.path.join(os.path.curdir, FILE_NAME)

#Counter variables
current_batch = 0
counter = 0
batch_size = 32 #amount imported each time, goes backwards 

#takes each image from the data file line
with open(FILE_PATH) as data_file:
	images = [url.strip () for url in data_file] 
	row_count = len(images)
	print ("Total number of images: ", row_count)

while(counter < row_count):
	print("Processing batch: #", (current_batch))
	imageList = []

	#appends images images in sets of 32
	#out of bounds error checked for
	for current_index in range(counter, counter+batch_size - 1):
		try:
			imageList.append(ClImage(url=images[current_index]))
		except IndexError:
			break

	app.inputs.bulk_create_images(imageList)
	counter = counter + batch_size
	current_batch = current_batch + 1

#Searching by image
#Used as a reference like a training data set
search = app.inputs.search_by_image(url='https://www.jerseymikes.com/media/static/menu/products/lg/cookie.jpg')

#Returns search results
for search_result in search:
	print("Similarity: ", search_result.score, "| URL: ", search_result.url)

	"""

"""
#Training model for images, can be specified
#model = app.models.get('travel-v1.0')
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
"""