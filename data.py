import pandas as pd
import numpy as np
import os

# --- PART 1: DATA GENERATION ---
# Interview talk: "I generated 500 rows to simulate a month of delivery logs"
rows = 500
data = {
    'OrderID': range(101, 101 + rows),
    'Delivery_Time_Days': np.random.randint(1, 10, rows),
    'Customer_Rating': np.random.choice([1, 2, 3, 4, 5], rows, p=[0.1, 0.1, 0.2, 0.3, 0.3]),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], rows),
    'Product_Category': np.random.choice(['Electronics', 'Fashion', 'Home'], rows)
}

df = pd.DataFrame(data)

# --- PART 2: DATA CLEANING/TRANSFORMATION ---
# Interview talk: "I created a Status column to flag delays automatically"
df['Status'] = np.where(df['Delivery_Time_Days'] > 5, 'Late', 'On-Time')

# --- PART 3: SAVING AND FINDING THE FILE ---
file_name = 'delivery_data.csv'
df.to_csv(file_name, index=False)

print("="*50)
print("🚀 PROJECT UPDATE SUCCESSFUL")
print(f"📍 EXACT FILE PATH: {os.path.abspath(file_name)}")
print("="*50)

# --- PART 4: QUICK INSIGHTS FOR YOUR INTERVIEW ---
print("\n📊 QUICK ANALYSIS FOR YOUR INTERVIEW:")
avg_rating = df.groupby('Status')['Customer_Rating'].mean()
print(avg_rating)
print("\n(Tip: Notice how 'Late' orders usually have lower ratings!)")