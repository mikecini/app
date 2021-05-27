import quantstats as qs
import streamlit as st
import quantstats as qs

st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.agf.com%2Fca%2Fen%2Findex.jsp&psig=AOvVaw0l4S5def0KDEDJsBHZJQkV&ust=1622234318764000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNi5pfTb6vACFQAAAAAdAAAAABAD')

st.title('O14')
st.header('This is O14s app')

qs.extend_pandas()
stock = qs.utils.download_returns('0P000073QD.TO')

st.line_chart(stock)
