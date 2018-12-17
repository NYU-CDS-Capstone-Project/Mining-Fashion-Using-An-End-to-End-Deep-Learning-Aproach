## Handbag Brand Detection

This is used for handbag brand detection. Given an image of handbag, we train a neural network to predict the corresponding brand of the bag.

Convolutional Neural Network is the state-of-art method for image classification. There are a lot of frameworks which can be directly used for this task, including AlexNet, ResNet, VGG, DenseNet and so on. We can load the pre-trained embediings from pytorch easily.

After loading the pre-trained embeddings, we can modify the prototype according to our use case. 

The code is referred to https://github.com/affromero/CNN-Classifier-Pytorch.

We also thank Hearst for providing us with testing image data to test our model. 
