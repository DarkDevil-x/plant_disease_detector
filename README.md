# 🌿 AI-Based Plant Disease Detection Using Leaf Images

An AI-powered web app that detects plant diseases from leaf images using Convolutional Neural Networks (CNN).  
Designed to assist farmers and researchers in early disease detection through a simple, easy-to-use interface.

---

## 📌 Features

- 🧠 AI-driven plant disease detection
- 📸 Leaf image-based diagnosis
- 🧪 ~92% test accuracy
- 🌐 Streamlit web interface for instant results
- 📱 Easy to use for farmers and agriculture researchers

---

## 🔧 Tech Stack

- Python 3.x
- TensorFlow / Keras
- Streamlit
- NumPy, OpenCV, Pillow

---

## 📁 Project Structure

```
plant_disease_detector/
├── app.py                  # Streamlit web app
├── train_model.py          # Script to train the CNN model
├── utils.py                # Helper functions for model loading and image preprocessing
├── requirements.txt        # List of required Python packages
├── README.md               # Documentation
├── model/
│   └── plant_disease_model.h5  # Trained model file
└── dataset/
    └── [Your training dataset folders]
```


---

## 📦 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/DarkDevil-x/plant_disease_detector.git
cd plant_disease_detector
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the app
bash
Copy
Edit
streamlit run app.py
🧠 Model Training
To train the model from scratch:

Download the PlantVillage Dataset

Extract it into the dataset/ directory

Run the training script:

bash
Copy
Edit
python train_model.py
This will generate a model file at model/plant_disease_model.h5

🖼️ Sample Predictions
Input Image	Predicted Output
Tomato Leaf (infected)	Tomato___Early_blight
Tomato Leaf (healthy)	Tomato___Healthy

📈 Accuracy
Achieved ~92% validation accuracy using CNN

Improved using data augmentation and dropout

Can be further enhanced with hyperparameter tuning and more data

🔮 Future Scope
Support for more crop types and diseases

Integration with mobile cameras for field use

Offline prediction using TFLite

Voice support and multilingual interface

Drone-based scanning for large farmlands

🙋‍♂️ Author
Himanshu Singh
Department of Computer Science & Engineering
📧 [Your Email]
🔗 GitHub: DarkDevil-x
