import streamlit as st
import ffn

GS = st.checkbox('AGF Global Select', value = 'True')
EDG = st.checkbox('Edgepoint Global Portfolio')
DYN = st.checkbox('Dynamic Power Global Growth Portfolio')
FID = st.checkbox('Fidelity Global Innovators')

if GS is True:
  GS_Prices = ffn.get('0P000073QD.TO').to_returns().dropna()
  
if EDG is True:
  EDG_Prices = ffn.get('0P0000IUYO.TO').to_returns().dropna()
  
if DYN is True: 
  DYN_Prices = ffn.get('0P0000737Y.TO').to_returns().dropna()

if FID is True:
  FID_Prices = ffn.get('0P0001C8AE.TO').to_returns().dropna()

