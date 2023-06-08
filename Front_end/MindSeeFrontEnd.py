import streamlit as st
import requests
import numpy as np
import pandas as pd
import requests
from mindsee.params import *




st.markdown("""# MindSee
## Recreating images from MRI scans""")



# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slihe displayed lines

uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file is None:
    response=None

else:
    #Converting image name to string to send to API
    uploaded_file_name_raw = str(uploaded_file)
    uploaded_file_name =  uploaded_file_name_raw.split(',')[1][6:]
    st.markdown(uploaded_file_name)

#Get request to the API
    params= {'image_name':uploaded_file_name}
    response=requests.get(API_URL, params=params).json()
    response = list(response.values())[0]

    st.markdown(response)
