# Handbag Detection and Brand Recognition


 All the files are in the current directory, command below will apply object detection on the input image `bag.jpg`.
 
 `detectandcut.py` helps cut out the bounding box from an image, which is ready for further classification. It will finally output the image with bounding box and the brand name on it.
 
 `$ python detectcut.py --image bag.jpg --config handbag-tiny.cfg --weights handbag-tiny_5000.weights
 
## Yolo v3 
  ### sample input:
  ![](bag.jpg)

  ### sample cutted image :
   <img src="https://github.com/NYU-CDS-Capstone-Project/Fashion_Apparel_Detection/blob/master/Final_Product/data/test/1/cutted-image.jpg"/> 


## CNN

  ### sample input :
  <img src="https://github.com/NYU-CDS-Capstone-Project/Fashion_Apparel_Detection/blob/master/Final_Product/data/test/1/cutted-image.jpg"/> 

  ### sample output :
  Label:
  - Louis_Vuitton
  - balenciaga
  - burberry
  - chloe
  - coach
  - givenchy
  - gucci
  - longchamp
  - michaelkors
  - prada
  - saint laurent
  - valentino
  - unknown
  
## Final Output :
 <img src="https://github.com/NYU-CDS-Capstone-Project/Fashion_Apparel_Detection/blob/master/Final_Product/object-detection.jpg"/> 




 
 
