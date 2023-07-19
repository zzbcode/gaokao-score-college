import csv
from bs4 import BeautifulSoup

# Open the HTML file and read its contents
with open('山西省2023年普通高校招生第一批本科A类院校投档最低分.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all the table rows
rows = soup.find_all('tr')

# Open a CSV file for writing
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # Loop through each row and extract the data
    for row in rows:
        # Find all the table cells in the row
        cells = row.find_all('td')

        # Extract the text from each cell
        data = [cell.get_text(strip=True) for cell in cells]

        # Write the data to the CSV file
        writer.writerow(data)

print('Done!')