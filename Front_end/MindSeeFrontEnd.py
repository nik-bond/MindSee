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
import glob, random







st.markdown("""# MindSee
# Recreating images from MRI scans""")



# To generate random 5 images from the folder
@st.cache_data(persist=True)
def get_images():

    random_image_lst= []
    for i in range(1000):
        file_path_type = ["Front_end/test_images_indexed/*.png"]
        images = glob.glob(random.choice(file_path_type))
        random_image = random.choice(images)
        # random_image_lst.append(random_image)
        if random_image not in random_image_lst:
            random_image_lst.append(random_image)
            if len(random_image_lst)==6:
                break

    return random_image_lst

random_image_list = get_images()

# To get a picture grid

images = []
for file in random_image_list:
    with open(file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        # st.markdown(images)
        images.append(f"data:image/png;base64,{encoded}")


clicked = clickable_images(
    images,
    titles=[f"Image #{str(i)}" for i in range(len(images))],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)
st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

if clicked==-1:
    uploaded_file = None
else:
    uploaded_file=random_image_list[clicked]

# st.markdown(uploaded_file)


@st.cache_data
def square(x):
    return x**2

@st.cache_data
def cube(x):
    return x**3

if st.button("Generate New Images"):

    # Clear values from *all* all in-memory and on-disk data caches:
    # i.e. clear values from both square and cube
    st.cache_data.clear()



if uploaded_file is None:
    st.markdown("Click an image")
else:
    uploaded_image = st.image(uploaded_file)

# # #To show a brain scan pic
# brain_image = st.image(Image.open("images/brain_scan/7Re1.gif"))

if uploaded_file is None:
    response=None

else:
    # #Converting image name to string to send to API
    uploaded_file_name = uploaded_file

    uploaded_file_name = uploaded_file_name.rsplit('/', 1)[-1]

    uploaded_file_index = int(uploaded_file_name.rsplit(".png", 1)[0])
    st.markdown(uploaded_file_index)
    st.markdown(type(uploaded_file_index))
    st.markdown(uploaded_file_name)
    data=pd.read_csv("../MindSee/df_test.csv")
    data=data.set_index("Image_index")
    PROMPT = data.loc[uploaded_file_index,'test_caps_processed']
    st.markdown(PROMPT)
# uploaded_file_name = uploaded_file_name.rsplit('/', 1)[-1]






# Get request to the API
# Getting back the predicted captions from the Model

# params= {'image_name':"a,b,c"}
# response=requests.get(API_URL, params=params).json()
# response = list(response.values())[0]
# response = ', '.join(response)
# st.markdown(response)

# Dall E

# if uploaded_file is not None:

#     ## Creating the Dalle image as a json file
#     # PROMPT = response
#     DATA_DIR = Path.cwd() / "responses"

#     #creating directory for Dall E-json response
#     DATA_DIR.mkdir(exist_ok=True)

#     openai.api_key = OPENAI_KEY

#     response = openai.Image.create(
#         prompt=PROMPT,
#         n=1,
#         size="512x512",
#         response_format="b64_json",
#     )
    # file_name = DATA_DIR / f"{PROMPT[:10]}-{response['created']}.json"

    # with open(file_name, mode="w", encoding="utf-8") as file:
    #     json.dump(response, file)

    # ##Converting and saving the image
    # DATA_DIR = Path.cwd() / "responses"
    # JSON_FILE = file_name
    # IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem

    # IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    # with open(JSON_FILE, mode="r", encoding="utf-8") as file:
    #     response = json.load(file)

    # for index, image_dict in enumerate(response["data"]):
    #     image_data = base64.b64decode(image_dict["b64_json"])
    #     image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
    #     st.image(image_data)
    #     with open(image_file, mode="wb") as png:
    #         png.write(image_data)


# # # Display the Dall E image on Streamlit
