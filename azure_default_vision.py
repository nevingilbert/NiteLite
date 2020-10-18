from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import yaml

class Basic_Vision:
    def __init__(self, subscription_key, endpoint):
        self.client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    
    def detect_objects(self, remote_image_url_objects):
        '''
        Detect Objects - remote
        This example detects different kinds of objects with bounding boxes in a remote image.
        '''
        print("===== Detect Objects - remote =====")
        print("Detecting objects in remote image:")
        # Call API with URL
        detect_objects_results_remote = self.client.detect_objects(remote_image_url_objects)

        # Print detected objects results with bounding boxes
        if len(detect_objects_results_remote.objects) == 0:
            print("No objects detected.")
        else:
            for object in detect_objects_results_remote.objects:
                print("{} at location {}, {}, {}, {}".format( object.object_property, \
                object.rectangle.x, object.rectangle.x + object.rectangle.w, \
                object.rectangle.y, object.rectangle.y + object.rectangle.h))
    
    def tag_image(self, remote_image_url_objects):
        print("===== Tag an image - remote =====")
        # Call API with remote image
        tags_result_remote = self.client.tag_image(remote_image_url_objects )

        # Print results with confidence score
        print("Tags in the remote image: ")
        if (len(tags_result_remote.tags) == 0):
            print("No tags detected.")
        else:
            for tag in tags_result_remote.tags:
                print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

if __name__ == "__main__":
    
    with open(r'credentials.yaml') as  file:
            credentials = yaml.load(file, Loader=yaml.BaseLoader)

    subscription_key = credentials['basic']['subscription_key']
    endpoint = credentials['basic']['endpoint']

    # Get URL image with different objects
    # remote_image_url_objects = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg"
    # remote_image_url_objects = "https://assets.atlasobscura.com/media/W1siZiIsInVwbG9hZHMvcGxhY2VfaW1hZ2VzLzFhY2M5ZTY2LTQxNjQtNDg4OS1iZWFkLWUzM2QxZTE4OTg4ZjNiYTg5ZDk1YmI4MDMwNmI3OF9nYXNsYW1wMS5KUEciXSxbInAiLCJ0aHVtYiIsIngzOTA-Il0sWyJwIiwiY29udmVydCIsIi1xdWFsaXR5IDgxIC1hdXRvLW9yaWVudCJdXQ/gaslamp1.JPG"
    remote_image_url_objects = "https://techcrunch.com/wp-content/uploads/2015/05/shutterstock_116263732.jpg"

    default_vision = Basic_Vision(subscription_key, endpoint)

    default_vision.detect_objects(remote_image_url_objects)
    default_vision.tag_image(remote_image_url_objects)