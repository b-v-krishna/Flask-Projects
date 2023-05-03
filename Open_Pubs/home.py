import streamlit as st
import pandas as pd
from matplotlib import image
from PIL import Image
import os

st.set_page_config(layout="centered")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pic = Image.open(os.path.join(BASE_DIR, 'resources/images/1.jpg'))
st.image(pic, width=700)

st.title(':red[Welcome to Open Pub Application]')

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "IMDb_Data_final.csv")

pub_df=pd.read_csv(DATA_PATH)


st.write('This page displays information and statistics about pubs in the UK.')

option = st.radio(
    "Select option",
    ('Head', 'Shape','Maxlatitude','Minlatitude','Maxlongitude','Minlongitude','Postcode','Authority'))

if option == 'Head':
    st.write(pub_df.head())
elif option=='Shape':
    st.write('The shape of dataframe is: ',pub_df.shape)
elif option=='Maxlatitude':
    st.write('The max latitude is: ',pub_df.Latitude.max())
elif option=='Minlatitude':
    st.write('The min latitude is: ',pub_df.Latitude.min())
elif option=='Maxlongitude':
    st.write('The max longitude is: ',pub_df.Longitude.max())
elif option=='Minlongitude':
    st.write('The min longitude is: ',pub_df.Latitude.min())
elif option=='Postcode':
    st.write('The unique postcodes: ',pub_df.PostCode.nunique())
elif option == 'Authority':
    unique_authorities = pub_df.Local_Authority.value_counts()[:20]
    st.write('The unique authorities: ')
    st.bar_chart(unique_authorities)




            

