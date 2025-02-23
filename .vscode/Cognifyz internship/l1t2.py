import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv(r'C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv')  # Replace 'your_dataset.csv' with the path to your dataset CSV file
# Step 2: Data Cleaning
# Remove leading and trailing whitespaces from city data
df['City'] = df['City'].str.strip()
# Convert city data to lowercase to ensure consistency
df['City'] = df['City'].str.lower()

# Step 3: Identify the city with the highest number of restaurants
city_restaurant_counts = df['City'].value_counts()
city_with_highest_restaurants = city_restaurant_counts.idxmax()

# Step 4: Identify the column for ratings
rating_column = [col for col in df.columns if 'rating' in col.lower()]
if not rating_column:
    print("Rating column not found in the dataset.")
else:
    # Step 5: Calculate the average rating for restaurants in each city
    city_avg_rating = df.groupby('City')[rating_column[0]].mean()

    # Step 6: Determine the city with the highest average rating
    city_with_highest_avg_rating = city_avg_rating.idxmax()

    # Print results
    print("City with the Highest Number of Restaurants:", city_with_highest_restaurants)
    print("\nAverage Rating for Restaurants in Each City:")
    for city, avg_rating in city_avg_rating.items():
        print(city, ':', avg_rating)
    print("\nCity with the Highest Average Rating:", city_with_highest_avg_rating)
