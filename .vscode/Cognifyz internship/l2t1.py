import pandas as pd

def analyze_ratings(csv_file_path):
    try:
        # Task 1: Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Convert 'Aggregate rating' column to numeric, ignoring errors
        df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

        # Task 2: Analyze the distribution of aggregate ratings
        rating_counts = df['Aggregate rating'].value_counts(dropna=False)
        most_common_rating = rating_counts.idxmax()

        # Task 3: Calculate the average number of votes received by restaurants
        average_votes = df['Votes'].mean()

        return {
            "Most Common Rating": most_common_rating,
            "Average Number of Votes": average_votes
        }
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
csv_file_path = r'C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv'  # Replace with the path to your CSV file
analysis_results = analyze_ratings(csv_file_path)
if analysis_results:
    print("Most Common Rating:", analysis_results["Most Common Rating"])
    print("Average Number of Votes:", analysis_results["Average Number of Votes"])
else:
    print("Failed to analyze the data.")
