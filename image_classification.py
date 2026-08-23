import gradio as gr
import torch
from torchvision import models, transforms
from PIL import Image

# Load pre-trained ResNet18 model
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()

# Load ImageNet class labels
weights = models.ResNet18_Weights.DEFAULT
labels = weights.meta["categories"]

# Image preprocessing
preprocess = weights.transforms()

# Prediction function
def classify_image(image):
    image = preprocess(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)

    # Get top 5 predictions
    top5_prob, top5_catid = torch.topk(probabilities, 5)

    results = {
        labels[top5_catid[i]]: float(top5_prob[i])
        for i in range(5)
    }

    return results

# Create Gradio interface
demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=5),
    title="Image Classification App",
    description="Upload an image and get the top 5 predicted classes."
)

# Launch app
demo.launch()