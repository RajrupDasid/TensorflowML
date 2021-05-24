# Types of tensors
import tensorflow as tf
import numpy as np
import pandas as pd

t=tf.zeros([4,4,4,4])
a=tf.reshape(t, [256,-1])
print(a)