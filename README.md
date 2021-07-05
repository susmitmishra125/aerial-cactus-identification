# [Cactus Identification using Transfer Learning](https://www.kaggle.com/c/aerial-cactus-identification)

This is the source code for predicting whether a image contains a cactus or not. This project is inspired from the kaggle competition which aims to build a 
system for autonomous surveillance of protected areas. It tasked us with creation of an algorithm that can identify a specific type of cactus in aerial imagery.
## [Dataset](https://www.kaggle.com/c/aerial-cactus-identification/data)
This dataset contains a large number of 32 x 32 thumbnail images containing aerial photos of a columnar cactus (Neobuxbaumia tetetzo). Kaggle has resized the images from the original dataset to make them uniform in size. The file name of an image corresponds to its id.
## Methodology
In this project we want to recognise whether the image contains cactus or not.
For this we are going to construct a neural network with layers and train its weights.
Further we are going to use **Transfer Learning** which speeds up training by using pre-trained classification models. We are going to train only the top layer form the pretrained layers.
We are using pre-trained **MoblieNetV2** model feature detector which is released Google. For training the untrained layers we use TensorFlow 2.0 optimisers.

## Performance
After 30 epochs the model's validation accuracy increases form around 0.8 to 0.97.
Based on the accuracy and loss graphs, more epochs may result in even greater improvements.
![](images/accuracy.png)
![](images/cost.png)


![](demo.gif)

## References
1. This project is inspired from Transfer Learning using Pretrained ConvNets on [TensorFlow.org](https://www.tensorflow.org/tutorials/images/transfer_learning)
2. M. Sandler, A. Howard, M. Zhu, A. Zhmonginov, L. C. Chen, [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/pdf/1801.04381.pdf) (2019), Google Inc.

## API using heroku: [URL](https://aerial-cactus-identification.herokuapp.com/)
1. Created a api which takes image as input and returns whether the image is a cacuts image or not
2. Used Flask for creating the api and heroku for server
3. The server uses pickle file of the model we created using transfer Learing.
## Takeaway
The accuracy of the model can be further improved by finetuning the trained layers.