import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# -------------------------------
# Load Saved Generator
# -------------------------------
generator = load_model("dcgan_generator.keras")

latent_dim = 100

# -------------------------------
# Generate Images
# -------------------------------
noise = np.random.normal(0,
                         1,
                         (25, latent_dim))

generated_images = generator.predict(noise, verbose=0)

generated_images = (generated_images + 1) / 2

# -------------------------------
# Display Images
# -------------------------------
fig, axes = plt.subplots(5,5, figsize=(7,7))

count = 0

for i in range(5):
    for j in range(5):
        axes[i,j].imshow(generated_images[count,:,:,0],
                         cmap='gray')

        axes[i,j].axis("off")

        count += 1

plt.show()

# -------------------------------
# Save Images
# -------------------------------
for i in range(25):

    plt.imsave(f"generated_image_{i+1}.png",
               generated_images[i,:,:,0],
               cmap="gray")

print("25 Images Saved Successfully.")

# Save the trained generator model
generator.save("dcgan_generator.keras")

print("Generator model saved as dcgan_generator.keras")