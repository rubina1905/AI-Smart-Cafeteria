import gradio as gr
import os
import torch
from diffusers import StableDiffusionPipeline

# ==========================================================
# BASE FOLDER
# ==========================================================

base_folder = os.path.dirname(os.path.abspath(__file__))

# ==========================================================
# MENU FILE
# ==========================================================

menu_file = os.path.join(base_folder, "next_day_menu.txt")

if not os.path.exists(menu_file):
    raise FileNotFoundError(
        f"next_day_menu.txt not found at:\n{menu_file}"
    )

with open(menu_file, "r", encoding="utf-8") as file:
    menu = file.read()

# ==========================================================
# IMAGE OUTPUT FOLDER
# ==========================================================

image_folder = os.path.join(base_folder, "images")

# Create images folder if it doesn't exist
os.makedirs(image_folder, exist_ok=True)

# Main image path for Streamlit
output_file = os.path.join(
    image_folder,
    "cafeteria_menu.png"
)

# Also create a copy in the main Gen AI folder
generated_file = os.path.join(
    base_folder,
    "generated_menu.png"
)

# ==========================================================
# LOAD STABLE DIFFUSION MODEL
# ==========================================================

print("Loading Stable Diffusion model...")

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

# CPU
pipe = pipe.to("cpu")

print("Model loaded successfully.")

# ==========================================================
# GENERATE IMAGE
# ==========================================================

def generate_image():

    print("\nGenerating cafeteria menu image...")

    prompt = f"""
Create a realistic university cafeteria food photograph.

Show ONLY the foods mentioned in the menu below.

MENU:
{menu}

Organize the image into three clearly separated sections:

BREAKFAST
LUNCH
DINNER

Breakfast should contain only the breakfast foods.
Lunch should contain only the lunch foods.
Dinner should contain only the dinner foods.

Style:
Modern Indian university cafeteria,
realistic Indian food,
clean cafeteria presentation,
professional food photography,
well arranged food,
bright natural lighting,
realistic textures,
high quality.

Do not add random dishes.
Do not add extra food.
"""

    # Generate image
    result = pipe(
        prompt,
        width=384,
        height=384,
        num_inference_steps=10,
        guidance_scale=6
    )

    image = result.images[0]

    # ======================================================
    # SAVE IMAGE FOR STREAMLIT
    # ======================================================

    image.save(output_file)

    # Also save a copy in Gen AI folder
    image.save(generated_file)

    print("\n==========================================")
    print("IMAGE GENERATED SUCCESSFULLY")
    print("==========================================")

    print(f"Streamlit image:")
    print(output_file)

    print(f"\nGenerated image:")
    print(generated_file)

    print("==========================================")

    return image


# ==========================================================
# GRADIO INTERFACE
# ==========================================================

with gr.Blocks(title="AI Smart Cafeteria") as demo:

    gr.Markdown(
        "# 🍽️ AI Smart Cafeteria"
    )

    gr.Markdown(
        "## 🍛 Next-Day Special Menu"
    )

    # Display menu
    menu_display = gr.Textbox(
        value=menu,
        label="Tomorrow's Menu",
        lines=8
    )

    # Generate button
    generate_button = gr.Button(
        "🎨 Generate Menu Image",
        variant="primary"
    )

    # Image output
    output_image = gr.Image(
        label="AI Generated Menu Visualization",
        type="pil"
    )

    # Button action
    generate_button.click(
        fn=generate_image,
        inputs=None,
        outputs=output_image
    )


# ==========================================================
# LAUNCH GRADIO
# ==========================================================

demo.launch()