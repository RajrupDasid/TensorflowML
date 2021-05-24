#rank/degree of a tensor
import tensorflow as tf
#string=tf.variable("example string",tf.string)
rank1_tensor=tf.variable([["one","dimensional","list"],["test","yes"]],tf.string)
tf.rank(rank1_tensor)
