import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import csv

# Part 1: Download NASDAQ data as CSV
def download_nasdaq_data():
    data_url = 'https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=0&download=true'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(data_url, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.content)
        headers = data["data"]["headers"].values()
        rows = data["data"]["rows"]
        
        with open('nasdaq_download.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(headers)
            for row in rows:
                row_data = [row[key] for key in data["data"]["headers"].keys()]
                csvwriter.writerow(row_data)
    else:
        print(f"Failed to download the file: Status code {response.status_code}")

# Part 2: Scrape S&P 500 tickers from Wikipedia
def get_sp500_tickers():
    sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(sp500_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable sortable'})
    sp500_tickers = {}
    
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if cols:
            symbol = cols[0].text.strip()
            security = cols[1].text.strip()
            sp500_tickers[symbol] = security
    
    return list(sp500_tickers.keys())

# Part 3: Filter NASDAQ data for S&P 500 companies and save to a new CSV
def filter_sp500_data(sp500_tickers):
    df = pd.read_csv('nasdaq_download.csv')
    filtered_df = df[df['Symbol'].isin(sp500_tickers)]
    selected_columns_df = filtered_df[['Symbol', 'Name', 'Last Sale', 'Market Cap', '% Change', 'Sector', 'Industry']]
    selected_columns_df.to_csv('filtered_sp500_prices.csv', index=False)

# Main execution flow
if __name__ == "__main__":
    download_nasdaq_data()
    sp500_tickers = get_sp500_tickers()
    filter_sp500_data(sp500_tickers)