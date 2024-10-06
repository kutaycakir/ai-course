import streamlit as st
import pickle
from sklearn.neighbors import NearestNeighbors

with open('Images_features.pkl', 'rb') as f:
    image_features = pickle.load(f)

with open('filenames.pkl', 'rb') as f:
    filenames = pickle.load(f)

model = NearestNeighbors(n_neighbors=5, algorithm='brute', metric='euclidean')
model.fit(image_features)

st.title("Fashion Product Recommender")

selected_image = st.selectbox('Pick an image', filenames)

selected_index = filenames.index(selected_image)

distances, indices = model.kneighbors([image_features[selected_index]])


st.write("Here are similar products:")
for idx in indices[0]:
    st.write(filenames[idx])