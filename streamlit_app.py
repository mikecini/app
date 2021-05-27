import streamlit as st
import ffn
#%pylab inline

st.title('Global Equity Performance Tool')
st.header('This is O14s app')

st.selectbox ('Select 2 Funds',[AGF Global Select, Fidelity Global Innovators,Dynamic Power Global Growth])


prices = ffn.get('0P000073QD.TO,0P0000737Y.TO', start='2008-01-01')
ax = prices.rebase()

st.line_chart(ax)
