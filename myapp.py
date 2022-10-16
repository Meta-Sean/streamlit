import yfinance as yf
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('S&P 500 App')

st.markdown("""
This app retrieves the list of the **S&P 500** (from Wikipedia) and its corresponding **stock closing price** (year-to-date)!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('User Input Features')

@st.cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header = 0)
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')


# tickerSymbol = 'META'

# tickerData = yf.Ticker(tickerSymbol)

# tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-5-31')
# # OHLCV Dividens Stock Splits

# st.line_chart(tickerDf.Close)
# st.line_chart(tickerDf.Volume)
