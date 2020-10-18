import azure_custom_vision
import maps, yaml

if __name__ == "__main__":
    origin = "Sydney Town Hall"
    dest = "Parramatta, NSW"

    print("Proceeding to identify street lamps on route from {} to {}".format(origin, dest))

    print("Finding route...")
    direction_result = maps.get_route(origin, dest)
    print("Success \nGetting images along route...")
    route_images = maps.get_route_img(direction_result)
    print("Success")

    with open(r'credentials.yaml') as  file:
            credentials = yaml.load(file, Loader=yaml.BaseLoader)

    endpoint = credentials['custom_vision']['endpoint']
    prediction_key = credentials['custom_vision']['prediction_key']
    project_id = credentials['custom_vision']['id']
    publish_iteration_name = credentials['custom_vision']['name']
    
    print("Using credentials: {}".format(credentials['custom_vision']))

    print("Connecting to prediction model...")
    model = azure_custom_vision.Custom_Vision(endpoint, prediction_key, project_id, publish_iteration_name)
    print("Success")

    print("Predicting with threshold {}...".format(0.15))
    
    total_street_lamps = []
    for url in route_images:
        print("---------------------------------------------------------------") 
        print("Finding street lamps in image at {}".format(url))
        predictions = model.get_predictions(url, 0.15)
        print("Found {} lamps".format(len(predictions)))
        total_street_lamps.extend(predictions)

    # Display the findings.    
    for prediction in total_street_lamps:
        print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))