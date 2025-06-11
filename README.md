# Pair Trading Strategy

This repository contains a comprehensive pair trading strategy implementation using Python. The project includes data fetching, pair selection, cointegration analysis, signal generation, and backtesting components.

## Project Structure

- `data_fetch.py`: Script to download S&P 500 historical price data
- `data_prep.ipynb`: Data preparation and preprocessing notebook
- `pair_selection.ipynb`: Implementation of pair selection methodology
- `cointegration.ipynb`: Cointegration analysis for selected pairs
- `signal.ipynb`: Trading signal generation
- `backtesting.ipynb`: Strategy backtesting and performance analysis
- `Pnl.ipynb`: Profit and loss analysis

## Setup Instructions

1. Clone the repository:
```bash
git clone [your-repository-url]
cd pair-trading
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run Jupyter notebooks:
```bash
jupyter notebook
```

## Data

The project uses S&P 500 historical price data from 2015 to 2024. Data is automatically downloaded using the `data_fetch.py` script.

## Dependencies

- Python 3.x
- pandas
- numpy
- yfinance
- matplotlib
- scipy
- statsmodels
- jupyter

## License

MIT License 