import azure_custom_vision
import maps, yaml, safety
from flask import Flask, json, request

processed_requests = []
api = Flask(__name__)

@api.route('/processed_requests', methods=['GET'])
def get_routes():
    return json.dumps(processed_requests)

@api.route('/processed_requests', methods=['POST'])
def post_route():
    origin = request.json['origin']
    dest = request.json['destination']
    
    route_dict = safety.compute_data_all_routes(origin.replace(' ', '+'), dest.replace(' ', '+'))
    
    processed_requests.append(route_dict)
    for route in route_dict:
        print('Route {} - Score {}'.format(route['id'], route['score_rel']))

    return json.dumps({"id": len(processed_requests) - 1}), 201

if __name__ == "__main__":
    api.run()
    # origin = "clough undergraduate learning commons"
    # dest = "georgia tech campus recreation center"

