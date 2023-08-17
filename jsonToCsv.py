import requests
import csv

# Replace this URL with the actual API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

# Extract the required fields from the JSON data
fields = ["userId", "id", "title", "body"]
rows = [[item[field] for field in fields] for item in data]

# Specify the output CSV file name
csv_file = "output.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(rows)

print("CSV file created:", csv_file)
