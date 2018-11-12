## Dataset Dowloading

This folder introduces how to downloading Handbag dataset from the Open Image Dataset

#### Step 1: download OID dataset
```ruby
mkdir data
wget http://storage.googleapis.com/openimages/2017_07/images_2017_07.tar.gz
tar -xf images_2017_07.tar.gz
mv 2017_07 data/images
rm images_2017_07.tar.gz

wget http://storage.googleapis.com/openimages/2017_07/annotations_human_bbox_2017_07.tar.gz
tar -xf annotations_human_bbox_2017_07.tar.gz
mv 2017_07 data/bbox_annotations
rm annotations_human_bbox_2017_07.tar.gz

wget http://storage.googleapis.com/openimages/2017_07/classes_2017_07.tar.gz
tar -xf classes_2017_07.tar.gz
mv 2017_07 data/classes
rm classes_2017_07.tar.gz
```

#### Step 2: 
Keep only "/m/080hkjn" (indicates Handbag class) in the file ../data/classes/classes-bbox-trainable.txt

#### Step 3:
Run [Download_Handbag_Dataset.ipynb](https://github.com/NYU-CDS-Capstone-Project/Fashion_Apparel_Detection/blob/master/Downloading_Dataset/Download_Handbag_Dataset.ipynb)

Don't forget to change the directory path.
