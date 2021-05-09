# Mushrooms Classification

There are many species of mushrooms in our environment, they are located in different wooded areas of our planet, one of the countries with more richness of mushrooms is our country, Spain. In this country there is a great deal of diversity, and we are going to study the mushrooms of one of the provinces where this biodiversity is most evident, Guadalajara. This project consists of identifying images of mushrooms from Guadalajara by applying Deep Learning, more specifically convolutional neural networks, specialised in image processing.

# Objective

Classify mushrooms, you can choose between All Regions and only Guadalajara Regions as we will explain later. In our case, the dataset used is 150 images per mushrooms from Guadalajara Region (almost 50 mushrooms).

# How to get the data and run the code

We will briefly explain what it consists of and how the dataset used for the project has been constructed.

The dataset used for the project consists of 150 images of each of the most interesting mushroom species found in Guadalajara, according to the page https://www.amivall.com/documentos/epmguadalajara.pdf, if you don´t want to use this dataset, these images can be scraped with the code (Scraping_Mushrooms.ipynb) where you can choose if you want Guadalajara Mushrooms or All regions in Spain, and also you will choose the number of photos per mushroom you want and where you want to save it (you will need to specify a route to save the images), if you choose Default as the route, then, you will choose your current path. For the execution of the project we have chosen 150 photos per mushroom of the mushrooms of Guadalajara. 

The script Scraping_Mushrooms.ipynb is in the repo and you can download, after this you can run it from the main script (Mushrooms_Classification.ipynb) in the section ("Getting the data") when it ask you if you want to "Scrape_Mushrooms" or "Use_data". You will choose between scraping the mushrooms for your own with the parameters that we specified in the paragraph above (Guadalajara or All regions, path to save the photos, number of photos per mushroom) or, on the other hand, if you choose Use_data option you will have access to your files to download the data (Drive that I have)

Then we ccontinue running the code Mushrooms_Classification.ipynb to obtain new images, a technique to increase the number of images for each mushroom called Data Augmentation, and to train the neural network that will allow us to classify the images of each mushroom among the different types that exist.

After this we will test the neural network, and later we choose a photo from internet and give the network trained a photo , this photo will have 3 possible mushrooms as a response with a certain percentage each from highest to lowest on which mushrooms they can be.

In addition, a Front-End has been created using Streamlit, where you put a photo and automatically you wlll have the 3 mushrooms more similar to that photo with a graphic and its probabilities of being the mushroom given. 5 photos of the mushroom with the highest percentage probability of being the given photo will also be displayed.

And with that we finished this manual to play with this project!

Welcome and enjoy the project!

## For this project is needed

Jupyter notebook 

Google Colab

ZipFile ngrok-stable-linux-amd64.zip to use ngrok and run Streamlit (you will have on the repo)

Libraries and dependencies run on notebooks 
