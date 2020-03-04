# coding:utf-8
import os
import shutil #复制文件
#读取路径下所有文件夹
#寻找文件夹下所有.jpg/.xml文件
#分别放入不同文件夹下


#添加路径
p1='input'
p2='test.avi'

#data_path=input("请输入数据集路径：")
data_path="/home/data/after"
pic_file_dir="/home/data/VOC2007/JPEGImages"
#pic_file_dir=input("拷入路径：")
#class_name=input("请输入该数据集分类：")
#clip_dataset_path='/home/data/syf/traincdw2014'
#data_path='/home/data/syf/bmdataset2014'
mmmm=1
#获取类别文件夹名称
for label in sorted(os.listdir(data_path)):
    nnn=1
    print(label)
    for fname in os.listdir(os.path.join(data_path,label)):#获取dataset类别文件夹名称
         #寻找文件夹下.jpg文件 .xml文件
        #xml_name=os.path.join(data_path,label,fname,'*.xml')
        if(fname[-3:]=='jpg'):
            pic_name=os.path.join(data_path,label,fname)
            #print(pic_name)
        #移动到新建的文件夹下
        shutil.move(pic_name,pic_file_dir)
       # print(mmmm)
        mmmm=mmmm+1  
print('finshed!!!!!!!!!!!!!!!')

'''
cap = cv2.VideoCapture('Board.avi')
if not cap.isOpened():
    print('video is not opened')
else:
    # 每秒25帧
    num = 0
    # 取10秒
    needTime = 100
    # 每10秒
    timeSpace = 100
    # 获取视频帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # AVI格式编码输出XVID
    videoWriter = cv2.VideoWriter('resultVideo_2.avi',cv2.VideoWriter_fourcc('X','V','I','D'),fps,frameSize=(320,288))
    while(1):
        success,frame = cap.read()
        if (num%timeSpace <= needTime):
            videoWriter.write(frame)
            print('write'+ str(num))
        num = num + 1
        if not success:
            print('finished')
            break
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cap.release()
'''
