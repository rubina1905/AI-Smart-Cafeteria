# 🍽️ AI Smart Cafeteria

## AI-Based Food Waste Prediction & Menu Planning System

An AI-powered university cafeteria management system that combines **Machine Learning, Local LLMs, and Local Image Generation** to predict cafeteria food demand, reduce food wastage, generate next-day menu recommendations, and create visual representations of the menu.

---

## 📌 Problem Statement

University cafeterias prepare large quantities of food every day. However, accurately estimating the number of students who will consume each meal is difficult.

Overestimating demand results in:

* Excess food preparation
* Increased food wastage
* Higher operational costs
* Unnecessary resource consumption

Underestimating demand can result in:

* Food shortages
* Student dissatisfaction
* Poor cafeteria planning

The objective of this project is to develop an AI-based cafeteria system that predicts meal demand and food wastage and uses Generative AI to assist with menu planning and visualization.

---

## 🎯 Objectives

The main objectives of the project are:

1. Predict the expected number of students for each meal.
2. Estimate potential food wastage.
3. Reduce food wastage using AI-based demand prediction.
4. Generate a next-day cafeteria menu.
5. Use a Local LLM for text generation.
6. Use a Local Image Generation Model for menu visualization.
7. Provide an interactive dashboard using Streamlit.
8. Provide a Gradio interface for AI image generation.
9. Ensure the complete application can run locally.

---

## 🚀 Features

### 📊 1. Cafeteria Demand Prediction

The system predicts cafeteria demand for:

* Breakfast
* Lunch
* Dinner

The prediction system uses machine learning to estimate the expected number of meals required based on historical cafeteria data and relevant factors.

---

### ♻️ 2. Food Waste Analysis

The system estimates potential food wastage based on predicted meal demand.

The dashboard compares:

**Food Waste Without AI vs Food Waste With AI**

and calculates the percentage reduction in food waste.

---

### 🤖 3. Machine Learning Models

Two regression models are trained and compared:

* **Random Forest Regressor**
* **XGBoost Regressor**

Both models are evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

After evaluation, the better-performing model is selected for the final demand prediction system.

In the current implementation, **XGBoost is selected as the best model** and saved as:

```text
models/cafeteria_xgboost_model.pkl
```

---

### 🍛 4. AI-Based Menu Planning

The system generates a practical next-day university cafeteria menu using the predicted demand.

The menu generation considers:

* Expected students
* Breakfast demand
* Lunch demand
* Dinner demand
* Food waste
* Waste reduction
* Affordability
* Nutrition
* Bulk preparation feasibility

The generated menu is stored locally in:

```text
next_day_menu.txt
```

---

### 🧠 5. Local LLM – Ollama + Llama 3

The project uses a **Local Large Language Model** through Ollama.

The model used is:

**Llama 3**

The LLM generates the next-day cafeteria menu using the machine learning predictions as input.

The workflow is:

```text
ML Predictions
      ↓
Expected Students
      ↓
Meal Demand
      ↓
Food Waste Analysis
      ↓
Llama 3
      ↓
Next-Day Menu
```

No cloud-based LLM APIs such as OpenAI, Gemini, or Claude are used.

---

### 🎨 6. Local Image Generation – Stable Diffusion

The project uses **Stable Diffusion** as the local image generation model.

The generated menu text is used to create a visual representation of the cafeteria menu.

The workflow is:

```text
Next-Day Menu
      ↓
Image Generation Prompt
      ↓
Stable Diffusion
      ↓
AI Generated Menu Image
```

The generated image is saved locally as:

```text
images/cafeteria_menu.png
```

---

### 🖥️ 7. Streamlit Dashboard

The Streamlit application provides the main cafeteria dashboard.

The dashboard displays:

* Expected students
* Breakfast demand
* Lunch demand
* Dinner demand
* Food waste without AI
* Food waste with AI
* Waste reduction percentage
* Next-day menu
* AI-generated menu image

---

### 🎨 8. Gradio Image Generation Interface

Gradio provides an interactive interface for generating the cafeteria menu visualization using Stable Diffusion.

The user can:

1. View the next-day menu.
2. Generate an AI menu visualization.
3. View the generated image.
4. Save the image locally.
5. Display the generated image in Streamlit.

---

## 🏗️ System Architecture

The overall architecture of the AI Smart Cafeteria system is:

```text
                      🍽️ AI SMART CAFETERIA
                               │
                               ▼
                  ┌──────────────────────────┐
                  │     CAFETERIA DATA       │
                  │                          │
                  │ • Students Present       │
                  │ • Meal Type              │
                  │ • Previous Day Sales     │
                  │ • Previous Week Average  │
                  │ • Weather                │
                  │ • Exams / Holidays       │
                  │ • Scheduled Classes      │
                  │ • Meals Prepared         │
                  │ • Food Waste             │
                  └────────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │   DATA PREPROCESSING     │
                  │                          │
                  │ • Date Processing        │
                  │ • Feature Engineering    │
                  │ • Label Encoding         │
                  │ • Train/Test Split       │
                  └────────────┬─────────────┘
                               │
                               ▼
              ┌────────────────┴────────────────┐
              │                                 │
              ▼                                 ▼
    ┌─────────────────────┐          ┌─────────────────────┐
    │   RANDOM FOREST     │          │       XGBOOST       │
    │                     │          │                     │
    │ RandomForest        │          │ XGBRegressor        │
    │ Regressor           │          │                     │
    │                     │          │                     │
    │ MAE / RMSE / R²     │          │ MAE / RMSE / R²     │
    └──────────┬──────────┘          └──────────┬──────────┘
               │                                │
               └───────────────┬────────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │    MODEL COMPARISON      │
                  │                          │
                  │ Random Forest vs XGBoost │
                  └────────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │    BEST MODEL SELECTED   │
                  │                          │
                  │        XGBoost           │
                  │                          │
                  │ cafeteria_xgboost_       │
                  │ model.pkl                │
                  └────────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │    DEMAND PREDICTION     │
                  │                          │
                  │ Breakfast → 1046         │
                  │ Lunch     → 1539         │
                  │ Dinner    → 873          │
                  └────────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │    FOOD WASTE ANALYSIS   │
                  │                          │
                  │ • Without AI Waste       │
                  │ • With AI Waste          │
                  │ • Waste Reduction %      │
                  └────────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │       LOCAL LLM          │
                  │                          │
                  │     Ollama + Llama 3     │
                  │                          │
                  │ Inputs:                  │
                  │ • Expected Students      │
                  │ • Meal Demand            │
                  │ • Food Waste             │
                  │ • Waste Reduction        │
                  └────────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │    NEXT-DAY MENU         │
                  │                          │
                  │ Breakfast: ...           │
                  │ Lunch: ...               │
                  │ Dinner: ...              │
                  └────────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │    STABLE DIFFUSION      │
                  │                          │
                  │ Local Image Generation   │
                  │                          │
                  │ Menu Text → Image        │
                  └────────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │         GRADIO           │
                  │                          │
                  │ Generate Menu Image      │
                  │ cafeteria_menu.png       │
                  └────────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │       STREAMLIT          │
                  │       DASHBOARD          │
                  │                          │
                  │ 📊 Demand Prediction     │
                  │ ♻️ Waste Analysis        │
                  │ 🍛 Next-Day Menu         │
                  │ 🖼️ Generated Image       │
                  └──────────────────────────┘
```

---

## 🔄 Complete Workflow

The complete system workflow is:

```text
Historical Cafeteria Data
          ↓
Data Preprocessing
          ↓
Feature Engineering
          ↓
Random Forest ──────────┐
          ↓             │
       Evaluation       │
                        ├──→ Model Comparison
          XGBoost ──────┘
          ↓
Best Model: XGBoost
          ↓
Meal Demand Prediction
          ↓
Food Waste Analysis
          ↓
Ollama + Llama 3
          ↓
Next-Day Menu Generation
          ↓
Stable Diffusion
          ↓
Menu Image Generation
          ↓
Gradio
          ↓
cafeteria_menu.png
          ↓
Streamlit Dashboard
```

---

## 🧰 Technologies Used

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest
* XGBoost
* Joblib

### Generative AI

* Ollama
* Llama 3
* Stable Diffusion
* Diffusers
* PyTorch

### Application Frameworks

* Streamlit
* Gradio

### Development Tools

* Git
* GitHub

---

## 📂 Repository Structure

```text
AI-Smart-Cafeteria/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── app.py
├── gradio_app.py
├── AI_food_prediction.py
├── AI_food_wastage_prediction_data.py
│
├── data/
│   └── cafeteria_food_waste_dataset_12000.csv
│
├── models/
│   ├── cafeteria_demand_xgboost.pkl
│   └── cafeteria_xgboost_model.pkl
│
├── images/
│   └── cafeteria_menu.png
│
├── outputs/
│
├── docs/
│   ├── architecture.png
│   ├── workflow.png
│   └── screenshots/
│
└── demo/
    └── demo.mp4
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rubina1905/AI-Smart-Cafeteria.git
```

Move into the project directory:

```bash
cd AI-Smart-Cafeteria
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Ollama

Install Ollama on the local machine and download the Llama 3 model.

Run:

```bash
ollama pull llama3
```

Verify that the model is available:

```bash
ollama list
```

The application uses Ollama locally and does not require a cloud LLM API.

---

## ▶️ Usage

### Step 1 – Run the ML Pipeline

Run the machine learning script:

```bash
python AI_food_prediction.py
```

This performs:

* Dataset loading
* Data preprocessing
* Feature engineering
* Random Forest training
* XGBoost training
* Model evaluation
* Model comparison
* Demand prediction
* Food waste calculation
* Llama 3 menu generation

The generated menu is saved as:

```text
next_day_menu.txt
```

---

### Step 2 – Generate the Menu Image

Run the Gradio application:

```bash
python gradio_app.py
```

Gradio will provide a local interface where the menu visualization can be generated using Stable Diffusion.

The generated image is saved as:

```text
images/cafeteria_menu.png
```

---

### Step 3 – Run the Streamlit Dashboard

Run:

```bash
streamlit run app.py
```

The Streamlit dashboard will open in the browser.

It displays the complete cafeteria AI workflow including:

* Demand predictions
* Food waste analysis
* Next-day menu
* AI-generated menu image

---

## 📈 Model Evaluation

The system compares Random Forest and XGBoost using three regression metrics.

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted meal demand.

Lower MAE indicates better performance.

### Root Mean Squared Error (RMSE)

Measures the square root of the average squared prediction error.

Lower RMSE indicates better performance.

### R² Score

Measures how well the model explains the variation in meal demand.

Higher R² indicates better performance.

The model with the better overall performance is selected for the final prediction workflow.

---

## ♻️ Food Waste Reduction

The system demonstrates the potential impact of AI-based demand prediction by comparing traditional food preparation with AI-optimized preparation.

The current implementation assumes:

```text
Traditional Preparation:
15% extra food

AI-Optimized Preparation:
3% extra food
```

The system calculates:

```text
Waste Reduction =
(Without AI Waste - With AI Waste)
---------------------------------- × 100
       Without AI Waste
```

This allows the cafeteria to estimate the potential reduction in food waste.

---

## 🤖 Generative AI Workflow

The project combines two local generative AI components.

### Local Text Generation

```text
XGBoost Demand Prediction
          ↓
Food Waste Analysis
          ↓
Ollama
          ↓
Llama 3
          ↓
Next-Day Menu
```

### Local Image Generation

```text
Next-Day Menu
      ↓
Image Prompt
      ↓
Stable Diffusion
      ↓
Generated Menu Visualization
```

Therefore, the application integrates **text generation and image generation in a single workflow**.

---

## 🔐 Local AI and Privacy

The project is designed to run locally.

The following AI components run on the local machine:

* Llama 3 through Ollama
* Stable Diffusion
* XGBoost
* Random Forest

No OpenAI, Gemini, Claude, or other cloud-based AI APIs are required for the core application workflow.

---

## 📸 Screenshots

Screenshots demonstrating the application are stored in:

```text
docs/screenshots/
```

Recommended screenshots include:

1. Streamlit dashboard
2. Cafeteria demand prediction
3. Food waste analysis
4. Generated next-day menu
5. Gradio interface
6. Stable Diffusion generated image

---

## 🎥 Demo Video

The project demonstration video is available at:

```text
demo/demo.mp4
```

The demo demonstrates:

1. Running the prediction system
2. Generating cafeteria demand predictions
3. Calculating food waste
4. Generating the next-day menu using Llama 3
5. Generating the menu image using Stable Diffusion
6. Displaying the results in Streamlit

---

## 🔮 Future Enhancements

Future versions of the system could include:

* Real-time cafeteria attendance data
* Student meal booking information
* Weather API integration
* Campus event information
* Dynamic food pricing
* Cost optimization
* Nutritional optimization
* Multiple cafeteria support
* Real-time waste monitoring
* Computer vision-based leftover food measurement
* Automated inventory management
* Better image generation models such as SDXL or FLUX

---

## 👩‍💻 Author

**Rubina Mohammed**

M.Sc. Data Analytics

AI Smart Cafeteria – Generative AI Project

GitHub:

https://github.com/rubina1905/AI-Smart-Cafeteria

---

## 📄 License

This project is intended for academic and educational purposes.
