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

menu_file = os.path.join(
    base_folder,
    "next_day_menu.txt"
)

if not os.path.exists(menu_file):
    raise FileNotFoundError(
        f"next_day_menu.txt not found at:\n{menu_file}"
    )

with open(
    menu_file,
    "r",
    encoding="utf-8"
) as file:
    menu = file.read().strip()

print("\n====================================")
print("AI SMART CAFETERIA")
print("====================================")

print("\nMENU:")
print(menu)

# ==========================================================
# EXTRACT INDIVIDUAL MENU ITEMS
# ==========================================================

def extract_menu_items(menu_text):

    breakfast = "Indian university cafeteria breakfast"
    lunch = "Indian university cafeteria lunch"
    dinner = "Indian university cafeteria dinner"

    lines = menu_text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        upper_line = line.upper()

        if upper_line.startswith("BREAKFAST:"):
            breakfast = line.split(
                ":", 1
            )[1].strip()

        elif upper_line.startswith("LUNCH:"):
            lunch = line.split(
                ":", 1
            )[1].strip()

        elif upper_line.startswith("DINNER:"):
            dinner = line.split(
                ":", 1
            )[1].strip()

    return breakfast, lunch, dinner


breakfast_dish, lunch_dish, dinner_dish = extract_menu_items(menu)

print("\n====================================")
print("EXTRACTED MENU")
print("====================================")

print("Breakfast:", breakfast_dish)
print("Lunch:", lunch_dish)
print("Dinner:", dinner_dish)

# ==========================================================
# IMAGE FOLDER
# ==========================================================

image_folder = os.path.join(
    base_folder,
    "images"
)

os.makedirs(
    image_folder,
    exist_ok=True
)

# ==========================================================
# IMAGE FILES
# ==========================================================

breakfast_file = os.path.join(
    image_folder,
    "breakfast.png"
)

lunch_file = os.path.join(
    image_folder,
    "lunch.png"
)

dinner_file = os.path.join(
    image_folder,
    "dinner.png"
)

# ==========================================================
# LOAD STABLE DIFFUSION
# ==========================================================

print("\n====================================")
print("LOADING STABLE DIFFUSION")
print("====================================")

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

print("Stable Diffusion loaded successfully.")

# ==========================================================
# GENERATION SETTINGS
# ==========================================================

WIDTH = 384
HEIGHT = 384

STEPS = 10

GUIDANCE = 7


# ==========================================================
# GENERATE BREAKFAST
# ==========================================================

def generate_breakfast():

    prompt = f"""
Realistic Indian university cafeteria food photograph.

Dish: {breakfast_dish}

Show ONLY this breakfast dish.

One appetizing serving on a clean cafeteria plate.

Professional food photography.
Realistic Indian food.
Natural lighting.
Realistic texture.
Clean presentation.

No lunch.
No dinner.
No other dishes.
"""

    print("\nGenerating breakfast...")
    print("Dish:", breakfast_dish)

    image = pipe(
        prompt,
        width=WIDTH,
        height=HEIGHT,
        num_inference_steps=STEPS,
        guidance_scale=GUIDANCE
    ).images[0]

    image.save(
        breakfast_file
    )

    print(
        "Breakfast saved:",
        breakfast_file
    )

    return image


# ==========================================================
# GENERATE LUNCH
# ==========================================================

def generate_lunch():

    prompt = f"""
Realistic Indian university cafeteria food photograph.

Dish: {lunch_dish}

Show ONLY this lunch dish.

One appetizing serving on a clean cafeteria plate.

Professional food photography.
Realistic Indian food.
Natural lighting.
Realistic texture.
Clean presentation.

No breakfast.
No dinner.
No other dishes.
"""

    print("\nGenerating lunch...")
    print("Dish:", lunch_dish)

    image = pipe(
        prompt,
        width=WIDTH,
        height=HEIGHT,
        num_inference_steps=STEPS,
        guidance_scale=GUIDANCE
    ).images[0]

    image.save(
        lunch_file
    )

    print(
        "Lunch saved:",
        lunch_file
    )

    return image


# ==========================================================
# GENERATE DINNER
# ==========================================================

def generate_dinner():

    prompt = f"""
Realistic Indian university cafeteria food photograph.

Dish: {dinner_dish}

Show ONLY this dinner dish.

One appetizing serving on a clean cafeteria plate.

Professional food photography.
Realistic Indian food.
Natural lighting.
Realistic texture.
Clean presentation.

No breakfast.
No lunch.
No other dishes.
"""

    print("\nGenerating dinner...")
    print("Dish:", dinner_dish)

    image = pipe(
        prompt,
        width=WIDTH,
        height=HEIGHT,
        num_inference_steps=STEPS,
        guidance_scale=GUIDANCE
    ).images[0]

    image.save(
        dinner_file
    )

    print(
        "Dinner saved:",
        dinner_file
    )

    return image


# ==========================================================
# GENERATE ALL THREE
# ==========================================================

def generate_all():

    print("\n====================================")
    print("GENERATING ALL MENU IMAGES")
    print("====================================")

    # Breakfast

    breakfast_image = generate_breakfast()

    # Lunch

    lunch_image = generate_lunch()

    # Dinner

    dinner_image = generate_dinner()

    print("\n====================================")
    print("ALL IMAGES GENERATED SUCCESSFULLY")
    print("====================================")

    print(
        "Breakfast:",
        breakfast_file
    )

    print(
        "Lunch:",
        lunch_file
    )

    print(
        "Dinner:",
        dinner_file
    )

    return (
        breakfast_image,
        lunch_image,
        dinner_image
    )


# ==========================================================
# GRADIO INTERFACE
# ==========================================================

with gr.Blocks(
    title="AI Smart Cafeteria"
) as demo:

    gr.Markdown(
        "# 🍽️ AI Smart Cafeteria"
    )

    gr.Markdown(
        "## 🍛 AI Menu Image Generation"
    )

    # ------------------------------------------------------
    # DISPLAY MENU
    # ------------------------------------------------------

    gr.Markdown(
        "### Tomorrow's Menu"
    )

    menu_display = gr.Textbox(
        value=menu,
        label="Generated Menu",
        lines=5,
        interactive=False
    )

    # ------------------------------------------------------
    # DISPLAY EXTRACTED DISHES
    # ------------------------------------------------------

    gr.Markdown(
        "### 🍽️ Menu Items Used for Image Generation"
    )

    with gr.Row():

        breakfast_text = gr.Textbox(
            value=breakfast_dish,
            label="🍳 Breakfast",
            interactive=False
        )

        lunch_text = gr.Textbox(
            value=lunch_dish,
            label="🍛 Lunch",
            interactive=False
        )

        dinner_text = gr.Textbox(
            value=dinner_dish,
            label="🍽️ Dinner",
            interactive=False
        )

    # ------------------------------------------------------
    # GENERATE BUTTON
    # ------------------------------------------------------

    generate_button = gr.Button(
        "🎨 Generate All Three Images",
        variant="primary"
    )

    # ------------------------------------------------------
    # OUTPUT IMAGES
    # ------------------------------------------------------

    with gr.Row():

        breakfast_output = gr.Image(
            label="🍳 AI Generated Breakfast",
            type="pil"
        )

        lunch_output = gr.Image(
            label="🍛 AI Generated Lunch",
            type="pil"
        )

        dinner_output = gr.Image(
            label="🍽️ AI Generated Dinner",
            type="pil"
        )

    # ------------------------------------------------------
    # BUTTON ACTION
    # ------------------------------------------------------

    generate_button.click(
        fn=generate_all,
        inputs=None,
        outputs=[
            breakfast_output,
            lunch_output,
            dinner_output
        ]
    )


# ==========================================================
# LAUNCH
# ==========================================================

demo.launch()