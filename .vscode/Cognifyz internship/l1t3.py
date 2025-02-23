import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv(r'C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv')  # Replace 'your_dataset.csv' with the path to your dataset CSV file

# Step 2: Data Cleaning (if necessary)
# No specific data cleaning needed for this task

# Step 3: Visualize the distribution of price ranges
plt.figure(figsize=(8, 6))
df['Price range'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Price Ranges Among Restaurants')
plt.xlabel('Price range')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0)  # Rotate x-axis labels if necessary
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Step 4: Calculate the percentage of restaurants in each price range category
price_range_percentage = df['Price range'].value_counts(normalize=True) * 100

# Print the percentage of restaurants in each price range category
print("Percentage of Restaurants in Each Price Range Category:")
print(price_range_percentage)
