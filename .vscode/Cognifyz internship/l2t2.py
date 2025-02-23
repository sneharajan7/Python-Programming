import pandas as pd

def analyze_cuisine_combinations(csv_file_path):
    try:
        # Task 1: Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Replace NaN values in 'Cuisines' column with an empty string
        df['Cuisines'] = df['Cuisines'].fillna('')

        # Task 2: Extract cuisine combinations
        df['Cuisine Combination'] = df['Cuisines'].apply(lambda x: frozenset(x.split(', ')))
        cuisine_combinations_counts = df['Cuisine Combination'].value_counts()

        # Task 3: Determine if certain cuisine combinations tend to have higher ratings
        cuisine_combinations_avg_rating = df.groupby('Cuisine Combination')['Aggregate rating'].mean()

        return {
            "Most Common Cuisine Combinations": cuisine_combinations_counts.head(10),
            "Cuisine Combinations Average Ratings": cuisine_combinations_avg_rating
        }
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
csv_file_path = r"C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv"  # Replace with the absolute path to your CSV file
analysis_results = analyze_cuisine_combinations(csv_file_path)
if analysis_results:
    print("Most Common Cuisine Combinations:")
    print(analysis_results["Most Common Cuisine Combinations"])
    print("\nCuisine Combinations Average Ratings:")
    print(analysis_results["Cuisine Combinations Average Ratings"])
else:
    print("Failed to analyze the data.")
