'''
Filename: Test_Upload.py
Author:   Main: Sravya Balasa
          Partners: Jill Su, Titan Ngo, Stanley Lee
Date:     10/14/18
'''

'''
run()

Uploads all vacation images to the server
No output
Loaded every time website is reloaded
'''
def run():

    #Import statements + constructors
    import os
    from clarifai.rest import ClarifaiApp
    from clarifai.rest import Image as ClImage

    #Creates Clarifai App
    app = ClarifaiApp(api_key='303124e3f6374c819309c02579c5c08b')
    #Resets the server to 0 images, avoids duplicates
    app.inputs.delete_all()

    #URL
    URL_FILE_NAME = 'vacations_url.txt'
    URL_FILE_PATH = os.path.join(os.path.curdir, URL_FILE_NAME)

    #Reads the urls of images from txt file
    with open(URL_FILE_PATH) as data_file:
        images = [url.strip() for url in data_file]
        row_count = len(images)

    #Making images into a list that convers into being uploadable to the server
    imageList = []
    for i in range(row_count):
        imageList.append(ClImage(url=images[i], allow_dup_url=False))
    app.inputs.bulk_create_images(imageList)

    #NAMES
    NAMES_FILE_NAME = 'vacations_names.txt'
    NAMES_FILE_PATH = os.path.join(os.path.curdir, NAMES_FILE_NAME)

    return

run()
