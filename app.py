import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import load_model
from PIL import Image

model = load_model('horse_human_classifier.keras')

st.title('Horse vs Human Classifier')

uploaded_file = st.file_uploader('Upload an Image...' , type = ['jpg','png','jpeg'])


if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption = 'upload image', use_column_width = True)

img = image.resize((150, 150))  # Resize to match model input
img_array = np.array(img) / 255.0
img_array = img_array.reshape(1, 150, 150, 3)

    # Predict
prediction = model.predict(img_array)[0][0]
label = "Human" if prediction > 0.5 else "Horse"

    # Show prediction
st.write(f"### Prediction: {label}")