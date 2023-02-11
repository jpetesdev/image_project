#!/usr/bin/python3

import os
import PIL
from os import listdir
from PIL import Image

with Image.open("./images/ic_local_pizza_black_48dp") as im:
        im.rotate(90).show()

image_dir = "./images"
output_dir = "new_images/"

#Iterates over each image in the folder they are stored in with the os module
for image in os.listdir(image_dir):
        if image != ".DS_Store":
                #Creates the full file path to image
                inputPath = os.path.join(image_dir, image)
                #Uses the Image module from PIL to open the image and then manipulate it.
                img = Image.open(inputPath)
                #Creates the new folder that the images will be stored in, but with the same file name
                fullOutPath = os.path.join(output_dir, image)
                img = img.rotate(-90)
                img = img.resize((128, 128))
                img = img.convert("RGB")
                #Saves the image as a .jpeg from original TIFF format. Had to convert prior in order to do that. 
                img = img.save(fullOutPath, format="JPEG")
