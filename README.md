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
