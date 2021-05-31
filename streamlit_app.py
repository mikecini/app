import streamlit as st
import ffn

GS = st.checkbox('AGF Global Select')
EDG = st.checkbox('Edgepoint Global Portfolio')
DYN = st.checkbox('Dynamic Power Global Growth Portfolio')
FID = st.checkbox('Fidelity Global Innovators')

if GS:
  st.checkbox('AGF Global Select', value = 'True')
  GS_Returns = ffn.get('0P000073QD.TO')
  st.line_chart(GS_Returns)
