import gradio as gr
import numpy as np
from PIL import Image
import tensorflow as tf
Dense = tf.keras.layers.Dense
Input = tf.keras.layers.Input
Model = tf.keras.Model
Flatten = tf.keras.layers.Flatten
Reshape = tf.keras.layers.Reshape

# -----------------------------
# Build Autoencoder
# -----------------------------
input_shape = (28, 28, 1)

input_img = Input(shape=input_shape)

x = Flatten()(input_img)
encoded = Dense(64, activation='relu')(x)
decoded = Dense(784, activation='sigmoid')(encoded)

output_img = Reshape((28, 28, 1))(decoded)

autoencoder = Model(input_img, output_img)

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# -----------------------------
# Train on MNIST Dataset
# -----------------------------
(x_train, _), (_, _) = tf.keras.datasets.mnist.load_data()

x_train = x_train.astype('float32') / 255.0
x_train = np.reshape(x_train, (-1, 28, 28, 1))

# Add Noise
noise_factor = 0.5
x_train_noisy = x_train + noise_factor * np.random.normal(
    loc=0.0,
    scale=1.0,
    size=x_train.shape
)

x_train_noisy = np.clip(x_train_noisy, 0., 1.)

autoencoder.fit(
    x_train_noisy,
    x_train,
    epochs=3,
    batch_size=256,
    shuffle=True
)

# -----------------------------
# Prediction Function
# -----------------------------
def denoise_image(image):

    image = image.convert("L")
    image = image.resize((28, 28))

    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    reconstructed = autoencoder.predict(img_array)

    reconstructed = reconstructed.reshape(28, 28) * 255
    reconstructed = reconstructed.astype(np.uint8)

    return Image.fromarray(reconstructed)

# -----------------------------
# Gradio Interface
# -----------------------------
interface = gr.Interface(
    fn=denoise_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil"),
    title="Autoencoder Image Denoising",
    description="Upload a noisy handwritten digit image. The autoencoder reconstructs a cleaner version."
)

interface.launch()