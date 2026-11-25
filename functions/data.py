import pandas as pd
import yfinance as yf

def download_data(ticker:str) -> pd.DataFrame:
    """
    Function that download a historical data frame.

    Arg:
        ticker (str): Ticker code.
    """
    
    df = yf.download(
        tickers = ticker,
        multi_level_index = False
    ).reset_index()

    return df
