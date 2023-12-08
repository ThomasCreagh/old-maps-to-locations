import urllib.request 
from PIL import Image 
import os
  
# url = r"https://griffiths.askaboutireland.ie/gv4/single_layer/tiles/16/31664/20824.jpg"
base_url = "https://griffiths.askaboutireland.ie/gv4/single_layer/tiles/16"
# folder = "31664"
# name = "20824"
IMAGE_SIZE = 30

START_NAME = 20824
START_FOLDER = 31664

GET_IMAGES = True

if not os.path.isdir(f"data"):
    os.mkdir(f"data") 

if not os.path.isdir(f"data/stich"):
    os.mkdir(f"data/stich") 

if GET_IMAGES:
    for name in range(START_NAME, START_NAME+IMAGE_SIZE):
        for folder in range(START_FOLDER, START_FOLDER+IMAGE_SIZE):
            if not os.path.isdir(f"data/{folder}"):
                os.mkdir(f"data/{folder}") 

            url = f"{base_url}/{folder}/{name}.jpg"
            print(url)

            horizontal = int(name)-START_NAME

            image_1_name = f"stich/{name-START_NAME}"
            image_2_name = f"{folder}/{name}"

            if not os.path.exists(f"data/{folder}/{name}.png"):
                urllib.request.urlretrieve(url, f"data/{folder}/{name}.png") 

            if folder == START_FOLDER:
                continue

            if folder == START_FOLDER+1:
                image_1_name = f"{folder-1}/{name}"

            if not os.path.exists(f"data/stich/{horizontal}.png"):
                file = open(f"data/stich/{horizontal}.png", "w")
                file.write("0")
                file.close()

            image_1 = Image.open(f"data/{image_1_name}.png")
            image_2 = Image.open(f"data/{image_2_name}.png")

            width = image_1.width + image_2.width
            height = max(image_1.height, image_2.height)

            stitched_image = Image.new('RGB', (width, height))

            stitched_image.paste(image_1, (0, 0))
            stitched_image.paste(image_2, (image_1.width, 0))           

            stitched_image.save(f"data/stich/{horizontal}.png")


for i in range(1, IMAGE_SIZE):
    image_1_name = f"stich"
    image_2_name = f"stich/{i}"

    if i == 1:
        image_1_name = "stich/0"

    image_1 = Image.open(f"data/{image_1_name}.png")
    image_2 = Image.open(f"data/{image_2_name}.png")

    width = max(image_1.width, image_2.width)
    height = image_1.height + image_2.height

    stitched_image = Image.new('RGB', (width, height))

    stitched_image.paste(image_1, (0, 0))
    stitched_image.paste(image_2, (0, image_1.height))           

    if not os.path.exists(f"data/stich.png"):
        file = open(f"data/stich.png", "w")
        file.write("0")
        file.close()

    stitched_image.save(f"data/stich.png")
