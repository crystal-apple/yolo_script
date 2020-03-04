import cv2
from glob2 import glob

for fn in glob('*.jpg'): #确认文件格式
    img=cv2.imread(fn)
    horizontal_img=cv2.flip(img,1)#图像翻转
    #vertical_img=cv2.flip(img,0)
    splitName=fn.split(".")
    newName=splitName[0]
    cv2.imwrite(newName+'_flip_1.jpg',horizontal_img)

