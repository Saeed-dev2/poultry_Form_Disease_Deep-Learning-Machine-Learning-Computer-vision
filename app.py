import streamlit as st
import tensorflow as tf
import cv2
from PIL import Image, ImageOps
import numpy as np


@st.cache(allow_output_mutation=True)
def load_model():
  model = tf.keras.models.load_model("./model/mobilenetV2/mobilenetv2.h5", compile = False) 
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()


st.markdown("<h1 style='text-align: center; color: red;'>Poultry Diseases Identifier 🐣🐓💩 App Using Machine Learning</h1>", unsafe_allow_html=True)
st.title('')

file = st.file_uploader("You can check your poultry bird's health via Poultry Disease Identifier. This app helps to detect unhealthy diseases such as Coccidiosis, Salmonella, and Newcastle from image files of chicken feces.", type=["jpg", "png", "jpeg"])
st.set_option('deprecation.showfileUploaderEncoding', False)
 
def upload_predict(upload_image, model):
        classes = {'Coccidiosis': 0, 'Healthy': 1, 'NewCastleDisease': 2, 'Salmonella': 3}

        img = tf.keras.preprocessing.image.load_img(
          upload_image, 
          target_size=(128, 128))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array*1/255.)
        score = tf.nn.softmax(predictions[0])
        pred_class=[j for j in classes if classes[j] == np.argmax(score)][0]
        return pred_class, round(100 * np.max(score),2)
if file is None:
    st.text("Please Upload Your Poultry Bird Image File")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    image_class, score_preds = upload_predict(file, model)
    st.write("🐥The image is classified as",image_class)
    st.write("🐔The similarity score is approximately",score_preds)
    print("The image is classified as ",image_class, "with a similarity score of",score_preds)

st.markdown("<h3 style='text-align: center; color: Green;'>Identification and Classification of Poultry Diseases</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Green;'>By OMIDEYI, Damilare.A</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Green;'>18/27/PCS007</h3>", unsafe_allow_html=True)
