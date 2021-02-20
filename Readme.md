# Image recognition using keras and Tensorflow
The project aims to build a simple image recognising model based on cifar-10 dataset, availabe [here].

## About the dataset
The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.
The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.
The above dataset was chosen as it requires no preprocessing.
There are 10 classes of images as listed below


**1) airplane**

**2) automobile**	

**3) bird**

**4) cat**

**5) deer**

**6) dog**

**7) frog**

**8) horse**

**9) ship**

**10) truck**

## Project Files
The project files consists of the following files/folders,

[Readme.md](Readme.md)- Project description

[source.py](source.py)- Source code

[predict.py](predict.py)- Code for using the model to predict an image class.

[Model](Model)- Folder containing trained model, (Note : this can be generated on training on any compatible machine, its provided here for reference)

[Sample images](Sample-images) - Folder containing random images ( they come under the 10 listed classes) used for testing model's prediction






















[here]https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

