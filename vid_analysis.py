import argparse
import sys
from google.cloud import videointelligence
import io
import os

os.system("export GOOGLE_APPLICATION_CREDENTIALS='google_application_credentials.json'")

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.enums.Feature.LABEL_DETECTION]

with io.open('output.mp4', 'rb') as movie:
    input_content = movie.read()
try:
    operation = video_client.annotate_video(features=features, input_content=input_content)
    print('\nProcessing video:')
    result = operation.result(timeout=90)
except Exception as err:
    print ("Video Intelligence error")
    print(err)
    exit()	

print('\nFinished processing.')

segment_labels = result.annotation_results[0].segment_label_annotations
for i, segment_label in enumerate(segment_labels):
    print('Video label description: {}'.format(segment_label.entity.description))
    for category_entity in segment_label.category_entities:
        print("Label category description: " +category_entity.description)	

    for i, segment in enumerate(segment_label.segments):
        confidence = segment.confidence
        print("The accuracy of the identification in this case is " +str(confidence) + "\n")
