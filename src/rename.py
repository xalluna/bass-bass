#! /usr/bin/python

# import the necessary packages
from imutils import paths
from pathlib import Path
#import argparse
import cv2

imagePaths = list(paths.list_images("dataset\\Paosrc"))

path = Path(__file__).parent.joinpath('songs\\Pao')
if(not path.exists()):
	path.mkdir(0, True)

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    img_name = f"{path}\\image_{i}.jpg"
    print(img_name)
    image = cv2.imread(imagePath)
    cv2.imwrite(img_name, image)
    print(f"{img_name} written!")
	# extract the person name from the image path
	# print("[INFO] processing image {}/{}".format(i + 1,
	# 	len(imagePaths)))
	# name = imagePath.split(os.path.sep)[-2]

