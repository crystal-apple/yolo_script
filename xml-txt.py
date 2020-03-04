import xml.etree.ElementTree as ET
from os import getcwd

# sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

# classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
#classes = ['filter stick','fluffy catkins','pipe tobacco','oil stain','soot','crap iron','glue scale','cigarette','glue','tobacco powder']
classes = ['others','tobacco_dust','pip_tobacco','filter stick','glue','scale','cigarette','normal']

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id, list_file):
    #in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
    in_file = open('/home/data/VOC%s/Annotations/%s.xml'%(year, image_id))
    out_file = open('/home/data/VOC%s/labels/%s.txt'%(year, image_id),'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = 0
        if obj.find('difficult') != None:
            difficult = int(obj.find('difficult').text) == 1
        if obj.find('Difficult') != None:
            difficult = difficult or int(obj.find('Difficult').text) == 1
            
        #difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        bb = convert((w,h),b)
        #list_file.write(" " + ",".join([str(a) for a in bb]) + ',' + str(cls_id))
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for year, image_set in sets:
    image_ids = open('/home/data/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('/home/jdh/meiling/darknet-back/data/%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('/home/data/VOC%s/JPEGImages/%s.jpg'%(year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

os.system("cat 2007_train.txt 2007_val.txt > train.txt")
#os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt > train.all.txt")


