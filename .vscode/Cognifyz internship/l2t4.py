import pandas as pd

def analyze_restaurant_chains(csv_file_path):
    try:
        # Task 1: Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Task 2: Identify Restaurant Chains
        chains = df.groupby('Restaurant Name').filter(lambda x: len(x) > 1)['Restaurant Name'].unique()

        # Task 3: Analyze Ratings and Popularity for each chain
        chain_data = []
        for chain in chains:
            chain_df = df[df['Restaurant Name'] == chain]
            chain_avg_rating = chain_df['Aggregate rating'].mean()
            chain_total_votes = chain_df['Votes'].sum()
            chain_data.append({'Restaurant Chain': chain, 'Average Rating': chain_avg_rating, 'Total Votes': chain_total_votes})

        return pd.DataFrame(chain_data)
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
csv_file_path = r"C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv"  # Replace with the absolute path to your CSV file
chain_analysis_results = analyze_restaurant_chains(csv_file_path)
if chain_analysis_results is not None:
    print("Restaurant Chains Analysis:")
    # Print analysis results excluding non-ASCII characters
    for column in chain_analysis_results.columns:
        chain_analysis_results[column] = chain_analysis_results[column].astype(str).str.encode('ascii', 'ignore').str.decode('ascii')
    print(chain_analysis_results)
else:
    print("Failed to analyze restaurant chains.")
