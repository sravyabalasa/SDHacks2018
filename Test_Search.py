def output():
    from clarifai.rest import ClarifaiApp
    app = ClarifaiApp(api_key='549be605f54443cd8bf67b33e6061169')
    # Search using a URL
    search = app.inputs.search_by_image(url='https://image.shutterstock.com/image-photo/santorini-greece-picturesq-view-traditional-260nw-1040803156.jpg')
    for search_result in search:
        print("Score:", search_result.score, "| URL:", search_result.url)
    return

output()