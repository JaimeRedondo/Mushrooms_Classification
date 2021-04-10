# Mushrooms Classification

There are many species of mushrooms in our environment, they are located in different wooded areas of our planet, one of the countries with more richness of mushrooms is our country, Spain. In this country there is a great deal of diversity, and we are going to study the mushrooms of one of the provinces where this biodiversity is most evident, Guadalajara. This project consists of identifying images of mushrooms from Guadalajara by applying Deep Learning, more specifically convolutional neural networks, specialised in image processing.

# Objective

Classify the different mushrooms of Guadalajara by images.

# Raw Data Description

## How to get the data and run the code

We will briefly explain what it consists of and how the dataset used for the project has been constructed.

The initial dataset consists of 150 images of each of the most interesting mushroom species found in Guadalajara, according to the page https://www.amivall.com/documentos/epmguadalajara.pdf, these images can be scraped with the code (Scraping_Mushrooms.ipynb) or through the Drive that I will upload to the repo which is the result of executing that code.

Then we will run the code Mushrooms_Classification.ipynb both to obtain new images, a technique to increase the number of images for each mushroom called Data Augmentation, and to train the neural network that will allow us to classify the images of each mushroom among the different types that exist.

