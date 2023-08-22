import pandas as pd
import random

# Load your existing dataset
df = pd.read_csv('GHW_Index.csv')

# Function to apply data augmentation
def augment_data(row):
    augmented_rows = []
    for _ in range(3):  # Create 3 augmented samples per original sample
        new_row = row.copy()  # Create a copy of the original row
        new_row['Height'] *= random.uniform(0.95, 1.05)  # Vary the Height
        new_row['Weight'] *= random.uniform(0.95, 1.05)  # Vary the Weight
        augmented_rows.append(new_row)
    return augmented_rows

# Apply augmentation to each row and create a new DataFrame
augmented_data = []
for index, row in df.iterrows():
    augmented_data.extend(augment_data(row))

augmented_df = pd.DataFrame(augmented_data)

# Convert 'Weight' and 'Height' columns to integers
augmented_df['Weight'] = augmented_df['Weight'].astype(int)
augmented_df['Height'] = augmented_df['Height'].astype(int)
# Save the augmented data to a new CSV file

augmented_df.to_csv('augmented_dataset2.csv', index=False)
