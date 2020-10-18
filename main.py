import azure_custom_vision
import maps, yaml, safety

if __name__ == "__main__":
    origin = "clough undergraduate learning commons"
    dest = "georgia tech campus recreation center"

    route_dict = safety.compute_data_all_routes(origin.replace(' ', '+'), dest.replace(' ', '+'))
    for route in route_dict:
        print('Route {} - Score {}'.format(route['id'], route['score_rel']))