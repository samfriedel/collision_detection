# Script to train a drone detector using dataset found here:
# https://www.kaggle.com/datasets/dasmehdixtr/drone-dataset-uav?resource=download-directory 
# USAGE: python3 train_detector.py -c {path to image directory} -a {path to annotation directory} -o {output path}

# import the necessary packages
from __future__ import print_function
from imutils import paths
from scipy.io import loadmat
from skimage import io
import argparse
import dlib
import sys

# handle Python 3 compatibility
if sys.version_info > (3,):
    long = int

# function to convert YOLO to LIST
def convert_format(box, iwidth = 256, iheight = 256):
    x = (iwidth*box[0]) - ((box[2]*iwidth)/2)
    y = (iheight*box[1]) - ((box[3]*iheight)/2)
    o_w = box[2]*iwidth
    o_h = box[3]*iheight
    return [x, y, o_w, o_h]

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--class", required=True,
    help="Path to the training class images")
ap.add_argument("-a", "--annotations", required=True,
    help="Path to the training class annotations")
ap.add_argument("-o", "--output", required=True,
    help="Path to the output detector")
args = vars(ap.parse_args())

# grab the default training options for our HOG + Linear SVM detector, then initialize the
# list of images and bounding boxes used to train the classifier
print("[INFO] gathering images and bounding boxes...")
options = dlib.simple_object_detector_training_options()
images = []
boxes = []

# loop over the image paths
for imagePath in paths.list_images(args["class"]):
    # extract the image ID from the image path and load the annotations file
    imageID = (imagePath.split("/")[1]).replace(".jpg", "")
    print(imageID)
    print(imagePath) 
    annotationPath = "{}/{}.txt".format(args["annotations"], imageID)
    with open(annotationPath) as p:
        lines = p.readlines()
        tmp_lst = lines[0].split(' ')
        startX = float(tmp_lst[1])
        startY = float(tmp_lst[2])
        endX = float(tmp_lst[3])
        endY = float(tmp_lst[4])
        
        boxes.append(convert_format([startX, startY, endX, endY]))
        print(boxes)

        # TODO: dataset annotations are either given in either xml or YOLO format.
        # YOLO format didn't work well with dlib, need to find a way to extract bounding boxes
        # from xml annotations to train drone detector.

    # add the image to the list of images
    images.append(io.imread(imagePath))

# train the object detector
print("[INFO] training detector...")
detector = dlib.train_simple_object_detector(images, boxes, options)

# dump the classifier to file
print("[INFO] dumping classifier to file...")
detector.save(args["output"])

