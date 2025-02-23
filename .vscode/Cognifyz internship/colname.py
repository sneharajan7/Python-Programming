import pandas as pd

def get_column_names(csv_file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        # Get column names
        column_names = df.columns.tolist()
        return column_names
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
csv_file_path = r'C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv'  # Replace with the path to your CSV file
column_names = get_column_names(csv_file_path)
if column_names:
    print("Column Names:")
    for col in column_names:
        print(col)
else:
    print("Failed to retrieve column names.")
