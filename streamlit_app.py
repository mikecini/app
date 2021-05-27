import streamlit as st
import ffn
#%pylab inline

st.title('Global Equity Performance Tool')
st.header('This is O14s app')

prices = ffn.get('aapl,msft', start='2010-01-01')
ax = prices.rebase()

st.line_chart(ax)
