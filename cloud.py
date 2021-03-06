import io
import os

from google.cloud import vision

client = vision.ImageAnnotatorClient()

file_name = os.path.abspath('loser.jpg')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.label_detection(image=image)
print(response)
labels = response.label_annotations
print(labels)
print('Labels:')

for label in labels:
    print(label.description)
