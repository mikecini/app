import streamlit as st
import ffn

GS = st.checkbox('AGF Global Select')
EDG = st.checkbox('Edgepoint Global Portfolio')
DYN = st.checkbox('Dynamic Power Global Growth Portfolio')
FID = st.checkbox('Fidelity Global Innovators')
min_weight = st.number_input('Minimum Weight')
max_weight = st.number_input('Maximum Weight')


if GS and EDG is True:
  GS_EDG = ffn.get('0P000073QD.TO,0P0000IUYO.TO').to_returns().dropna()
  weights = ffn.core.calc_mean_var_weights(GS_EDG, weight_bounds=(min_weight, max_weight), rf=0.0, covar_method='ledoit-wolf')
  st.table (weights)
  
if GS and DYN is True: 
  GS_DYN = ffn.get('0P000073QD.TO,0P0000737Y.TO').to_returns().dropna()
  weights = ffn.core.calc_mean_var_weights(GS_DYN, weight_bounds=(min_weight, max_weight), rf=0.0, covar_method='ledoit-wolf')
  st.table (weights)
  
if GS and FID is True:
  GS_FID = ffn.get('0P000073QD.TO,0P0001C8AE.TO').to_returns().dropna()
  weights = ffn.core.calc_mean_var_weights(GS_FID, weight_bounds=(min_weight, max_weight), rf=0.0, covar_method='ledoit-wolf')
  st.table (weights)
