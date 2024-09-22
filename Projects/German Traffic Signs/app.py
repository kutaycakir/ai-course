import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('traffic_sign_model.h5')


def process_image(img):
    img = img.resize((32, 32))
    img = np.array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

st.title('GTSRB - German Traffic Sign Recognition')
st.write('Upload an image for Traffic Sign Recognition')
file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png', 'webp'])
picture = st.camera_input("Take a picture", )


classes = { 0:'Speed limit (20km/h)',
                1:'Speed limit (30km/h)',
                2:'Speed limit (50km/h)',
                3:'Speed limit (60km/h)',
                4:'Speed limit (70km/h)',
                5:'Speed limit (80km/h)',
                6:'End of speed limit (80km/h)',
                7:'Speed limit (100km/h)',
                8:'Speed limit (120km/h)',
                9:'No passing',
                10:'No passing veh over 3.5 tons',
                11:'Right-of-way at intersection',
                12:'Priority road',
                13:'Yield',
                14:'Stop',
                15:'No vehicles',
                16:'Veh > 3.5 tons prohibited',
                17:'No entry',
                18:'General caution',
                19:'Dangerous curve left',
                20:'Dangerous curve right',
                21:'Double curve',
                22:'Bumpy road',
                23:'Slippery road',
                24:'Road narrows on the right',
                25:'Road work',
                26:'Traffic signals',
                27:'Pedestrians',
                28:'Children crossing',
                29:'Bicycles crossing',
                30:'Beware of ice/snow',
                31:'Wild animals crossing',
                32:'End speed + passing limits',
                33:'Turn right ahead',
                34:'Turn left ahead',
                35:'Ahead only',
                36:'Go straight or right',
                37:'Go straight or left',
                38:'Keep right',
                39:'Keep left',
                40:'Roundabout mandatory',
                41:'End of no passing',
                42:'End no passing veh > 3.5 tons' }

if picture is not None:
    img = Image.open(picture)
    st.image(img, caption='Uploaded Image')
    image = process_image(img)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)

    st.write(f'Prediction: {classes[predicted_class]}')

if file is not None:
    img = Image.open(file)
    st.image(img, caption='Uploaded Image')
    image = process_image(img)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)

    st.write(f'Prediction: {classes[predicted_class]}')

    #Mobile entegre etmeyi beceremedim.