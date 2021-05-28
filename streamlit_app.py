import streamlit as st
import ffn


stocks = ["0P000073QD.TO", "0P0000737Y.TO", "0P0001C8AE.TO", "0P0000IUYO.TO"]

check_boxes = [st.sidebar.checkbox(stock, key=stock) for stock in stocks]
checked_stocks = [stock for stock, checked in zip(stocks, check_boxes) if checked]

prices = ffn.get(stock, start='2008-01-01').dropna()

lookback = ffn.core.calc_perf_stats(prices)
  
st.table(lookback.iloc[0:3])  
  
