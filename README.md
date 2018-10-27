# NYU-Hearst
# Review of Deep Learning Algorithms for Object Detection
## Introduction
Hearst owns one of the world's largest pulisher of monthly magazines in multiple fields including fashion, cars, composition, food, room decorations and etc. Objct Detection/Localization is important for such a big magazine publishr to search for similar images and locate particular objects. As computer vision has grown by leaps and bouds, we are now able to use it as a tool to scan images and accurately identify objects and components within them. Particularly, we are attempt to create a tool for Hearst that can scan images and videos for metadata to recognize objects in images that are then searchable within their explore function.

Currently, Hearst has a basic model which the model will search for pictures of similar objects when input an image of a particular object, and our task is to improve the model such that the model can find not only the object image, but also the images containing the object as an embedding. There are currently several models that can appropriate identify relevant objects in a single image and the localization of the objects. We will try to implement them with our selected data for one of the Heast Magazine topic and compare their performance and accuracy. Our work will be evaluated on Heast internal dataset with their basic model as baseline. 


## Dataset
The PASCAL Visual Object Classification (PASCAL VOC) dataset is a well-known dataset for object detection, classification, segmentation of objects. There are around 10 000 images for training and validation containing bounding boxes with objects with 20 categories and we plan to filter indoor furnitures as our targed classes for Country Living Magazine (Heast).

## Algorithms
We will try several state-of-the art of object detection models including but not limited to"

1. R-CNN
2. Fast R-CNN
3. Yolo
4. SSD
