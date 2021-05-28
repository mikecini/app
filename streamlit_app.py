import streamlit as st
import ffn
#%pylab inline

st.title('Global Equity Performance Tool')
st.header('This is O14s app')

st.checkbox ('AGF Global Select')
st.checkbox ('FIDO Gloabl Innovators')
st.checkbox ('Dynamic Power Global Growth')
st.checkbox ('Edgepoint Global Portfolio')
st.checkbox ('Mawer Global Equity')
st.checkbox ('Capital Group Global Equity Canada')


prices = ffn.get('0P000073QD.TO,0P0000737Y.TO', start='2008-01-01')
ax = prices.rebase()

st.line_chart(ax)
