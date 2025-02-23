import folium
import pandas as pd

def plot_restaurant_locations(csv_file_path):
    try:
        # Task 1: Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Task 2: Plot restaurant locations on a map
        map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)

        for index, row in df.iterrows():
            folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(map)

        return map
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
csv_file_path = r"C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv"  # Replace with the absolute path to your CSV file
map = plot_restaurant_locations(csv_file_path)
if map:
    map.save("restaurant_locations.html")
    print("Restaurant locations plotted successfully. Check 'restaurant_locations.html' file.")
else:
    print("Failed to plot restaurant locations.")
