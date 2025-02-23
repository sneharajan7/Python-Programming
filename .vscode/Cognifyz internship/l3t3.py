import pandas as pd

def analyze_price_range_services(csv_file_path):
    try:
        # Task 1: Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Task 2: Convert 'Has Online delivery' and 'Has Table booking' to numeric values
        df['Has Online delivery'] = pd.to_numeric(df['Has Online delivery'], errors='coerce')
        df['Has Table booking'] = pd.to_numeric(df['Has Table booking'], errors='coerce')

        # Task 3: Group by Price Range and Analyze Availability
        price_range_services = df.groupby('Price range')[['Has Online delivery', 'Has Table booking']].mean() * 100

        return price_range_services
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
csv_file_path = r"C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv"  # Replace with the absolute path to your CSV file
price_range_services_analysis = analyze_price_range_services(csv_file_path)
if price_range_services_analysis is not None:
    print("Percentage of Restaurants Offering Online Delivery and Table Booking by Price Range:")
    print(price_range_services_analysis)
else:
    print("Failed to analyze price range and services.")
