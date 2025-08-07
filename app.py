import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image

# Load your trained model
model = load_model('horse_human_classifier.keras')

st.title('Horse vs Human Classifier')

uploaded_file = st.file_uploader('Upload an Image...', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    try:
        # Open and display image
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded Image', use_container_width=True)

        # Preprocess image to (300,300,3)
        img = image.resize((300, 300))
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1, 300, 300, 3)

        # Predict
        prediction = model.predict(img_array)[0][0]

        # Calculate probabilities
        prob_human = prediction
        prob_horse = 1 - prediction

        # Display probabilities
        st.write("### Prediction probabilities:")
        st.write(f"Human: {prob_human:.2%}")
        st.write(f"Horse: {prob_horse:.2%}")

        # Determine label
        label = "Human" if prob_human > prob_horse else "Horse"
        st.write(f"### Predicted Label: {label}")

    except Exception as e:
        st.error(f"Error processing the image: {e}")

else:
    st.info('Please upload an image file.')
