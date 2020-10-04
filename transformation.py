from pycocotools.coco import COCO

import matplotlib.pyplot as plt
import cv2

import os
import numpy as np
import random


# In[50]:


cocoRoot="./person_keypoints_val2017.json"


# In[51]:


coco=COCO(cocoRoot)


# In[52]:



# In[53]:


# 利用getCatIds函数获取某个类别对应的ID，
# 这个函数可以实现更复杂的功能，请参考官方文档
ids = coco.getCatIds('person')[0]
print(f'"person" 对应的序号: {ids}')

# 利用loadCats获取序号对应的文字类别
# 这个函数可以实现更复杂的功能，请参考官方文档
cats = coco.loadCats(1)
print(f'"1" 对应的类别名称: {cats}')


# In[54]:


# 获取包含person的所有图片
imgIds = coco.getImgIds(catIds=[1])
print(f'包含person的图片共有：{len(imgIds)}张')


# In[55]:


# 获取包含dog的所有图片
id = coco.getCatIds(['person'])[0]
imgIds = coco.catToImgs[id]
print(f'包含person的图片共有：{len(imgIds)}张, 分别是：')
print(imgIds)


# In[70]:


lis1='brodarski-C_'


# In[71]:


lis2='_right.jpg'


# In[72]:


imgIds_modi=[]
for i in range(0,len(imgIds)):
   sum=lis1+imgIds[i]+lis2
   imgIds_modi.append(sum)
print(imgIds_modi)


# In[74]:

import os,shutil
fileDir='../deep-high-resolution-net.pytorch/data/coco/images/train201701'
tarDir='../deep-high-resolution-net.pytorch/data/coco/images/val201701'
for name in imgIds_modi:
    shutil.move(os.path.join(fileDir, name), os.path.join(tarDir, name))


# In[56]:

