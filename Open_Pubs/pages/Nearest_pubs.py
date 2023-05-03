import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import os
from PIL import Image

st.set_page_config(layout="centered")


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
pic = os.path.join(dir_of_interest, "images", "2.jpg")
st.image(pic, width=700)


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


DATA_PATH = os.path.join(dir_of_interest, "data", "pub_df.csv")

pub_data=pd.read_csv(DATA_PATH)



st.markdown("<h1 style='text-align: center; color: #EB6864; font-weight: bold;'>🍺 Open Pubs Application 🍻</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #5243AA;'>Find the Nearest Pub</h2>", unsafe_allow_html=True)

# Allow user to enter their latitude and longitude
lat = st.number_input("Enter your latitude:", value=51.73)
lon = st.number_input("Enter your longitude:", value=-4.72)

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)

# Calculate the distance between the user's location and each pub in the dataset
pub_data['distance'] = pub_data.apply(lambda row: euclidean_distance(row['Latitude'], row['Longitude'], lat, lon), axis=1)

# Sort the dataset by distance and display the nearest 5 pubs
nearest_pubs = pub_data.sort_values(by='distance').head(5)
st.write(f"Displaying the 5 nearest pubs to your location (lat: {lat}, lon: {lon}):")
st.dataframe(nearest_pubs)

# Create a map centered on the user's location
m = folium.Map(location=[lat, lon], zoom_start=13)

# Add a marker for the user's location
folium.Marker(location=[lat, lon], icon=folium.Icon(color='red'), popup='Your Location').add_to(m)

# Add markers for each of the nearest pubs
marker_cluster = MarkerCluster().add_to(m)
for index, row in nearest_pubs.iterrows():
    Marker([row['Latitude'], row['Longitude']], popup=row['Name']).add_to(marker_cluster)

# Display the map
st.write("Map of the nearest pubs:")
folium_static(m)

# Add a footer with some information about the app
st.markdown("<hr>", unsafe_allow_html=True)
