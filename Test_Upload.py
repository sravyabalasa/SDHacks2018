# UPLOAD.PY
import os
import time
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

#Creates Clarifai App
app = ClarifaiApp(api_key='549be605f54443cd8bf67b33e6061169')
app.inputs.delete_all()

#URL
URL_FILE_NAME = 'vacations_url.txt'
URL_FILE_PATH = os.path.join(os.path.curdir, URL_FILE_NAME)
# Counter variables
current_batch = 0
counter = 0
with open(URL_FILE_PATH) as data_file:
    images = [url.strip() for url in data_file]
    row_count = len(images)
    print("Total number of images:", row_count)

#Making images into a list --> SERVER
imageList = []
for i in range(row_count):
    print("Processing image: #", (counter+1))
    imageList.append(ClImage(url=images[i], allow_dup_url=False))
    counter=counter+1
app.inputs.bulk_create_images(imageList)

'''
#NAMES
NAMES_FILE_NAME = 'vacations_names.txt'
NAMES_FILE_PATH = os.path.join(os.path.curdir, NAMES_FILE_NAME)
# Counter variables
current_batch = 0
counter = 0
with open(NAMES_FILE_PATH) as data_file:
    names = [url.strip() for url in data_file]
    row_count = len(names)
    print("Total number of names:", row_count)

#Making names into a list
nameList = []
for i in range(row_count):
    nameList.append(names[i])
'''
