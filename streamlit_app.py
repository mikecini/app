import quantstats as qs
import streamlit as st
import quantstats as qs

st.title('O14')
st.header('This is O14s app')

qs.extend_pandas()
stock = qs.utils.download_returns('0P000073QD.TO')

st.pyplot(stock)
