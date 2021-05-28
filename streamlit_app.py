import streamlit as st
import ffn
#%pylab inline

stocks = ["0P000073QD.TO", "0P0000737Y.TO", "0P0001C8AE.TO", "0P0000IUYO.TO"]

check_boxes = [st.sidebar.checkbox(stock, key=stock) for stock in stocks]

checked_stocks = [stock for stock, checked in zip(stocks, check_boxes) if checked]

if st.button("Download data"):
    for stock in checked_stocks:
        download_data(stock)
