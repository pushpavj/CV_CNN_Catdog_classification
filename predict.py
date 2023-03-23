#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

@author: Pushpa V J
"""

import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class dogcat:
    def __init__(self,filename):
        self.filename =filename #get the uploaded image file as input parameter


    def predictiondogcat(self):
        # load model
        model = load_model('model.h5') #load the dogcate classifier ML model as prediction model

        # summarize model
        #model.summary()
        imagename = self.filename #gets the input as uploaded image file from calling module
      #  loader=image.__loader__
       # test_image=loader.load_images(imagename,target_size=(64,64))
        
        test_image = image.load_img(imagename, target_size = (64, 64)) #load the image from
                                                              #image file with setting size as
                                                               #64 X 64
        test_image = image.img_to_array(test_image) #convert the image into array data of 
                                                    #dimention 64 X 64 X 3 (3 for color rgb)
        test_image = np.expand_dims(test_image, axis = 0) #expand the array dimension to 4
                                               #dimension data i.e 1 X 64 X 64 X 3 as we have
                                               # used 4 dimensioned image data while training
                                               # the model
        result = model.predict(test_image) #predict the 4 dimensioned image data array

        if result[0][0] == 1:
            prediction = 'dog' #set the prediction result to dog if the predicted value is 1
            return [{ "image" : prediction}] 
        else:
            prediction = 'cat'#set the prediction result to cat if the predicted value is 0
            return [{ "image" : prediction}]


