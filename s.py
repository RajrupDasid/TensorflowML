#change shape
import tensorflow as tf
import numpy as np 
import pandas as pd

tensor1= tf.ones([1,2,3]) #tf.ones() creates a shape [1.2.3] tensor full of ones @ creates an image as that have one object 2 image and 3 elements
tensor2=tf.reshape(tensor1,[2,3,1]) #reshaping the order
tensor3= tf.reshape(tensor2,[3,-1]) #-1 tells the tensor to calculate the size of the dimension in that place #this will reshape the tensor to [3,2]
print(tensor3)