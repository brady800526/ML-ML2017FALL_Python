#!/usr/bin/env python
# coding: utf-8

# In[15]:


from PIL import Image
from math import floor
import sys
img = Image.open(sys.argv[1]) # Or directly input the filename
data = img.getdata()

# Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
output_img_data = [(floor(d[0]/2), floor(d[1]/2), floor(d[2]/2)) for d in data]

img.putdata(output_img_data)
img.save('Q2.jpg')


# In[ ]:




