# UPLOAD.PY
import os
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

#Creates Clarifai App
app = ClarifaiApp(api_key='549be605f54443cd8bf67b33e6061169')

def testSearch ( inputURL ):
    global app
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

    #NAMES
    NAMES_FILE_NAME = 'vacations_names.txt'
    NAMES_FILE_PATH = os.path.join(os.path.curdir, NAMES_FILE_NAME)
    #Counter variables
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

    from clarifai.rest import ClarifaiApp
    app = ClarifaiApp(api_key='549be605f54443cd8bf67b33e6061169')
    # Search using a URL
    search = app.inputs.search_by_image(url= inputURL)
    
    results = []
    count = 0
    for search_result in search:
        results.append(( nameList[count], str(search_result.url) ))
        count=count + 1

    return(results[1],results[2],results[3])
    

testSearch('https://image.shutterstock.com/image-photo/santorini-greece-picturesq-view-traditional-260nw-1040803156.jpg')
