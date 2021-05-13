
### IMPORT LIBRARIES

### Streamlit
import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt

### Images
from matplotlib import image
from matplotlib import pyplot
from skimage import io
import cv2
import os
import skimage
from skimage import data, io, filters, transform
import numpy as np

### Load model
from keras.models import load_model

### Deep Learning
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import Input
import tensorflow as tf

### Random
import random 

### Web scraping packages
from bs4 import BeautifulSoup
import requests
import itertools
from urllib.request import Request, urlopen
import urllib.request

### Title, subheader and first paragraphs
st.title('Mushrooms Classification')
st.subheader('App to know what mushroom is your picture')
st.markdown("Hello everybody and welcome to this interactive website on **mushrooms classification**.")
st.markdown("This work consists on classifying different types of mushrooms from images, using the famous convolutional neural networks (CNN) as a method.")
st.markdown("Put a mushroom and get the probability that it is a type of mushroom among the different species studied, and you will also get the 3 most likely mushrooms it is.")
st.markdown("Please, put a picture of your choice")

### Load the model saved before.
model = load_model('model_mushrooms_SGD.h5')

### Read the mushrooms_labels.csv
l2 = pd.read_csv('mushrooms_labels.csv',sep='|')
l2 = l2['0'].to_list()

### Programming the App
try:

  ### Charge the picture of your choice
  picture = st.file_uploader('picture',type='jpg')

  ### Display the picture chosen in the app
  st.image(picture)

  ### Standarize pixels
  image_rgb=io.imread(picture)/255.0

  ### Resize photo, this time (28,28)
  data_picture = cv2.resize(image_rgb, (28, 28))

  ### Predict which mushroom is in the picture and giving the 3 more similar to it.
  pictures = np.array([data_picture])
  pred_photos = model.predict_proba(pictures)
  df = pd.DataFrame(pred_photos[0], columns = ['probabilities'])
  df['labels']=l2
  df_sort = df.sort_values('probabilities',ascending = False)[0:3]
  X=df_sort['probabilities']
  Y=df_sort['labels'] 

  ### Barplot with the information about the 3 mushrooms more similar to the one in the photo
  fig = plt.figure(figsize=(12, 8))
  plt.bar(range(len(X)), X)
  plt.xticks(np.arange(len(X)), Y)
  plt.ylabel('probability')
  ax = X.plot(kind='bar')
  ax.set_xticklabels(Y)
  rects = ax.patches
  for rect, label in zip(rects, X):
      height = rect.get_height()
      ax.text(rect.get_x() + rect.get_width() / 10, height+0.01, label,
              ha='left', va='bottom')
  st.pyplot(fig)

  ### Text with the percentage of accuracy and the mushroom more similar to the one in the photo
  probability = str(round(df_sort['probabilities'][:-2]*100,2).reset_index()['probabilities'][0])
  label = df_sort['labels'][:-2].reset_index()['labels'][0]
  text = f"Your choice has **{probability} %** to be **{label}** mushroom"
  st.markdown(text)

  ### Show pictures similars to the one that the model thinks is in the photo
  st.markdown("Here, you have other different pictures of this mushroom")
  
  url = 'https://www.google.com/search?q='+label+'&tbm=isch&hl=es&sa=X&ved=2ahUKEwjw_M7z2NfuAhUMpRoKHbPQAokQgowBegQIARAX&biw=1905&bih=852'
  response = requests.get(url)
  soup = BeautifulSoup(response.content,'html.parser')
  images = soup.find_all("img")         
  images = images[1::]
  random_photos = random.sample(images, 8)

  urls_list = []
  for image in random_photos:
    image_src = image['src']
    urls_list.append(image_src)

  st.image(urls_list)

except:
  pass