'''
Filename: Test_Search.py
Author:   Main: Sravya Balasa
          Partners: Jill Su, Titan Ngo, Stanley Lee
Date:     10/14/18
'''

'''
output( inputURL )

Takes in user's input URL
Outputs top three vacation location names + urls
'''


def output(inputURL):

    # Import statements & Constructors
    import os
    from clarifai.rest import ClarifaiApp
    app = ClarifaiApp(api_key='303124e3f6374c819309c02579c5c08b')

    # URL Declaration
    URL_FILE_NAME = 'vacations_url.txt'
    URL_FILE_PATH = os.path.join(os.path.curdir, URL_FILE_NAME)

    # Reads the urls of images from txt file
    with open(URL_FILE_PATH) as data_file:
        images = [url.strip() for url in data_file]
        row_count = len(images)

    # NAMES Declaration
    NAMES_FILE_NAME = 'vacations_names.txt'
    NAMES_FILE_PATH = os.path.join(os.path.curdir, NAMES_FILE_NAME)

    # Reads the names of locations from txt file
    with open(NAMES_FILE_PATH) as data_file:
        names = [url.strip() for url in data_file]
        row_count = len(names)

    # Making names into a list
    nameList = []
    for i in range(row_count):
        nameList.append(names[i])

    # Searching for similar images
    search = app.inputs.search_by_image(url=inputURL)

    # Top 1
    var0 = search[0].url
    index0 = images.index(var0)
    name0 = names[index0]

    # Top 2
    var1 = search[1].url
    index1 = images.index(var1)
    name1 = names[index1]

    # Top 3
    var2 = search[2].url
    index2 = images.index(var2)
    name2 = names[index2]

    return ([name0, var0], [name1, var1], [name2, var2])
