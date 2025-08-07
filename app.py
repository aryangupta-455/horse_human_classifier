import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('horse_human_classifier.keras')

st.title("Horse vs Human Classifier")
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded Image', use_column_width=True)
        img = image.resize((150, 150))
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1, 150, 150, 3)
        
        prediction = model.predict(img_array)[0][0]
        
        label = "Human" if prediction > 0.5 else "Horse"
        st.write(f"### Prediction: {label}")

    except Exception as e:
        st.error(f"Error processing the image: {e}")

else:
    st.info("Please upload an image file.")
