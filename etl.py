import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('fingraphica.db')
cursor = conn.cursor()

def clean_last_sale(last_sale):
    """Remove dollar sign ($) and convert to float."""
    return float(last_sale.replace('$', ''))

def clean_pct_sign(pct_change):
    """Remove percent sign (%) and convert to float."""
    return float(pct_change.replace('%', ''))

# Open the CSV file and read its contents
with open('filtered_sp500_prices.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Extract data from the CSV row
        symbol = row['Symbol']
        name = row['Name']
        last_sale = clean_last_sale(row['Last Sale'])
        market_cap = float(row['Market Cap'])
        pct_change = clean_pct_sign(row['% Change'])
        sector = row['Sector']
        industry = row['Industry']
        
        # Insert data into the SQLite database
        cursor.execute('''
            INSERT INTO stocks (symbol, name, last_sale, market_cap, pct_change, sector, industry)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (symbol, name, last_sale, market_cap, pct_change, sector, industry))

# Commit changes and close connection
conn.commit()
conn.close()
