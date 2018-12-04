#############################################
# Object detection - YOLO - OpenCV
# Original Author : Arun Ponnusamy   (July 16, 2018)
# Website : http://www.arunponnusamy.com
############################################

import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torch.utils.data.sampler import SubsetRandomSampler
from model import *
from PIL import Image
import os


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help = 'path to input image')
ap.add_argument('-c', '--config', required=True,
                help = 'path to yolo config file')
ap.add_argument('-w', '--weights', required=True,
                help = 'path to yolo pre-trained weights')
#ap.add_argument('-cl', '--classes', required=True,
#                help = 'path to text file containing class names')
args = ap.parse_args()


def get_output_layers(net):
    
    layer_names = net.getLayerNames()
    
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers


def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):

    label = str(outcome)

    color = COLORS[0]

    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    
image = cv2.imread(args.image)

Width = image.shape[1]
Height = image.shape[0]
scale = 0.00392

#classes = None
#
#with open(args.classes, 'r') as f:
#    classes = [line.strip() for line in f.readlines()]

COLORS = np.random.uniform(0, 255,  3)

net = cv2.dnn.readNet(args.weights, args.config)

blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

net.setInput(blob)

outs = net.forward(get_output_layers(net))

class_ids = []
confidences = []
boxes = []
conf_threshold = 0.5
nms_threshold = 0.4


for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * Width)
            center_y = int(detection[1] * Height)
            w = int(detection[2] * Width)
            h = int(detection[3] * Height)
            x = center_x - w / 2
            y = center_y - h / 2
            class_ids.append(class_id)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])


indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)


def crop(image, x, y, w, h):
    return image[y:y+h , x:x+w, :]


save_dir = "/Users/yuxiong/Desktop/Capstone/Fashion_Apparel_Detection/Final_Product/data/test"
model_path= "/Users/yuxiong/Desktop/Capstone/Fashion_Apparel_Detection/Final_Product/CNN-Classifier-Pytorch/0012.pth"


dic = {}
for i in indices:
    i = i[0]
    box = boxes[i]
    x = box[0]
    y = box[1]
    w = box[2]
    h = box[3]
    cv2.imwrite(os.path.join(save_dir,"1/cutted-image.jpg"), crop(image, int(x), int(y), int(w), int(h)))
#    print(class_ids[i], confidences[i], int(round(x)), round(y), round(x+w), round(y+h))


    ########################################################################################
    image_size = 224
    batch_size = 16
    num_workers = 4
    brand=['Louis_Vuitton','balenciaga','burberry','chloe','coach','givenchy','gucci','longchamp',
           'michaelkors','prada','saint laurent','unknown','valentino']

    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])
    transform_test = transforms.Compose([transforms.Resize((image_size, image_size), interpolation=Image.ANTIALIAS),transforms.ToTensor(),normalize])
    data_test = datasets.ImageFolder(save_dir, transform=transform_test)
    test_loader = torch.utils.data.DataLoader(data_test, batch_size=batch_size,
                                              shuffle=False,
                                              num_workers=num_workers)

    model = get_model(model_path, 13)
    optimizer = torch.optim.Adam(model.parameters(), 0.001, [0.5, 0.999])
    model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage))

    def solver(data_loader, model):
        model.eval()
        
        count_test = 0
        test_out = []
        
        for batch_idx, (data,target) in enumerate(data_loader):
            #data = Variable(data, volatile=True)
            output = model(data)
            _, arg_max_out = torch.max(output.data.cpu(), 1)
            
            
            for oo in arg_max_out:
                test_out.append('%s,%d\n'%(str(count_test).zfill(4), oo))
                count_test+=1

        return brand[int(test_out[0].split(",")[1])]

    def test(test_loader, model):
        #assert start_epoch>0, "you must first TRAIN"
        #solver(config.model, val_loader, model,  mode='val')
        return solver(test_loader, model)

    outcome = test(test_loader, model)
    
    ############################################################################################

    draw_prediction(image, outcome, confidences[i], int(round(x)), int(round(y)), int(round(x+w)), int(round(y+h)))
    


cv2.imshow("object detection", image)
cv2.waitKey(5000)
    
cv2.imwrite("object-detection.jpg", image)
cv2.destroyAllWindows()



