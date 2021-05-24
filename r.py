#rank/degree of a tensor
import tensorflow as tf
string=tf.Variable("example string",tf.string)
rank1_tensor=tf.Variable([["one","dimensional"],["test","yes"]],tf.string)
tf.rank(rank1_tensor)
rank1_tensor.shape