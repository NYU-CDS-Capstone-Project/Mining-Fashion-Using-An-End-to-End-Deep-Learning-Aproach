# NYU-Hearst
# Review of Deep Learning Algorithms for Object Detection
## Introduction
Hearst owns one of the world's largest pulisher of monthly magazines in multiple fields including fashion, cars, composition, food, room decorations and etc. Objct Detection/Localization is important for such a big magazine publishr to search for similar images and locate particular objects. As computer vision has grown by leaps and bouds, we are now able to use it as a tool to scan images and accurately identify objects and components within them. Particularly, we are attempt to create a tool for Hearst that can scan images and videos for metadata to recognize objects in images that are then searchable within their explore function.

Currently, Hearst has a basic model which the model will search for pictures of similar objects when input an image of a particular object, and our task is to improve the model such that the model can find not only the object image, but also the images containing the object as an embedding. There are currently several models that can appropriate identify relevant objects in a single image and the localization of the objects. We will try to implement them with our selected data for one of the Heast Magazine topic and compare their performance and accuracy. Our work will be evaluated on Heast internal dataset with their basic model as baseline. 


## Dataset
The Open Images Dataset is a well-known dataset for object detection, classification, segmentation of objects. The newest version V4 is realeased on 30th April 2018 with 15.4M bounding-boxes for 600 categories on 1.9M images, making it the largest existing dataset with object location annotations. And we plan to filter handbag images as our targed classes for Heast fashion magazines.


## Algorithms
We will try several state-of-the art of object detection models including but not limited to:

1. R-CNN
2. Fast R-CNN
3. Yolo
4. SSD

and our analysis criteria will be on their performance and accuracy. 

## To Do List:
Frist Stage: Dataset and Research
- [x] Filtered out Handbag/ Handbag embedded images from the Open Images Dataset where there are total categories in total.
- [x] Explored potential algorithems for object detection: including models such as R-CNN, Fast R-CNN, Yolo, SSD.

Second Stage: try different algorithms on sub sample with correct input format.
- [x] SSD:
  - [x] preprocessing our handbag dataset to an acceptable format for SSD model
  - [x] train bounding box using SSD model
- [ ] YOLO:
  - [ ] preprocessing our handbag dataset to an acceptable format to <object-class> <x> <y> <width> <height>
  - [ ] train bounding box using YOLO
- [ ] R-CNN:
  - [ ] preprocessing our handbag dataset to an acceptable format
  - [ ] train bounding box using R-CNN
- [ ] Fast R-CNN
  - [ ] preprocessing our handbag dataset to an acceptable format
  - [ ]train bounding box using Fast R-CNN
  
Third Stage: 
- [ ] Run all algorithms on full handbag dataset and construct a system that records the performance and evaluation score.

Fourth Stage:
- [ ] Test the best model on Hearst Handbag dataset.

Fifth Stage (optional):
- [ ] Construct a handbag brand detection model.

