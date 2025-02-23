import pandas as pd

def analyze_delivery(csv_file_path):
    try:
        # Task 1: Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Convert 'Has Online delivery' column to numeric (mapping 'yes' to 1 and 'no' to 0)
        df['Has Online delivery'] = df['Has Online delivery'].map({'yes': 1, 'no': 0})

        # Convert 'Aggregate rating' column to numeric, ignoring errors
        df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

        # Task 2: Determine the percentage of restaurants that offer online delivery
        total_restaurants = len(df)
        online_delivery_restaurants = df['Has Online delivery'].sum()
        if total_restaurants == 0:
            percentage_online_delivery = 0
        else:
            percentage_online_delivery = (online_delivery_restaurants / total_restaurants) * 100

        # Task 3: Exclude rows with missing or invalid 'Aggregate rating' values
        df_valid_ratings = df.dropna(subset=['Aggregate rating'])

        # Task 4: Compare the average ratings of restaurants with and without online delivery
        df_with_delivery = df_valid_ratings[df_valid_ratings['Has Online delivery'] == 1]
        df_without_delivery = df_valid_ratings[df_valid_ratings['Has Online delivery'] == 0]

        # Calculate average ratings
        avg_rating_with_delivery = df_with_delivery['Aggregate rating'].mean()
        avg_rating_without_delivery = df_without_delivery['Aggregate rating'].mean()

        return {
            "Percentage of Restaurants with Online Delivery": percentage_online_delivery,
            "Average Rating with Online Delivery": avg_rating_with_delivery,
            "Average Rating without Online Delivery": avg_rating_without_delivery
        }
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
csv_file_path = r'C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv'  # Replace with the path to your CSV file
analysis_results = analyze_delivery(csv_file_path)
if analysis_results:
    print("Percentage of Restaurants with Online Delivery:", analysis_results["Percentage of Restaurants with Online Delivery"])
    print("Average Rating with Online Delivery:", analysis_results["Average Rating with Online Delivery"])
    print("Average Rating without Online Delivery:", analysis_results["Average Rating without Online Delivery"])
else:
    print("Failed to analyze the data.")
