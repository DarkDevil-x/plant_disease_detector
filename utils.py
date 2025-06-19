import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

def load_model(path="model/plant_disease_model.h5"):
    return tf.keras.models.load_model(path)

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    return np.expand_dims(img_array, axis=0)