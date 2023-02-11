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

Afterunzipping the downloaded file, I wanted to take a look at the file types. Below is just a snippet of the output.

jesse@jesse-Latitude-E5470:~/Documents/GoogleIT/ImageProject/images$ file *
ic_add_location_black_48dp:            TIFF image data, little-endian, direntries=11, height=192, bps=8, compression=none, PhotometricIntepretation=BlackIsZero, width=192
ic_add_location_white_48dp:            TIFF image data, little-endian, direntries=11, height=192, bps=8, compression=none, PhotometricIntepretation=BlackIsZero, width=192

The downloaded images are indeed in the TIFF format. Their dimentions are 192x192. They are also rotated 90 degrees counter-clockwise (left)



