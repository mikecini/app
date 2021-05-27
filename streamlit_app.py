import quantstats as qs
import streamlit as st
import quantstats as qs

st.image('https://pbs.twimg.com/profile_images/973653394320646144/1ujH6gL6_400x400.jpg')

st.title('O14')
st.header('This is O14s app')

qs.extend_pandas()
stock = qs.utils.download_returns('0P000073QD.TO')

st.line(stock)
