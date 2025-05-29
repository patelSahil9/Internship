import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Daily.csv')
print(df.head(10))

#Copying :-
Copy = df.copy()

print(df.isnull().sum())

# Fill missing Subcategory with 'Unknown'
df['Subcategory'].fillna('Unknown', inplace=True)

print(df.isnull().sum())

# Drop 'Note' column if it’s not important, or keep it as-is (optional)
# df.drop('Note', axis=1, inplace=True)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print(df.shape)

# Convert 'Amount' to float (if needed)
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

# Drop any rows with invalid 'Date' or 'Amount' after conversion
df.dropna(subset=['Date', 'Amount'], inplace=True)

print(df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

nd = df.to_csv('kemcho.csv')