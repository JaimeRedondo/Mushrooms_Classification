# Mushrooms Classification

There are many species of mushrooms in our environment, they are located in different wooded areas of our planet, one of the countries with more richness of mushrooms is our country, Spain. In this country there is a great deal of diversity, and we are going to study the mushrooms of one of the provinces where this biodiversity is most evident, Guadalajara. This project consists of identifying images of mushrooms from Guadalajara by applying Deep Learning, more specifically convolutional neural networks, specialised in image processing.

# Objective

Classify the different mushrooms of Guadalajara by images, the code is made so that it can be done for 540 mushrooms from all the regions of spain, or almost 60 mushrooms in Guadalajara , is your election.

# How to get the data and run the code

We will briefly explain what it consists of and how the dataset used for the project has been constructed.

The dataset used for the project consists of 150 images of each of the most interesting mushroom species found in Guadalajara, according to the page https://www.amivall.com/documentos/epmguadalajara.pdf, if you don´t want to use this dataset, these images can be scraped with the code (Scraping_Mushrooms.ipynb) where you can choose if you want Guadalajara Mushrooms or All regions in Spain, and also you will choose the number of photos per mushroom you want and where you want to save it (you will need to specify a route to save the images). For the execution of the project we have chosen 150 photos per mushroom of the mushrooms of Guadalajara.

Then we will run the code Mushrooms_Classification.ipynb to obtain new images, a technique to increase the number of images for each mushroom called Data Augmentation, and to train the neural network that will allow us to classify the images of each mushroom among the different types that exist.

After this we will test the neural network, and later we choose a photo form internet and give the network trained a photo , this photo will have 3 possible mushrooms as a response with a certain percentage each from highest to lowest on which mushrooms they can be.

And with that we finished this manual to play with this project!

Welcome andd enjoy the project!
