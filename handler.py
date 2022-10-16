from boto3 import client as boto3_client
import face_recognition
import pickle

input_bucket = "smart-classroom-input"
output_bucket = "smart-classroom-output"


# Function to read the 'encoding' file
def open_encoding(filename):
    file = open(filename, "rb")
    data = pickle.load(file)
    file.close()
    return data


def face_recognition_handler(event, context):
    return {
        "data": "test"
    }
