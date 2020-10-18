
import azure_custom_vision
import maps, yaml

def authentication_credentials():
    with open(r'credentials.yaml') as  file:
            credentials = yaml.load(file, Loader=yaml.BaseLoader)

    endpoint = credentials['custom_vision']['endpoint']
    prediction_key = credentials['custom_vision']['prediction_key']
    project_id = credentials['custom_vision']['id']
    publish_iteration_name = credentials['custom_vision']['name']
    
    print("Using credentials: {}".format(credentials['custom_vision']))
    return endpoint, prediction_key, project_id, publish_iteration_name

def compute_data_all_routes(origin, dest):
    final_route_data = []
    lamp_confidence_threshold = 0.15
    print("Proceeding to identify street lamps on route from {} to {}".format(origin, dest))

    endpoint, prediction_key, project_id, publish_iteration_name = authentication_credentials()
    print("Connecting to prediction model...")
    model = azure_custom_vision.Custom_Vision(endpoint, prediction_key, project_id, publish_iteration_name)
    print("Success")


    print("Finding routes...")
    routes = maps.get_routes(origin, dest)
    print("Success")
    for i in range(len(routes['routes'])):
        print("---------------------------------------------------------------") 
        print("Counting lamps on route {} with confidence threshold {}...".format(i, lamp_confidence_threshold))
        curr_route = routes["routes"][i]
        images_urls = maps.get_route_img(curr_route)
        route_idx = i
        total_street_lamps = []
        for url in images_urls:
            print("Finding street lamps in image at {}".format(url))
            predictions = model.get_predictions(url, lamp_confidence_threshold)
            print("Found {} lamps".format(len(predictions)))
            total_street_lamps.extend(predictions)
        lamp_count = len(total_street_lamps)
    
        final_route_data.append({"id" : route_idx, "img_count" : len(images_urls), "lamp_count": lamp_count})
    print("---------------------------------------------------------------") 

    score_routes_relatively(final_route_data)
    score_routes_absolutey(final_route_data)

    return final_route_data


def score_routes_relatively(route_data):
    for route_dict in route_data:
        image_count = route_dict['img_count'] 
        lamp_count = route_dict['lamp_count']
        lamps_per_iamge = (0.0 + lamp_count) / image_count

        route_dict['score_rel'] = lamps_per_iamge 
    

def score_routes_absolutey(route_data): 
    """
    Will not append an asbolute score for now because i
    it is not implemented. 
    """
    pass