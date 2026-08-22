import pandas as pd
import numpy as np

np.random.seed(42)

# ------------------------------------
# SETTINGS
# ------------------------------------

total_rows = 12000

dates = pd.date_range(
    start="2020-01-01",
    end="2026-07-31",
    freq="D"
)

date_values = np.resize(
    dates,
    total_rows
)

df = pd.DataFrame()

df["Date"] = date_values


# ------------------------------------
# Meal Type
# ------------------------------------

df["Meal_Type"] = np.random.choice(
    [
        "Breakfast",
        "Lunch",
        "Dinner"
    ],
    total_rows,
    p=[
        0.30,
        0.50,
        0.20
    ]
)


# ------------------------------------
# Calendar Features
# ------------------------------------

df["Day"] = df["Date"].dt.day_name()

df["Month"] = df["Date"].dt.month_name()

df["Year"] = df["Date"].dt.year



# ------------------------------------
# Academic Factors
# ------------------------------------

df["Students_Registered"] = np.random.randint(
    1200,
    2500,
    total_rows
)


attendance = np.random.uniform(
    0.65,
    0.95,
    total_rows
)


df["Students_Present"] = (
    df["Students_Registered"]
    *
    attendance
).astype(int)



# NEW FEATURES

df["Faculty_Present"] = np.random.randint(
    80,
    200,
    total_rows
)


df["Staff_Present"] = np.random.randint(
    50,
    150,
    total_rows
)


df["Visitors"] = np.random.randint(
    0,
    50,
    total_rows
)


df["Hostel_Students"] = np.random.randint(
    300,
    1000,
    total_rows
)


df["Total_Campus_Population"] = (
    df["Students_Present"]
    +
    df["Faculty_Present"]
    +
    df["Staff_Present"]
    +
    df["Visitors"]
)



df["Scheduled_Classes"] = np.random.randint(
    2,
    8,
    total_rows
)


df["Exam_Period"] = np.random.choice(
    [
        "Yes",
        "No"
    ],
    total_rows,
    p=[
        0.15,
        0.85
    ]
)


df["Holiday"] = np.random.choice(
    [
        "Yes",
        "No"
    ],
    total_rows,
    p=[
        0.08,
        0.92
    ]
)


df["Semester_Week"] = np.random.randint(
    1,
    18,
    total_rows
)



# ------------------------------------
# Weather Factors
# ------------------------------------

df["Weather"] = np.random.choice(
    [
        "Sunny",
        "Rainy",
        "Cloudy"
    ],
    total_rows,
    p=[
        0.55,
        0.25,
        0.20
    ]
)


df["Temperature_C"] = np.random.randint(
    18,
    38,
    total_rows
)


df["Rainfall_mm"] = np.where(
    df["Weather"]=="Rainy",
    np.random.randint(
        5,
        80,
        total_rows
    ),
    0
)


df["Humidity"] = np.random.randint(
    40,
    90,
    total_rows
)



# ------------------------------------
# Campus Events
# ------------------------------------

df["Campus_Event"] = np.random.choice(
    [
        "No Event",
        "Cultural Fest",
        "Sports Day",
        "Placement Drive",
        "Convocation"
    ],
    total_rows,
    p=[
        0.75,
        0.08,
        0.07,
        0.07,
        0.03
    ]
)


event_effect = {

    "No Event":1,
    "Cultural Fest":1.25,
    "Sports Day":1.15,
    "Placement Drive":1.05,
    "Convocation":1.30

}


df["Event_Factor"] = df["Campus_Event"].map(
    event_effect
)



# ------------------------------------
# Cafeteria Factors
# ------------------------------------

df["Special_Menu"] = np.random.choice(
    [
        "Yes",
        "No"
    ],
    total_rows,
    p=[
        0.20,
        0.80
    ]
)


df["Menu_Category"] = np.random.choice(
    [
        "Indian",
        "South Indian",
        "Chinese",
        "Continental",
        "Fast Food"
    ],
    total_rows
)


df["Meal_Price"] = np.random.randint(
    40,
    120,
    total_rows
)


df["Previous_Day_Meals_Sold"] = np.random.randint(
    500,
    2500,
    total_rows
)


df["Previous_Week_Average"] = np.random.randint(
    600,
    2500,
    total_rows
)



# ------------------------------------
# Meals Sold Target
# ------------------------------------

menu_factor = {

    "Indian":1.0,
    "South Indian":1.10,
    "Chinese":1.05,
    "Continental":0.90,
    "Fast Food":1.15

}


df["Menu_Factor"] = df["Menu_Category"].map(
    menu_factor
)


exam_factor = np.where(
    df["Exam_Period"]=="Yes",
    1.10,
    1
)


holiday_factor = np.where(
    df["Holiday"]=="Yes",
    0.25,
    1
)


special_factor = np.where(
    df["Special_Menu"]=="Yes",
    1.15,
    1
)


meal_factor = df["Meal_Type"].map(
    {
        "Breakfast":0.65,
        "Lunch":1.0,
        "Dinner":0.55
    }
)



df["Meals_Sold"] = (

    df["Total_Campus_Population"]
    *
    meal_factor
    *
    df["Event_Factor"]
    *
    df["Menu_Factor"]
    *
    exam_factor
    *
    holiday_factor
    *
    special_factor

    +

    np.random.normal(
        0,
        40,
        total_rows
    )

).astype(int)



# ------------------------------------
# Food Waste
# ------------------------------------

df["Meals_Prepared"] = (
    df["Meals_Sold"]
    +
    np.random.randint(
        20,
        150,
        total_rows
    )
)


df["Food_Waste_kg"] = round(
    (
        df["Meals_Prepared"]
        -
        df["Meals_Sold"]
    )
    *
    np.random.uniform(
        0.08,
        0.15,
        total_rows
    ),
    2
)



# ------------------------------------
# Remove Helper Columns
# ------------------------------------

df.drop(
    columns=[
        "Event_Factor",
        "Menu_Factor"
    ],
    inplace=True
)



# ------------------------------------
# Save Dataset
# ------------------------------------

file_name = (
    "cafeteria_food_waste_dataset_12000.csv"
)


df.to_csv(
    file_name,
    index=False
)


print(
    "Dataset created successfully!"
)

print(
    "File:",
    file_name
)

print(
    "Rows:",
    df.shape[0]
)

print(
    "Columns:",
    df.shape[1]
)


print("\nSample:")
print(df.head())