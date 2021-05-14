# Mushrooms Classification

There are many species of mushrooms located in different areas of our planet. In fact, it is said that one of the countries with more variety of mushrooms is our country, Spain. The purpose of this project is to study the mushrooms of one of the provinces where this biodiversity is most evident, Guadalajara. This project consists of identifying images of mushrooms from Guadalajara by applying Deep Learning, more specifically convolutional neural networks, specialised in image processing.

# Objective

The aim of this project is to classify different mushrooms. You have the possibility of choosing between All regions and only Guadalajara depending on your interest. The results for this project have been obtained with a dataset with 60 images per mushroom from Guadalajara region (almost 50 types of mushrooms).

# How to get the data and run the code

The repo contains different folders, Documentation (with TFM Memory), Packages (with Packages necessary to run the code) and Scripts (with the main script Mushrooms_Classification and also the code in Jupyter notebook Scraping_Mushrooms (code we use to get the data) , and also the app.py that is the code used for generating the Streamlit app in google colab).

We will briefly explain what it consists of and how the dataset used for the project has been constructed.

The dataset used for the project consists of 60 images of each of the most interesting mushroom species found in Guadalajara according to the page https://www.amivall.com/documentos/epmguadalajara.pdf, if you do not want to use this dataset, these images can be scraped with the code (Scraping_Mushrooms.ipynb) where you can choose if you want Guadalajara Mushrooms or All regions in Spain (if you choose All regions in Spain you need later to change parameters in the neural network, the neural network is designed to classify Guadalajara Mushrooms (60 images per mushroom), if you choose All regions, or more photos, or whatever, you need to design moreover a neural network that works to that problem). Also you will choose the number of photos per mushroom you want and where you want to save it (you will need to specify a route to save the images), if you choose Default as the route, then, you will choose your current path. For the execution of the project, we have chosen 60 photos per mushroom of the mushrooms of Guadalajara. 

The script Scraping_Mushrooms.ipynb is in the repo and can be downloaded, after this, you can run it from the main script (Mushrooms_Classification.ipynb) in the section ("Getting the data") when it asks you if you want to "Scrape_mushrooms" or "Use_data". You will choose between scraping the mushrooms by your own with the parameters that we specified in the paragraph above (Guadalajara or All regions, path to save the photos, number of photos per mushroom) or, on the other hand, if you choose Use_data option you will have access to your files to download the data (in Drive I have).

**As a reminder, the project is designed to do with mushrooms of Guadalajara and 60 images per mushroom, as the Dataset in Drive.**

Then, we continue running the code Mushrooms_Classification.ipynb to obtain new images (with Data Augmentation) and to train the neural network that will allow us to classify the images of each mushroom among the different types that exist.

After this, we will test the neural network. Later, we will choose a photo from the internet and give it to the trained neural network, this photo will have 3 possible mushrooms as a response with a certain percentage each from highest to lowest on which mushrooms they can be.

In addition, a Front-End has been created using Streamlit. In order to use this app you should to upload a photo of the mushrooms you want to classify. After that, you will have the 3 more similar mushrooms to that photo with a graphic and its probabilities of being the mushroom given. 8 photos of the mushroom with the highest percentage probability of being the given photo will also be displayed.

To run the app you need to execute the code, but if you want to run directly the app, in the repo you can find the files used in the app (the model (with the SGD optimizer) and the CSV with the mushrooms_labels).

Welcome and enjoy the project!!
