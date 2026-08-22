# ==========================================================
# AI BASED CAFETERIA FOOD WASTE PREDICTION SYSTEM
# ==========================================================


# ==========================
# IMPORT LIBRARIES
# ==========================

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import joblib


# ==========================================================
# STEP 1 : LOAD DATASET
# ==========================================================


df = pd.read_csv(
    r"C:\Rubina\Msc\Trimester 4\Gen AI\CIA_project\cafeteria_food_waste_dataset.csv"
)
df.rename(
    columns={
        "Temperature_C":"Temperature"
    },
    inplace=True
)
print("\n==============================")
print("DATASET INFORMATION")
print("==============================")
print("Shape :", df.shape)
print("\nColumns:")
print(df.columns)
print("\nFirst 5 rows")
print(df.head())
print("\nMissing Values")
print(df.isnull().sum())


# ==========================================================
# STEP 2 : DATA PREPROCESSING
# ==========================================================

# Convert Date

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(
    "Date"
).reset_index(
    drop=True
)

# Extract date features

df["Day_Number"] = df["Date"].dt.day
df["Month_Number"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

#7_day_average_demand

df["7_Day_Average"] = (
    df["Previous_Week_Average"]
)
df["7_Day_Average"] = df["7_Day_Average"].fillna(
    df["Previous_Day_Meals_Sold"]
)

# Remove date

df.drop(
    "Date",
    axis=1,
    inplace=True
)

# ==========================
# Convert Yes/No values
# ==========================

for col in df.columns:
    if df[col].dtype == "object":
        unique_values = df[col].dropna().unique()
        if set(unique_values).issubset({"Yes","No"}):
            df[col] = df[col].map(
                {
                    "Yes":1,
                    "No":0
                }
            )

# ==========================
# Encode categories
# ==========================

categorical_columns = df.select_dtypes(
    include="object"
).columns
encoders={}
for col in categorical_columns:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(
        df[col]
    )
    encoders[col]=encoder
print("\nAfter Encoding")
print(df.head())


# ==========================================================
# CHECK REMAINING TEXT DATA
# ==========================================================

print("\nRemaining Text Columns")
print(
    df.select_dtypes(
        include="object"
    ).columns
)

# ==========================================================
# STEP 3 : CREATE FEATURES AND TARGET
# ==========================================================

X = df.drop(
    [
        "Meals_Sold",
        "Food_Waste_kg",
        "Meals_Prepared",
    ],
    axis=1
)
y = df["Meals_Sold"]
print("\nFeatures")
print(
    X.columns
)
print("\nFeature Shape")
print(
    X.shape
)
print("\nTarget Shape")
print(
    y.shape
)

# ==========================================================
# STEP 4 : TRAIN TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("\nTraining Data")
print(
    X_train.shape
)
print("\nTesting Data")
print(
    X_test.shape
)

# ==========================================================
# STEP 5 : RANDOM FOREST MODEL
# ==========================================================

rf_model = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    random_state=42
)
print("\nTraining Random Forest...")
rf_model.fit(
    X_train,
    y_train
)
rf_prediction = rf_model.predict(
    X_test
)

# ==========================================================
# STEP 6 : XGBOOST MODEL
# ==========================================================

xgb_model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
)
print("\nTraining XGBoost...")
xgb_model.fit(
    X_train,
    y_train
)
xgb_prediction = xgb_model.predict(
    X_test
)


# ==========================================================
# STEP 7 : MODEL EVALUATION
# ==========================================================

def evaluate_model(
        name,
        actual,
        prediction
):
    mae = mean_absolute_error(
        actual,
        prediction
    )
    rmse = np.sqrt(
        mean_squared_error(
            actual,
            prediction
        )
    )
    r2 = r2_score(
        actual,
        prediction
    )
    print("\n====================")
    print(name)
    print("====================")
    print(
        "MAE:",
        round(mae,2)
    )
    print(
        "RMSE:",
        round(rmse,2)
    )
    print(
        "R2 Score:",
        round(r2,4)
    )
evaluate_model(
    "Random Forest",
    y_test,
    rf_prediction
)
evaluate_model(
    "XGBoost",
    y_test,
    xgb_prediction
)

# ==========================================================
# STEP 8 : SAVE BEST MODEL
# ==========================================================

best_model = xgb_model
joblib.dump(
    best_model,
    "cafeteria_xgboost_model.pkl"
)
print("\nModel Saved Successfully")

# ==========================================================
# STEP 9 : FUTURE DAY PREDICTION
# ==========================================================

print("\n==============================")
print("FUTURE DAY MEAL PREDICTION")
print("==============================")

# Create future day automatically

future_day = X.mean().to_frame().T

# Example future scenario

future_day["Students_Present"] = 1800
future_day["Scheduled_Classes"] = 6

# No exam

future_day["Exam_Period"] = 0

# No holiday

future_day["Holiday"] = 0

# Sunny weather

future_day["Weather"] = encoders["Weather"].transform(
    ["Sunny"]
)[0]
expected_students = int(
    future_day["Students_Present"].values[0]
)
print(
    "Expected Students:",
    expected_students
)
meal_predictions={}
for meal in [
    "Breakfast",
    "Lunch",
    "Dinner"
]:
    meal_code = encoders["Meal_Type"].transform(
        [meal]
    )[0]
    prediction_input = future_day.copy()
    prediction_input["Meal_Type"] = meal_code
    prediction = best_model.predict(
        prediction_input
    )[0]
    meal_predictions[meal]=int(prediction)
print("\nPredicted Meals")
for meal,value in meal_predictions.items():
    print(
        meal,
        "Predicted :",
        value,
        "meals"
    )

# ==========================================================
# STEP 10 : FOOD WASTE CALCULATION
# ==========================================================

total_demand = sum(
    meal_predictions.values()
)

# Traditional cafeteria preparation
# 15% extra food prepared

without_ai_prepare = int(
    total_demand * 1.15
)

# AI optimized preparation
# Only 3% extra food prepared

with_ai_prepare = int(
    total_demand * 1.03
)
without_ai_waste = (
    without_ai_prepare - total_demand
)
with_ai_waste = (
    with_ai_prepare - total_demand
)
print("\n==============================")
print("FOOD WASTE ANALYSIS")
print("==============================")
print(
    "Without AI Waste :",
    without_ai_waste,
    "meals"
)
print(
    "With AI Waste :",
    with_ai_waste,
    "meals"
)
reduction = (
    (without_ai_waste - with_ai_waste)
    /
    without_ai_waste
) * 100
print(
    "Waste Reduction :",
    round(reduction,2),
    "%"
)

# ==========================================================
# STEP 11 : AI CAFETERIA ADVICE
# ==========================================================

print("\n==============================")
print("AI CAFETERIA ADVICE")
print("==============================")
if with_ai_waste < without_ai_waste:
    print(
"""
AI Recommendation:

1. Prepare meals according to predicted demand.

2. Reduce over-preparation during low attendance days.

3. Increase food preparation during exams and campus events.

4. Consider weather conditions before planning meals.

5. Monitor previous meal demand patterns.

"""
    )
else:
    print(
"""
AI Recommendation:

Increase prediction accuracy by adding more historical cafeteria data.

"""
    )

# ==========================================================
# STEP 12 : LLAMA 3 NEXT-DAY SPECIAL MENU
# ==========================================================

import ollama

print("\n==============================")
print("GENERATIVE AI NEXT-DAY MENU")
print("==============================")

menu_prompt = f"""

You are an AI university cafeteria menu planner.

Use the following ML prediction:

Expected Students: {expected_students}

Breakfast demand: {meal_predictions['Breakfast']} meals
Lunch demand: {meal_predictions['Lunch']} meals
Dinner demand: {meal_predictions['Dinner']} meals

Food waste with AI: {with_ai_waste} meals
Waste reduction: {round(reduction, 2)}%

Create ONE practical Indian university cafeteria menu for tomorrow.

The menu must:
- be affordable
- be nutritious
- be attractive to students
- be practical to prepare in bulk
- match the predicted demand
- help reduce food waste

Return ONLY this format:

BREAKFAST: dish
LUNCH: dish
DINNER: dish

Do not provide explanations.
"""

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": menu_prompt
        }
    ]
)

special_menu = response["message"]["content"]

# Format menu into separate lines
special_menu = special_menu.replace("LUNCH:", "\nLUNCH:")
special_menu = special_menu.replace("DINNER:", "\nDINNER:")

# Save the generated menu
with open(
    r"C:\Users\rubyt\Python\Gen AI\next_day_menu.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(special_menu)

print("\n==============================")
print("NEXT DAY SPECIAL MENU")
print("==============================")
print(special_menu)

print("\nMenu saved successfully.")


# ==========================================================
# STEP 13 : CREATE COMFYUI IMAGE PROMPT
# ==========================================================

image_prompt = f"""
Create a realistic menu visualization for a university cafeteria.

Tomorrow's menu:

{special_menu}

Show the THREE actual meals from this menu:
breakfast, lunch and dinner.

Create a clear three-panel food presentation:
breakfast on the left,
lunch in the center,
dinner on the right.

Each panel should clearly show the corresponding dish.

Modern Indian university cafeteria,
realistic food photography,
clean presentation,
professional,
appetizing,
no random dishes,
no extra food items.
"""

print("\n==============================")
print("COMFYUI IMAGE PROMPT")
print("==============================")
print(image_prompt)