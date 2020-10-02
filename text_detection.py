import boto3
#import json

#change photo to the path and file name of your image
photo = input("Enter the path and file name of image: ")

client = boto3.client('rekognition')

with open(photo, 'rb') as image:
    response = client.detect_text(
        Image = {'Bytes': image.read()}
    )

#print(response)
content = []
for text in response["TextDetections"]:
    if (text["Type"] == "WORD"):
        content.append(text["DetectedText"])

print(" ".join(content))

