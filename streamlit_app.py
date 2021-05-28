import streamlit as st
import ffn
#%pylab inline

stocks = ["AGF Global Select", "Dynamic Power Global Growth", "Fidelity Global Innovators", "Edgepoint Global Portfolio"]

check_boxes = [st.sidebar.checkbox(stock, key=stock) for stock in stocks]

st.write([stock for stock, checked in zip(stocks, check_boxes) if checked])

checked_stocks = [stock for stock, checked in zip(stocks, check_boxes) if checked]

if st.button("Download data"):
    for stock in checked_stocks:
        download_data(stock)
