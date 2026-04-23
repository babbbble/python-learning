# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program; 
# the Run menu or right-click > Run options do not work in the simulated environment. 
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.
### YOUR CODE HERE ###
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Fetch the webpage content
url = "http://localhost:8000/basebell_stats.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Print the HTML content to inspect
print(soup.prettify())

# Step 3.2: Extract the Required Data
table = soup.find("table")

headers = [header.get_text(strip=True) for header in table.find_all("th")]
game_data = []

for row in table.find("tbody").find_all("tr"):
    cells = [cell.get_text(strip=True) for cell in row.find_all("td")]
    game = dict(zip(headers, cells))
    game_data.append(game)

print(game_data)

# Step 4.1: Convert to a DataFrame
# Import pandas
# pandas was imported above as pd

# Convert the game data into a pandas DataFrame
df = pd.DataFrame(game_data)

# Inspect the DataFrame
print(df.head())

# Save and print the shaped data
print(df.shape)

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sports_statistics.csv")
df.to_csv(csv_path, index=False)

print(f"Data saved to {csv_path}")
