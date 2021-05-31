import streamlit as st
import ffn
import pandas as pd
import numpy as np


GS = st.checkbox('AGF Global Select')
EDG = st.checkbox('Edgepoint Global Portfolio')
DYN = st.checkbox('Dynamic Power Global Growth Portfolio')
FID = st.checkbox('Fidelity Global Innovators')
min_weight = st.number_input('Minimum Weight')
max_weight = st.number_input('Maximum Weight')


if GS and EDG is True:
  price_data = ffn.get('0P000073QD.TO,0P0000IUYO.TO')
  log_ret = np.log(price_data/price_data.shift(1))
  cov_mat = log_ret.cov() * 252
  num_port = 5000
  all_wts = np.zeros((num_port, len(price_data.columns)))
  port_returns = np.zeros((num_port))
  port_risk = np.zeros((num_port))
  sharpe_ratio = np.zeros((num_port))
  
  for i in range(num_port):
    wts = np.random.uniform(size = len(price_data.columns))
    wts = wts/np.sum(wts)
    all_wts[i,:] = wts
    port_ret = np.sum(log_ret.mean() * wts)
    port_ret = (port_ret + 1) ** 252 - 1
    port_returns[i] = port_ret
    port_sd = np.sqrt(np.dot(wts.T, np.dot(cov_mat, wts)))
    port_risk[i] = port_sd
    sr = port_ret / port_sd
    sharpe_ratio[i] = sr
    names = price_data.columns
    min_var = all_wts[port_risk.argmin()]
    max_sr = all_wts[sharpe_ratio.argmax()]
    min_var = pd.Series(min_var, index=names)

st.bar_chart(min_var)
  
if GS and DYN is True: 
  GS_DYN = ffn.get('0P000073QD.TO,0P0000737Y.TO').to_returns().dropna()
  GS_DYN.columns=['AGF Global Select','Dynamic Power Global Growth']
  weights = ffn.core.calc_mean_var_weights(GS_DYN, weight_bounds=(min_weight, max_weight), rf=0.0)
  st.table (weights)
  
if GS and FID is True:
  GS_FID = ffn.get('0P000073QD.TO,0P0001C8AE.TO').to_returns().dropna()
  GS_FID.columns=['AGF Global Select','Fidelity Global Innovators']
  weights = ffn.core.calc_mean_var_weights(GS_FID, weight_bounds=(min_weight, max_weight), rf=0.0)
  st.table (weights)
