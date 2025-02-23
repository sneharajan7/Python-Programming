import pandas as pd

def analyze_votes(csv_file_path):
    try:
        # Task 1: Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Task 2: Identify Restaurants with Highest and Lowest Votes
        highest_votes_restaurant = df.loc[df['Votes'].idxmax()]
        lowest_votes_restaurant = df.loc[df['Votes'].idxmin()]

        # Task 3: Correlation Analysis
        correlation = df['Votes'].corr(df['Aggregate rating'])

        return {
            "Highest Votes Restaurant": highest_votes_restaurant[['Restaurant Name', 'Votes']],
            "Lowest Votes Restaurant": lowest_votes_restaurant[['Restaurant Name', 'Votes']],
            "Correlation Coefficient": correlation
        }
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
csv_file_path = r"C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv"  # Replace with the absolute path to your CSV file
votes_analysis_results = analyze_votes(csv_file_path)
if votes_analysis_results is not None:
    print("Restaurants with Highest Votes:")
    print(votes_analysis_results["Highest Votes Restaurant"])
    print("\nRestaurants with Lowest Votes:")
    print(votes_analysis_results["Lowest Votes Restaurant"])
    print("\nCorrelation Coefficient between Votes and Rating:", votes_analysis_results["Correlation Coefficient"])
else:
    print("Failed to analyze votes.")
