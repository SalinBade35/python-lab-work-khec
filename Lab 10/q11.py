# wap that creates a tensorflow constant with values[100, 200, 300].
# print its shape and data type.

import tensorflow as tf

t = tf.constant([100, 200, 300])
print(t.shape)
print(t.dtype)