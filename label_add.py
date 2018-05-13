import pandas as pd
import csv
from os import listdir
from os.path import isfile, join
import numpy
import cv2

# define the label detection function
def detect_photo(listing_id, seq, index):

    import io
    import os


    from os import listdir
    from os.path import isfile, join

    # Imports the Google Cloud client library
    # [START migration_import]
    from google.cloud import vision
    from google.cloud.vision import types
    from google.protobuf.json_format import MessageToJson
    # [END migration_import]
    # Create the list
    label_list = []
    # Instantiates a client
    # [START migration_client]
    client = vision.ImageAnnotatorClient()
    # [END migration_client]

    file_name = os.path.join(
        os.path.dirname(__file__),
        'data/images', '%s', '%s-%s.jpg') % (listing_id, listing_id, seq)
    # load the image

    try:
        with io.open(file_name, 'rb') as image_file:
            if is_valid_jpg(file_name) == True:
                content = image_file.read()
                image = types.Image(content=content)
                listings.set_value(index, 'complete', 'True')
            else:
                # end function if the jpg file is not complete
                listings.set_value(index, 'complete', 'False')
                return
    except IOError:
        # some pictures in list don't exist in the folder
        listings.set_value(index, 'complete', 'not exist')
        return
    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    for label in labels:

        label_list.append(label.description)

    # Insert labels into the dataframe
    listings.set_value(index, 'labels', label_list)
    print (label_list)

    # serialize
    serialized = MessageToJson(response)

    # write
    file_name2 = os.path.join(
        os.path.dirname(__file__),
        'data/images', '%s', '%s-%s-label-detect.json') % (listing_id, listing_id, seq)
    text_file = open(file_name2, "w+")
    text_file.write(serialized)
    text_file.close()


def is_valid_jpg(jpg_file):
    #check whether the jpg file is complete. If the jpg is not complete, opencv will report Premature end of JPEG file
    if jpg_file.split('.')[-1].lower() == 'jpg':
        with open(jpg_file, 'rb') as f:
            try:
                f.seek(-2, 2)
                return f.read() == '\xff\xd9'
            except IOError:
                return False

    else:
        return True



# read the input csv file
listings = pd.read_csv('listings_updated.csv')
# add column 'labels'
listings['labels'] = ''



#listing_id = listings.get_value(0, 'listing_id')

#seq = listings.get_value(0, 'seq')

#detect_photo(listing_id, seq, 0)


for index in range(len(listings.index)):
    listing_id = listings.iat[index, 0]

    seq = listings.iat[index, 1]

    detect_photo(listing_id, seq, index)

    print (index, ' ', listing_id, ' ', seq)

    if index % 100 == 0:
        listings.to_csv('listings_updated.csv',index=False)
