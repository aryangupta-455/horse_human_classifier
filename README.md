# horse_human_classifier

# 🐴 Horse vs Human Classifier

This project is a deep learning-based image classifier that predicts whether an image contains a **horse**, **human**, or **both**.

It was built using TensorFlow/Keras and deployed using Streamlit for an easy-to-use web interface.

---

## 📌 Features

- Classifies images as:
  - Horse
  - Human
  - Both (if applicable, based on confidence)
- Simple Streamlit web interface for uploading and predicting
- Trained on custom dataset of horse and human images
- Model Demo: https://horsehumanclassifier-jfesubpmw5sbwux2wmgrqt.streamlit.app/
---

## 🛠️ Tech Stack

- 🧠 **Model**: TensorFlow / Keras
- 🐍 **Language**: Python
- 🖼️ **Image Handling**: PIL, NumPy
- 🌐 **Frontend**: Streamlit
- 🔢 **Model Format**: `.keras`

---

## 📁 Project Structure

│
├── disk-projects/ 
│
├── env/ # Virtual environment
│
├── app.py # Streamlit app for deployment
├── file_01.ipynb # Model training notebook
└── horse_human_classifier.keras
|__dataset
        |__human
        |__horse

## 🚀 Streamlit App

This project is deployed using **Streamlit Cloud**. To try the model live:

👉 **[🔗 Open Streamlit App](#)**  
_(Replace this with your actual Streamlit app link)_

---

## 🧪 Model Training

Model was trained using TensorFlow and Keras with a binary classification approach.

### Dataset:
- Custom dataset with:
  - `horse_images/`
  - `human_images/`
- Preprocessed to size `(150, 150)` and normalized

### Training Highlights:
- Binary Crossentropy Loss
- Adam Optimizer
- Accuracy as primary metric
- Saved as `horse_human_classifier.keras`

---

## 🖼️ How It Works

1. Upload an image using the Streamlit interface
2. The model resizes and preprocesses the image
3. Model makes a prediction and returns the label:
   - **"Horse"**
   - **"Human"**
   - Optionally both (if confidence split is detected — implementation-specific)


---

## ✅ To Finish This Up

To complete your README:

1. **Replace** the Streamlit app link:  
   `👉 [🔗 Open Streamlit App](#)`  
   → with your actual public link (e.g., `https://yourname.streamlit.app`)

2. (Optional) Add `requirements.txt` if you're uploading to GitHub or deploying.

Want me to generate a `requirements.txt` for your project too?




#Author
Aryan Gupta

