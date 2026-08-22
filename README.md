# 🍽️ AI Smart Cafeteria

## AI-Based Food Waste Prediction & Menu Planning System

An AI-powered university cafeteria management system that combines **Machine Learning, Local LLMs, and Local Image Generation** to predict cafeteria food demand, reduce food wastage, generate next-day menu recommendations, and create visual representations of the menu.

---

## 📌 Problem Statement

University cafeterias prepare large quantities of food every day. However, accurately estimating the number of students who will consume each meal is difficult.

Overestimating demand results in:

- Excess food preparation
- Increased food wastage
- Higher operational costs
- Unnecessary resource consumption

Underestimating demand can result in:

- Food shortages
- Student dissatisfaction
- Poor cafeteria planning

The objective of this project is to develop an AI-based cafeteria system that predicts meal demand and food wastage and uses Generative AI to assist with menu planning and visualization.

---

# 🎯 Objectives

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

# 🚀 Features

## 📊 1. Cafeteria Demand Prediction

The system predicts the expected cafeteria demand for:

- Breakfast
- Lunch
- Dinner

The prediction model uses machine learning techniques to estimate meal requirements.

---

## ♻️ 2. Food Waste Prediction

The system estimates the amount of food that could be wasted based on predicted demand.

The dashboard compares:

**Food waste without AI vs Food waste with AI**

and calculates the percentage reduction.

---

## 🍛 3. AI-Based Menu Planning

The system generates a next-day cafeteria menu based on predicted demand and cafeteria requirements.

The generated menu is stored in:

```text
next_day_menu.txt

**## 🤖 4. Local LLM**

The project uses a Local Large Language Model through Ollama.

The LLM is used for text-based menu generation and AI-assisted cafeteria planning.

No OpenAI, Gemini, Claude, or other cloud-based LLM APIs are used.

**## 🎨 5. Local Image Generation**

The project uses Stable Diffusion as the local image generation model.

The image generation pipeline creates a visual representation of the next-day cafeteria menu.

Generated images are stored locally in:

images/cafeteria_menu.png

**## 🖥️ 6. Streamlit Dashboard**

The Streamlit application provides a unified dashboard showing:

Expected student demand
Breakfast demand
Lunch demand
Dinner demand
Food waste comparison
Waste reduction
Next-day menu
AI-generated menu image

🎨 7. Gradio Image Generation Interface

Gradio provides an interactive interface for generating the cafeteria menu visualization using Stable Diffusion.

The generated image is automatically saved so that it can be displayed in the Streamlit dashboard.

🏗️ System Architecture

The overall workflow is:

                      🍽️ AI SMART CAFETERIA
                                  │
                                  ▼
                 ┌─────────────────────────────┐
                 │       CAFETERIA DATA        │
                 │                             │
                 │ • Students Present         │
                 │ • Meal Type                 │
                 │ • Previous Day Meals Sold   │
                 │ • Previous Week Average     │
                 │ • Weather                   │
                 │ • Exams / Holidays          │
                 │ • Scheduled Classes         │
                 │ • Meals Prepared / Waste    │
                 └──────────────┬──────────────┘
                                │
                                ▼
                 ┌─────────────────────────────┐
                 │     DATA PREPROCESSING      │
                 │                             │
                 │ • Date Processing           │
                 │ • Feature Engineering       │
                 │ • Label Encoding            │
                 │ • Train/Test Split          │
                 └──────────────┬──────────────┘
                                │
                                ▼
              ┌─────────────────┴─────────────────┐
              │                                   │
              ▼                                   ▼
   ┌──────────────────────┐             ┌──────────────────────┐
   │   RANDOM FOREST      │             │       XGBOOST        │
   │                      │             │                      │
   │ RandomForestRegressor│             │     XGBRegressor    │
   │                      │             │                      │
   │ Model Evaluation     │             │ Model Evaluation     │
   │ MAE / RMSE / R²      │             │ MAE / RMSE / R²      │
   └──────────┬───────────┘             └──────────┬───────────┘
              │                                    │
              │        MODEL COMPARISON            │
              └────────────────┬───────────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │   BEST MODEL SELECTED   │
                  │                         │
                  │       XGBoost           │
                  │                         │
                  │ cafeteria_xgboost_     │
                  │ model.pkl               │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │   DEMAND PREDICTION     │
                  │                         │
                  │ Breakfast → 1046        │
                  │ Lunch     → 1539        │
                  │ Dinner    → 873         │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │   FOOD WASTE ANALYSIS   │
                  │                         │
                  │ Without AI Waste        │
                  │ With AI Waste            │
                  │ Waste Reduction %       │
                  └────────────┬────────────┘
                               │
                               ▼
              ┌──────────────────────────────────┐
              │          LOCAL LLM               │
              │                                  │
              │        Ollama + Llama 3          │
              │                                  │
              │ Inputs:                          │
              │ • Predicted demand               │
              │ • Expected students              │
              │ • Food waste                     │
              │ • Waste reduction                │
              └───────────────┬──────────────────┘
                              │
                              ▼
                  ┌─────────────────────────┐
                  │  NEXT-DAY MENU          │
                  │  GENERATION             │
                  │                         │
                  │ Breakfast: ...          │
                  │ Lunch: ...              │
                  │ Dinner: ...             │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │  STABLE DIFFUSION       │
                  │                         │
                  │ Local Image Generation  │
                  │                         │
                  │ Menu Text → Image       │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │        GRADIO           │
                  │                         │
                  │ Generate Menu Image     │
                  │ cafeteria_menu.png      │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │       STREAMLIT         │
                  │       DASHBOARD         │
                  │                         │
                  │ 📊 Demand Prediction    │
                  │ ♻️ Waste Analysis       │
                  │ 🍛 Next-Day Menu        │
                  │ 🖼️ Generated Image      │
                  └─────────────────────────┘
