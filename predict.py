#!/bin/python
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
CATEGORIES = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

# load and prepare the image
def load_image(filename):
	# loading the input image
	img = load_img(filename, target_size=(32, 32))
	# converting to array
	img = img_to_array(img)
	# reshaping into a single sample with 3 channels
	img = img.reshape(1, 32, 32, 3)
	# preparing pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img
 
img = load_image('location_of_image_with_name')#image name here 
# load model
#use your model name here 
model = load_model('CNN.model2')
# predict the class
result = model.predict(img)
a=np.argmax(result,axis=-1)
#print(a)
print(CATEGORIES[a[0]])
 
