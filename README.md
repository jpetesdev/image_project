# image_project
Using PIL and OS Python modules to make bulk changes to image files.

Project Objectives:

The images received are in the wrong format:

    .tiff format
    Image resolution 192x192 pixel (too large)
    Rotated 90° anti-clockwise

The images required for the launch should be in this format:

    .jpeg format

    Image resolution 128x128 pixel

    Should be straight


Necessary image files to download. This command will download a zip file onto your computer. (Linux)

curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie






