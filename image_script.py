#!/usr/bin/python3

import os
import PIL
import glob
from os import listdir
from PIL import Image

with Image.open("./images/ic_local_pizza_black_48dp") as im:
        im.rotate(90).show()

image_dir = "./images"

output_dir = "new_images/"

#images = glob.glob("./images/ic_*")

for image in os.listdir(image_dir):
        if image != ".DS_Store":
                inputPath = os.path.join(image_dir, image)
                img = Image.open(inputPath)
                #print(image)
                #print("Image exists")
                fullOutPath = os.path.join(output_dir, image)
                img = img.rotate(-90)
                img = img.resize((128, 128))
                img = img.convert("RGB")
                img = img.save(fullOutPath, format="JPEG")
