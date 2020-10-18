from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import yaml

class Custom_Vision:
    def __init__(self, endpoint, prediction_key, project_id, publish_iteration_name):
        
        self.project_id = project_id
        self.publish_iteration_name = publish_iteration_name

        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        self.predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)
    
    def get_predictions(self, url, threshold):
        results = self.predictor.detect_image_url(self.project_id, self.publish_iteration_name, url)
        return [prediction for prediction in results.predictions if prediction.probability > threshold]


if __name__ == "__main__":

    with open(r'credentials.yaml') as  file:
            credentials = yaml.load(file, Loader=yaml.BaseLoader)

    endpoint = credentials['custom_vision']['endpoint']
    prediction_key = credentials['custom_vision']['prediction_key']
    project_id = credentials['custom_vision']['id']
    publish_iteration_name = credentials['custom_vision']['name']

    url = 'https://i.ebayimg.com/images/g/FEUAAOSwZUFb8xMC/s-l300.jpg'

    model = Custom_Vision(endpoint, prediction_key, project_id, publish_iteration_name)
    results = model.get_predictions(url, 0.15)

    # Display the results.    
    for prediction in results:
        print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))