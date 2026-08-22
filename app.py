import streamlit as st
import os

st.set_page_config(
    page_title="AI Smart Cafeteria",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ AI Smart Cafeteria")
st.subheader("AI-Based Food Waste Prediction & Menu Planning")

st.divider()

# ==========================================================
# CAFETERIA DEMAND PREDICTION
# ==========================================================

st.header("📊 Cafeteria Demand Prediction")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Expected Students", "1800")
col2.metric("Breakfast Demand", "1046")
col3.metric("Lunch Demand", "1539")
col4.metric("Dinner Demand", "873")

st.divider()

# ==========================================================
# FOOD WASTE ANALYSIS
# ==========================================================

st.header("♻️ Food Waste Analysis")

col1, col2, col3 = st.columns(3)

col1.metric("Without AI", "518 meals")
col2.metric("With AI", "103 meals")
col3.metric("Waste Reduction", "80.12%")

st.divider()

# ==========================================================
# NEXT-DAY SPECIAL MENU
# ==========================================================

st.header("🍛 Next-Day Special Menu")

try:
    with open("next_day_menu.txt", "r", encoding="utf-8") as file:
        menu = file.read()

    st.text(menu)

except FileNotFoundError:
    st.error("next_day_menu.txt not found.")

st.divider()

# ==========================================================
# AI GENERATED MENU IMAGE
# ==========================================================

st.header("🖼️ AI Generated Menu")

image_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "images",
    "cafeteria_menu.png"
)

if os.path.exists(image_file):

    st.image(
        image_file,
        caption="AI-generated visualization of tomorrow's special menu",
        use_container_width=True
    )

else:

    st.warning("AI generated image not found.")
    st.write("Streamlit is looking here:")
    st.code(image_file)