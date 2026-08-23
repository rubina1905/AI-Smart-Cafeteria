import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import (Input, Dense, Reshape, Flatten, Dropout,
                                     BatchNormalization, Conv2D,
                                     Conv2DTranspose, LeakyReLU)
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam

# -------------------------------
# Load and Preprocess Dataset
# -------------------------------
(X_train, _), (_, _) = mnist.load_data()

X_train = X_train.astype(np.float32)
X_train = (X_train - 127.5) / 127.5
X_train = np.expand_dims(X_train, axis=-1)

img_shape = (28, 28, 1)
latent_dim = 100

# -------------------------------
# Generator
# -------------------------------
def build_generator():

    model = Sequential()

    model.add(Dense(7 * 7 * 128, input_dim=latent_dim))
    model.add(Reshape((7, 7, 128)))

    model.add(BatchNormalization())
    model.add(LeakyReLU(negative_slope=0.2))

    model.add(Conv2DTranspose(128,
                              kernel_size=4,
                              strides=2,
                              padding='same'))

    model.add(BatchNormalization())
    model.add(LeakyReLU(negative_slope=0.2))

    model.add(Conv2DTranspose(64,
                              kernel_size=4,
                              strides=2,
                              padding='same'))

    model.add(BatchNormalization())
    model.add(LeakyReLU(negative_slope=0.2))

    model.add(Conv2D(1,
                     kernel_size=7,
                     activation='tanh',
                     padding='same'))

    noise = Input(shape=(latent_dim,))
    img = model(noise)

    return Model(noise, img)

# -------------------------------
# Discriminator
# -------------------------------
def build_discriminator():

    model = Sequential()

    model.add(Conv2D(64,
                     kernel_size=3,
                     strides=2,
                     padding='same',
                     input_shape=img_shape))

    model.add(LeakyReLU(negative_slope=0.2))
    model.add(Dropout(0.25))

    model.add(Conv2D(128,
                     kernel_size=3,
                     strides=2,
                     padding='same'))

    model.add(LeakyReLU(negative_slope=0.2))
    model.add(Dropout(0.25))

    model.add(Flatten())

    model.add(Dense(1, activation='sigmoid'))

    img = Input(shape=img_shape)
    validity = model(img)

    return Model(img, validity)

# -------------------------------
# Compile Models
# -------------------------------
optimizer = Adam(learning_rate=0.0002, beta_1=0.5)

discriminator = build_discriminator()

discriminator.compile(loss='binary_crossentropy',
                      optimizer=optimizer,
                      metrics=['accuracy'])

generator = build_generator()

z = Input(shape=(latent_dim,))
img = generator(z)

discriminator.trainable = False

validity = discriminator(img)

combined = Model(z, validity)

combined.compile(loss='binary_crossentropy',
                 optimizer=optimizer)

# -------------------------------
# Training Parameters
# -------------------------------
epochs = 40
batch_size = 64

valid = np.ones((batch_size, 1))
fake = np.zeros((batch_size, 1))

# -------------------------------
# Training Loop
# -------------------------------
for epoch in range(epochs):

    idx = np.random.randint(0,
                            X_train.shape[0],
                            batch_size)

    real_imgs = X_train[idx]

    noise = np.random.normal(0,
                             1,
                             (batch_size, latent_dim))

    fake_imgs = generator.predict(noise, verbose=0)

    d_loss_real = discriminator.train_on_batch(real_imgs,
                                               valid)

    d_loss_fake = discriminator.train_on_batch(fake_imgs,
                                               fake)

    d_loss = 0.5 * np.add(d_loss_real,
                          d_loss_fake)

    noise = np.random.normal(0,
                             1,
                             (batch_size, latent_dim))

    g_loss = combined.train_on_batch(noise,
                                     valid)

    print(f"Epoch {epoch+1}/{epochs} | "
          f"D Loss: {d_loss[0]:.4f} | "
          f"Accuracy: {100*d_loss[1]:.2f}% | "
          f"G Loss: {g_loss:.4f}")

# -------------------------------
# Save Generator Model
# -------------------------------
generator.save("dcgan_generator.keras")

print("Training Completed.")
print("Generator Model Saved Successfully!")

# -------------------------------
# Generate Sample Images
# -------------------------------
noise = np.random.normal(0,1,(25,latent_dim))

generated = generator.predict(noise, verbose=0)

generated = (generated + 1)/2

fig, axes = plt.subplots(5,5, figsize=(6,6))

count = 0

for i in range(5):
    for j in range(5):
        axes[i,j].imshow(generated[count,:,:,0], cmap='gray')
        axes[i,j].axis('off')
        count += 1

plt.show()