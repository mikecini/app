import streamlit as st
import ffn

GS = st.checkbox('AGF Global Select', value = 'True')
EDG = st.checkbox('Edgepoint Global Portfolio')
DYN = st.checkbox('Dynamic Power Global Growth Portfolio')
FID = st.checkbox('Fidelity Global Innovators')

if GS is True:
  GS_Returns = ffn.get('0P000073QD.TO')
  GS_PS = ffn.core.PerformanceStats(GS_Returns, rf = 0)

GS_PS
