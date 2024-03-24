import requests 
import json
import yfinance as yf
from bs4 import BeautifulSoup

API_KEY = '1WW0N090IMBDFDN4'
filename = 'response.txt'


# List of S&P 500 companies (ticker symbols)
s_and_p_500_companies = ['AAPL', 'MSFT', 'AMZN']

# Obtain S&P 500 Tickers
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a GET request to fetch the page content
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first table on the page
table = soup.find('table', {'class': 'wikitable sortable'})

# Initialize an empty dictionary to store the data
data = {}

# Loop through all rows in the table except for the header row
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if cols:
        # Extract the symbol and security name
        symbol = cols[0].text.strip()
        security = cols[1].text.strip()
        data[symbol] = security

# Print the data
sp500_ticker_list = list(data.keys())



msft = yf.Ticker("MSFT")

# get all stock info
msft.info



# Data Retrieval Iterate through each company
# for company in s_and_p_500_companies:
#     # Construct the API URL
#     url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={company}&apikey={API_KEY}'
    
#     # Send the API request
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = response.json()
        
#         # Process and store the data as needed
#         # For example, you could write it to a CSV file or store it in a database
#         # You may also want to handle error cases and rate limiting
#         with open(filename, 'w') as file:
#             json.dump(data, file, indent=4)
#     else:
#         print(f"Failed to fetch data: {response.status_code}")