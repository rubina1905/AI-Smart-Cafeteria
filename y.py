import tensorflow as tf
print(tf.__version__)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, input_shape=(5,))
])

print("TensorFlow is working!")