# NYU-Hearst
# Handbag Detection and Brand Recognition
## Introduction
Hearst owns one of the world's largest pulisher of monthly magazines in multiple fields including fashion, cars, composition, food, room decorations and etc. Objct Detection/Localization is important for such a big magazine publishr to search for similar images and locate particular objects. As computer vision has grown by leaps and bouds, we are now able to use it as a tool to scan images and accurately identify objects and components within them. Particularly, we are attempt to create a tool for Hearst that can scan images and videos for metadata to recognize objects in images that are then searchable within their explore function.

Currently, Hearst has a basic model which the model will search for pictures of similar objects when input an image of a particular object, and our task is to improve the model such that the model can find not only the object image, but also the images containing the object as an embedding. There are currently several models that can appropriate identify relevant objects in a single image and the localization of the objects. We will try to implement them with our selected data for one of the Heast Magazine topic (Handbag) and compare their performance and accuracy. In addition, after the localization of the handbag, we will build a classfier to detect the speicific brand.Our work will be evaluated on Heast internal dataset with their basic model as baseline. 



## Dataset
The Open Images Dataset is a well-known dataset for object detection, classification, segmentation of objects. The newest version V4 is realeased on 30th April 2018 with 15.4M bounding-boxes for 600 categories on 1.9M images, making it the largest existing dataset with object location annotations. Handbag images are filtered out as our targed classes to train the localization model. 

For the brand recognition classifier, we downloaded around 20 classes of brands with around 600 images in each brand from website.


## Algorithms
We will try several state-of-the art of object detection models including but not limited to Yolo v3 and SSD, which are the most recent algorithms, and our analysis criteria will be on their performance and accuracy. 
Next, we are going to build a CNN for brand recognition with initialized embedding weights from ResNet.

## To Do List:
Frist Stage: Dataset and Research
- [x] Filtered out Handbag/ Handbag embedded images from the Open Images Dataset where there are total categories in total.
- [x] Explored potential algorithems for object detection: including models such as Yolo, SSD.

Second Stage: try different algorithms on sub sample with correct input format.
- [x] SSD:
  - [x] preprocessing our handbag dataset to an acceptable format for SSD model
  - [x] train bounding box using SSD model
- [x] YOLO:
  - [x] preprocessing our handbag dataset to an acceptable format to <object-class> <x> <y> <width> <height>
  - [x] train bounding box using YOLO
  
Third Stage: 
- [x] Run all algorithms on full handbag dataset and construct a system that records the performance and evaluation score.

Fourth Stage:
- [x] Build a handbag brand recognition model.

Fifth Stage:
- [ ] Construct the whole pipeline which is able to localize the handbag in the input image and then detect the speicifc brand of the handbag.
- [ ] Test the whole pipeline on Hearst Handbag dataset.


