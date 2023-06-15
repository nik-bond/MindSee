
from fastapi import FastAPI
import pandas as pd
import numpy as np
from tensorflow.keras import models


app = FastAPI()


# Define a root `/` endpoint
@app.get('/')
def index():
    return {'project': 'MindSee'}

# Predict endpiont
@app.get('/predict_text')
def predict_text(image_name):
    image_name = int(image_name)

    #X_test = pd.read_csv('/Users/jakobduettmann/code/nik-bond/MindSee/data/X/X_df_scaled_FE.csv', index_col=0)
    X_test = pd.read_csv('/prod/data/X/X_df_scaled_FE.csv', index_col=0)

    #vocabulary_df = pd.read_csv('/Users/jakobduettmann/code/nik-bond/MindSee/data/y/vocabulary_df.csv', index_col=0)
    vocabulary_df = pd.read_csv('/prod/data/y/vocabulary_df.csv', index_col=0)


    #np.array(eval) is to make the list from the data frame back into an numpy array to plug it into the model
    x_fMRI=np.array(eval(X_test.at[image_name,'scaled_fMRI'])).reshape(1,-1)

    #loaded_model = models.load_model('/Users/jakobduettmann/code/nik-bond/MindSee/model/BaselineModelMark/model_mark_adjusted_val15_droupout_removed')
    loaded_model = models.load_model('/prod/model/BaselineModelMark/model_mark_adjusted_val15_droupout_removed')

    y_pred = loaded_model.predict(x_fMRI)
    caption_index=np.argpartition(y_pred[0],-4)[-4:]

    predicted_caption=list(vocabulary_df.columns[:][caption_index])
    # # # predicted_caption = ['banana', 'lobster']
    # Das muss bitte klappen
    return predicted_caption
