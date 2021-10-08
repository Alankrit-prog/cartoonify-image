#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
image = cv2.imread(r"C:\Users\Lenovo\Desktop\t5mex3dyn30xi3ox6ii5.jpg")

if(image is not None):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 1)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY, 11, 11)
    color = cv2.bilateralFilter(image, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imwrite("Cartoon.jpeg",cartoon)


# In[ ]:




