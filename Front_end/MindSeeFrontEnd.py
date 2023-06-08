import streamlit as st
from st_clickable_images import clickable_images
import requests
import numpy as np
import pandas as pd
import requests
from mindsee.params import *
import openai
from pathlib import Path
import base64
import json
import os
import PIL






st.markdown("""# MindSee
# Recreating images from MRI scans""")


# To get a picture grid

image0 = "Front_end/sample_pics/photo-1518727818782-ed5341dbd476.jpeg"
image1= "Front_end/sample_pics/photo-1565130838609-c3a86655db61.jpeg"
image2= "Front_end/sample_pics/photo-1565372195458-9de0b320ef04.jpeg"
image3= "Front_end/sample_pics/photo-1582550945154-66ea8fff25e1.jpeg"
image4= "Front_end/sample_pics/photo-1591797442444-039f23ddcc14.jpeg"

st.markdown("### Click on an image")

images = []
for file in [image0, image1, image2, image3, image4]:
    with open(file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        # st.markdown(images)
        images.append(f"data:image/jpeg;base64,{encoded}")


clicked = clickable_images(
    images,
    titles=[f"Image #{str(i)}" for i in range(len(images))],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

if clicked < 0:
    uploaded_file = None
if clicked == 0:
    uploaded_file = image0
if clicked == 1:
    uploaded_file = image1
if clicked == 2:
    uploaded_file = image2
if clicked == 3:
    uploaded_file = image3
if clicked == 4:
    uploaded_file = image4


# #To show a brain scan pic
if uploaded_file is None:
    st.markdown("Click an image")
else:
    uploaded_image = st.image(uploaded_file)


# # brain_image = st.image(Image.open("images/brain_scan/7Re1.gif"))




if uploaded_file is None:
    response=None

else:
    #Converting image name to string to send to API
    uploaded_file_name = uploaded_file
    #uploaded_file_name =  uploaded_file_name_raw.split(',')[1][6:]
    st.markdown(uploaded_file_name)

#Get request to the API
#Getting back the predicted captions from the Model

    params= {'image_name':uploaded_file_name}
    response=requests.get(API_URL, params=params).json()
    response = list(response.values())[0]
    response = ', '.join(response)
    st.markdown(response)


# Dall E
# Creating the Dalle image as a json file
PROMPT = str(response)
DATA_DIR = Path.cwd() / "responses"

#creating directory for Dall E-json response
DATA_DIR.mkdir(exist_ok=True)

openai.api_key = OPENAI_KEY

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)
file_name = DATA_DIR / f"{PROMPT[:10]}-{response['created']}.json"

with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)

#Converting and saving the image
DATA_DIR = Path.cwd() / "responses"
JSON_FILE = file_name
IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

with open(JSON_FILE, mode="r", encoding="utf-8") as file:
    response = json.load(file)

for index, image_dict in enumerate(response["data"]):
    image_data = base64.b64decode(image_dict["b64_json"])
    image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
    st.image(image_data)
    with open(image_file, mode="wb") as png:
        png.write(image_data)


# # Display the Dall E image on Streamlit
