import streamlit as st
import ffn
import pandas as pd
import numpy as np

GS = st.checkbox('AGF Global Select')
EDG = st.checkbox('Edgepoint Global Portfolio')
DYN = st.checkbox('Dynamic Power Global Growth Portfolio')
FID = st.checkbox('Fidelity Global Innovators')
CAP = st.checkbox('Capital Group Global Equity Canada')
MAW = st.checkbox('Mawer Global Equity')
from_date = st.date_input('From Date')

if GS and EDG is True:
  price_data = ffn.get('0P000073QD.TO,0P0000IUYO.TO', start = from_date)
  price_data.columns = ['AGF Global Select','Edgepoint Global Portfolio']
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
    max_sr = pd.Series(max_sr, index=names)
  
  rebase = ffn.core.rebase(price_data, value= 1)
  st.title('Performance')
  st.line_chart(rebase)
  
  st.title('Minimum Variance Portfolio')
  st.bar_chart(min_var)
  st.table(min_var)
  
  st.title('Maximum Sharpe Portfolio')
  st.bar_chart(max_sr)
  st.table(max_sr)
    
if GS and DYN is True:
  price_data = ffn.get('0P000073QD.TO,0P0000737Y.TO',start = from_date)
  price_data.columns = ['AGF Global Select','Dynamic Power Global Growth']
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
    max_sr = pd.Series(max_sr, index=names)
  
  rebase = ffn.core.rebase(price_data, value= 1)
  st.title('Performance')
  st.line_chart(rebase)
  
  st.title('Minimum Variance Portfolio')
  st.bar_chart(min_var)
  st.table(min_var)
  
  st.title('Maximum Sharpe Portfolio')
  st.bar_chart(max_sr)
  st.table(max_sr)
  
if GS and FID is True:
  price_data = ffn.get('0P000073QD.TO,0P0001C8AE.TO',start = from_date)
  price_data.columns = ['AGF Global Select','Fidelity Global Innovators']
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
    max_sr = pd.Series(max_sr, index=names)
  
  rebase = ffn.core.rebase(price_data, value= 1)
  st.title('Performance')
  st.line_chart(rebase)
  
  
  st.title('Minimum Variance Portfolio')
  st.bar_chart(min_var)
  st.table(min_var)
  
  st.title('Maximum Sharpe Portfolio')
  st.bar_chart(max_sr)
  st.table(max_sr)

  
if GS and CAP is True:
  price_data = ffn.get('0P000073QD.TO,0P000071YR.TO',start = from_date)
  price_data.columns = ['AGF Global Select','Captial Group Global Equity Canada']
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
    max_sr = pd.Series(max_sr, index=names)
  
  rebase = ffn.core.rebase(price_data, value= 1)
  st.title('Performance')
  st.line_chart(rebase)
  
  st.title('Minimum Variance Portfolio')
  st.bar_chart(min_var)
  st.table(min_var)
  
  st.title('Maximum Sharpe Portfolio')
  st.bar_chart(max_sr)
  st.table(max_sr)

  
if GS and MAW is True:
  price_data = ffn.get('0P000073QD.TO,0P0000MOFR.TO',start = from_date)
  price_data.columns = ['AGF Global Select','Mawer Global Equity']
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
    max_sr = pd.Series(max_sr, index=names)
  
  rebase = ffn.core.rebase(price_data, value= 1)
  st.title('Performance')
  st.line_chart(rebase)  
  
  st.title('Minimum Variance Portfolio')
  st.bar_chart(min_var)
  st.table(min_var)
  
  st.title('Maximum Sharpe Portfolio')
  st.bar_chart(max_sr)
  st.table(max_sr)
