import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv(r'C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Cognifyz internship\Dataset.csv.csv')
  # Replace 'your_dataset.csv' with the path to your dataset CSV file
print(df.head())

# Step 2: Data Cleaning
# Remove leading and trailing whitespaces from cuisine data
df['cuisines'] = df['Cuisines'].str.strip()
# Convert cuisine data to lowercase to ensure consistency
df['cuisines'] = df['Cuisines'].str.lower()

# Step 3: Extract the cuisine information
cuisine_series = df['Cuisines']

# Step 4: Count the occurrences of each cuisine
cuisine_counts = cuisine_series.value_counts()

# Step 5: Determine the top three cuisines
top_three_cuisines = cuisine_counts.head(3)

# Step 6: Calculate the percentage of restaurants serving each of these cuisines
total_restaurants = len(df)
percentages = (top_three_cuisines / total_restaurants) * 100

# Print results
print("Top Three Cuisines:")
print(top_three_cuisines)
print("\nPercentage of Restaurants Serving Each of the Top Three Cuisines:")
print(percentages)

