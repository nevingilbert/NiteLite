import azure_custom_vision
import maps, yaml, safety
from flask import Flask, json

test = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(test)

if __name__ == "__main__":
    api.run()
    # origin = "clough undergraduate learning commons"
    # dest = "georgia tech campus recreation center"

    # route_dict = safety.compute_data_all_routes(origin.replace(' ', '+'), dest.replace(' ', '+'))
    # for route in route_dict:
    #     print('Route {} - Score {}'.format(route['id'], route['score_rel']))