import quantstats as qs
import streamlit as st
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt

st.title('Global Equity Performance Tool')
st.header('This is O14s app')

qs.extend_pandas()
stock = qs.utils.download_returns('0P000073QD.TO')

