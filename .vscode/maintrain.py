import cv2
from keras.models import load_model
from PIL import Image
import numpy as np

model=load_model('BrainTumor10Epochs.h5')

image=cv2.imread('D:\Project\BT Final\BrainTumor Classification DL\predictions\pred(0).jpeg')
'''
while True: 
    return_value, frame = image.read() 
    if(return_value==False):
        print("******************************************************") 
        break
'''
img=Image.fromarray(image)

img=img.resize((64,64))

img=np.array(img)

input_img=np.expand_dims(img, axis=0)

result=model.predict(input_img)
print(result)



