import streamlit as st
import os
import time


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Smart Cafeteria",
    page_icon="🍽️",
    layout="wide"
)


# ==========================================================
# BASE FOLDER
# ==========================================================

base_folder = os.path.dirname(
    os.path.abspath(__file__)
)


# ==========================================================
# TITLE
# ==========================================================

st.title("🍽️ AI Smart Cafeteria")

st.subheader(
    "AI-Based Food Waste Prediction & Menu Planning System"
)

st.divider()


# ==========================================================
# CAFETERIA DEMAND PREDICTION
# ==========================================================

st.header("📊 Cafeteria Demand Prediction")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Expected Students",
    "1800"
)

col2.metric(
    "Breakfast Demand",
    "1046"
)

col3.metric(
    "Lunch Demand",
    "1539"
)

col4.metric(
    "Dinner Demand",
    "873"
)

st.divider()


# ==========================================================
# FOOD WASTE ANALYSIS
# ==========================================================

st.header("♻️ Food Waste Analysis")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Without AI",
    "518 meals"
)

col2.metric(
    "With AI",
    "103 meals"
)

col3.metric(
    "Waste Reduction",
    "80.12%"
)

st.divider()


# ==========================================================
# NEXT-DAY SPECIAL MENU
# ==========================================================

st.header("🍛 Next-Day Special Menu")

menu_file = os.path.join(
    base_folder,
    "next_day_menu.txt"
)

if os.path.exists(menu_file):

    try:

        with open(
            menu_file,
            "r",
            encoding="utf-8"
        ) as file:

            menu = file.read()

        st.info(menu)

    except Exception as e:

        st.error(
            f"Unable to read menu file: {e}"
        )

else:

    st.warning(
        "next_day_menu.txt not found."
    )


st.divider()


# ==========================================================
# AI GENERATED MENU IMAGES
# ==========================================================

st.header("🖼️ AI Generated Menu")

st.write(
    "These images are generated locally using "
    "Stable Diffusion through the Gradio interface."
)


# ==========================================================
# IMAGE FOLDER
# ==========================================================

image_folder = os.path.join(
    base_folder,
    "images"
)


# ==========================================================
# IMAGE PATHS
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
# CHECK IMAGE FILES
# ==========================================================

breakfast_exists = os.path.exists(
    breakfast_file
)

lunch_exists = os.path.exists(
    lunch_file
)

dinner_exists = os.path.exists(
    dinner_file
)


# ==========================================================
# DISPLAY THREE IMAGES
# ==========================================================

col1, col2, col3 = st.columns(3)


# ==========================================================
# BREAKFAST
# ==========================================================

with col1:

    st.subheader("🍳 Breakfast")

    if breakfast_exists:

        st.image(
            breakfast_file,
            caption="AI Generated Breakfast",
            width=300
        )

        breakfast_time = time.ctime(
            os.path.getmtime(
                breakfast_file
            )
        )

        st.caption(
            f"Generated: {breakfast_time}"
        )

    else:

        st.warning(
            "Breakfast image not found."
        )


# ==========================================================
# LUNCH
# ==========================================================

with col2:

    st.subheader("🍛 Lunch")

    if lunch_exists:

        st.image(
            lunch_file,
            caption="AI Generated Lunch",
            width=300
        )

        lunch_time = time.ctime(
            os.path.getmtime(
                lunch_file
            )
        )

        st.caption(
            f"Generated: {lunch_time}"
        )

    else:

        st.warning(
            "Lunch image not found."
        )


# ==========================================================
# DINNER
# ==========================================================

with col3:

    st.subheader("🍽️ Dinner")

    if dinner_exists:

        st.image(
            dinner_file,
            caption="AI Generated Dinner",
            width=300
        )

        dinner_time = time.ctime(
            os.path.getmtime(
                dinner_file
            )
        )

        st.caption(
            f"Generated: {dinner_time}"
        )

    else:

        st.warning(
            "Dinner image not found."
        )


st.divider()


# ==========================================================
# IMAGE GENERATION STATUS
# ==========================================================

st.header("🔄 Image Generation Status")

status_col1, status_col2, status_col3 = st.columns(3)


# ----------------------------------------------------------
# BREAKFAST STATUS
# ----------------------------------------------------------

with status_col1:

    if breakfast_exists:

        st.success(
            "✅ Breakfast image available"
        )

    else:

        st.error(
            "❌ Breakfast image missing"
        )


# ----------------------------------------------------------
# LUNCH STATUS
# ----------------------------------------------------------

with status_col2:

    if lunch_exists:

        st.success(
            "✅ Lunch image available"
        )

    else:

        st.error(
            "❌ Lunch image missing"
        )


# ----------------------------------------------------------
# DINNER STATUS
# ----------------------------------------------------------

with status_col3:

    if dinner_exists:

        st.success(
            "✅ Dinner image available"
        )

    else:

        st.error(
            "❌ Dinner image missing"
        )


# ==========================================================
# IMAGE FILE LOCATIONS
# ==========================================================

with st.expander(
    "🔍 Show Image File Locations"
):

    st.write("Breakfast image:")

    st.code(
        breakfast_file
    )

    st.write("Lunch image:")

    st.code(
        lunch_file
    )

    st.write("Dinner image:")

    st.code(
        dinner_file
    )


# ==========================================================
# REFRESH BUTTON
# ==========================================================

st.divider()

if st.button(
    "🔄 Refresh Generated Images"
):

    st.rerun()


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "🍽️ AI Smart Cafeteria | "
    "Machine Learning + Local LLM + Local Image Generation"
)
