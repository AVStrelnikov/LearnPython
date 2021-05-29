import os
import random
import numpy as np
import skimage
from skimage import io

os.getcwd()
os.listdir()

list = os.listdir()

im = []
for i in list:
    if i.find("jpg") !=-1:
        im.append (skimage.io.imread (i));


r = random.randint(1,6);
print (r);
skimage.io.imshow(im[r-1]);
io.show()