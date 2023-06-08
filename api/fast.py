from fastapi import FastAPI

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'project': 'MindSee'}

# Predict endpiont
@app.get('/predict_text')
def predict_text(image_name):

    predicted_caption = ['cat','dog','goat']

    return {'predicted_caption':predicted_caption}
