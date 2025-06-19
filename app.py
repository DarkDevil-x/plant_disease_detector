import streamlit as st
from utils import load_model, preprocess_image
import os

model = load_model()
CLASS_NAMES = ['Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Healthy']

st.title("🌿 AI Plant Disease Detector")
uploaded_file = st.file_uploader("Upload a leaf image", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    img_array = preprocess_image("temp.jpg")
    prediction = model.predict(img_array)
    predicted_class = CLASS_NAMES[prediction.argmax()]
    st.success(f"✅ Prediction: **{predicted_class}**")
    os.remove("temp.jpg")