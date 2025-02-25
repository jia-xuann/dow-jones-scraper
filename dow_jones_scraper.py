
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set headers to mimic a browser
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average"

# Send request and parse the HTML
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing Dow Jones Industrial Average components
try:
    table = soup.find("table",{"class":"wikitable"})
    
    # Extract the headers
    row_header = table.find_all("tr")[0] 
    table_header = [th.text.strip() for th in row_header.find_all("th")] 
    
    # Extract the rows of the table
    rows = table.find_all("tr")[1:]
    
    # Extract data from each row
    table_data = []
    for row in rows:
        cells = row.find_all(["th", "td"])  # Extract all cells in the row
        row_data = [cell.text.strip() for cell in cells]  # Clean and store the cell data
        table_data.append(row_data)


    # Create a DataFrame 
    df = pd.DataFrame(table_data, columns=table_header)
    
    # Save the DataFrame to a CSV file
    df.to_csv("dow_jones_components.csv", index=False)
    print("\nThe full data has been saved to 'dow_jones_components.csv'.")

    # Print a preview of the data
    print("\nPreview of Scraped Data:")
    print(df.head())

    

except Exception as e:
    print(f"Error occurred: {e}")

