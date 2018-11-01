import csv
from tqdm import tqdm

def get_class_index(classname):
    for l in csv.reader(open('class-descriptions-boxable.csv')):
        if l[1]!= classname:
            continue
        else:
            return l[0]

class_index = get_class_index('Handbag')


def get_text_file(annotation_filename):
    input_file = csv.DictReader(open(annotation_filename))

    for line in tqdm(list(input_file)):
        if line['LabelName'] != class_index:
            continue
        else:
            with open('../Dataset/train/Handbag/%s.txt'%line['ImageID'],'a') as f:
                x = (float(line['XMin']) + float(line['XMax']))/2.0 
                y = (float(line['YMin']) + float(line['YMax']))/2.0
                h = float(line['YMax']) - float(line['YMin'])
                w = float(line['XMax']) - float(line['XMin'])
                f.write(' '.join([str(0),str(x),str(y),str(w),str(h)])+'\n')


get_text_file("handbag_annotations.csv")
