import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model=load_model('my_cnn_model.h5')

def process_image(img):
    img=img.resize((170,170))
    img=np.array(img)
    img=img/255.0
    img=np.expand_dims(img,axis=0)
    return img

st.title('Cancer Image Classification :cancer:')
st.write("'Upload a picture and the module will guess you're cancer or not.")

file=st.file_uploader('Upload a Picture',type=['jpg','jpeg','png'])

if file is not None:
    img=Image.open(file)
    st.image(img,caption='Uploaded picture')
    image=process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)

    class_names=['Not Cancer','Cancer']
    st.write(f'Prediction: {class_names[predicted_class]}')