"""
Download S&P 500 daily adjusted-close prices for the period 2015-01-01 to 2024-01-01.
"""

import os
import pandas as pd
import yfinance as yf
import time

# Create data directory in current workspace
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# Output file
RAW_CSV = os.path.join(DATA_DIR, "sp500_prices_raw.csv")

# Date range
START_DATE = "2015-01-01"
END_DATE = "2024-12-31"

def get_sp500_tickers():
    """Fetch current S&P 500 tickers from Wikipedia."""
    print("Fetching current S&P 500 tickers...")
    try:
        sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        sp500_table = pd.read_html(sp500_url, header=0)[0]
        tickers = sp500_table["Symbol"].tolist()
        # yfinance expects dashes instead of periods
        tickers = [t.replace('.', '-') for t in tickers]
        print(f"Successfully retrieved {len(tickers)} tickers")
        return tickers
    except Exception as e:
        print(f"Error fetching tickers: {e}")
        return None

def download_prices(tickers):
    """Download historical prices for all tickers."""
    print(f"\nDownloading prices from {START_DATE} to {END_DATE}...")
    try:
        # Download in chunks to avoid timeout
        chunk_size = 50
        all_data = []
        
        for i in range(0, len(tickers), chunk_size):
            chunk = tickers[i:i + chunk_size]
            print(f"Downloading chunk {i//chunk_size + 1}/{(len(tickers) + chunk_size - 1)//chunk_size}...")
            
            data = yf.download(
                chunk,
                start=START_DATE,
                end=END_DATE,
                interval="1d",
                auto_adjust=False,
                progress=False
            )
            
            if not data.empty:
                all_data.append(data["Adj Close"])
            
            # Small delay to avoid rate limiting
            time.sleep(1)
        
        if not all_data:
            raise Exception("No data downloaded")
            
        # Combine all chunks
        prices_raw = pd.concat(all_data, axis=1)
        print(f"Successfully downloaded data for {len(prices_raw.columns)} tickers")
        return prices_raw
        
    except Exception as e:
        print(f"Error downloading prices: {e}")
        return None

def main():
    print("Starting S&P 500 data download...")
    
    # Get tickers
    tickers = get_sp500_tickers()
    if not tickers:
        return
    
    # Download prices
    prices_raw = download_prices(tickers)
    if prices_raw is None:
        return
    
    # Save raw data
    prices_raw.to_csv(RAW_CSV)
    print(f"\nSaved raw prices to '{RAW_CSV}'")
    print(f"Raw data shape: {prices_raw.shape}")
    
    print("\nDownload completed successfully!")

if __name__ == "__main__":
    main() 