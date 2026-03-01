import pandas as pd
import numpy as np
import os

# 1. Automatically find the folder this script is saved in
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Attach the filename to that exact folder path
csv_path = os.path.join(script_dir, 'superstore.csv')

# 3. Load the dataset using the absolute path
df = pd.read_csv(csv_path, encoding='latin-1')


# --- DATA CLEANING ---

# 1. Handle Missing Values
df.dropna(subset=['Sales', 'Profit', 'Customer.Name'], inplace=True)

# 2. Remove Duplicates
df.drop_duplicates(inplace=True)

# 3. Convert Order Date to datetime format
df['Order.Date'] = pd.to_datetime(df['Order.Date'], errors='coerce')

# 4. Ensure Sales and Profit are numeric
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

# 5. Clean Column Names
df.columns = [c.replace(".", "_") for c in df.columns]

# --- SAVE THE CLEANED DATA ---
output_filename = 'cleaned_superstore.csv'
df.to_csv(output_filename, index=False)

print("Data Cleaning Complete. Info:")
print(df.info())
print(f"\nSuccess: Cleaned data saved as '{output_filename}' in your current directory.")