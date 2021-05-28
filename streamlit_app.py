import streamlit as st
import ffn
#%pylab inline

st.title('Global Equity Performance Tool')
st.header('This is O14s app')

GS = st.sidebar.checkbox ('AGF Global Select')
FID = st.sidebar.checkbox  ('FIDO Gloabl Innovators')
DYN = st.sidebar.checkbox  ('Dynamic Power Global Growth')
EDG = st.sidebar.checkbox  ('Edgepoint Global Portfolio')
MAW = st.sidebar.checkbox  ('Mawer Global Equity')
CAP = st.sidebar.checkbox  ('Capital Group Global Equity Canada')

if st.checkbox

prices = ffn.get('0P000073QD.TO,0P0000737Y.TO', start='2008-01-01')
ax = prices.rebase()

st.line_chart(ax)
