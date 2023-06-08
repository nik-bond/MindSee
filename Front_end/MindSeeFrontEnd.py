import streamlit as st
import requests
import numpy as np
import pandas as pd
import requests
from mindsee.params import *
import openai
from pathlib import Path
from base64 import b64decode
import json
import os
from PIL import Image




st.markdown("""# MindSee
## Recreating images from MRI scans""")


Mi
# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slihe displayed lines

uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

#To show a brain scan pic

uploaded_image = st.image(uploaded_file)
brain_image = st.image(Image.open("images/brain_scan/7Re1.gif"))




if uploaded_file is None:
    response=None

else:
    #Converting image name to string to send to API
    uploaded_file_name_raw = str(uploaded_file)
    uploaded_file_name =  uploaded_file_name_raw.split(',')[1][6:]
    st.markdown(uploaded_file_name)

#Get request to the API
#Getting back the predicted captions from the Model
    params= {'image_name':uploaded_file_name}
    response=requests.get(API_URL, params=params).json()
    response = list(response.values())[0]
    response = ', '.join(response)
    st.markdown(response)


# # Dall E
# # Creating the Dalle image as a json file
# PROMPT = str(response)
# DATA_DIR = Path.cwd() / "responses"

# #creating directory for Dall E-json response
# DATA_DIR.mkdir(exist_ok=True)

# openai.api_key = OPENAI_KEY

# response = openai.Image.create(
#     prompt=PROMPT,
#     n=1,
#     size="256x256",
#     response_format="b64_json",
# )
# file_name = DATA_DIR / f"{PROMPT[:10]}-{response['created']}.json"

# with open(file_name, mode="w", encoding="utf-8") as file:
#     json.dump(response, file)

# #Converting and saving the image
# DATA_DIR = Path.cwd() / "responses"
# JSON_FILE = file_name
# IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem

# IMAGE_DIR.mkdir(parents=True, exist_ok=True)

# with open(JSON_FILE, mode="r", encoding="utf-8") as file:
#     response = json.load(file)

# for index, image_dict in enumerate(response["data"]):
#     image_data = b64decode(image_dict["b64_json"])
#     image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
#     st.image(image_data)
#     with open(image_file, mode="wb") as png:
#         png.write(image_data)


# # Display the Dall E image on Streamlit
