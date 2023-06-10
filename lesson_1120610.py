
import streamlit  as st
import pandas as pd

codeFrame = pd.read_csv('codeSearch.csv',usecols=['code','name'])
codeSeries = codeFrame['code'].astype(str) + codeFrame['name']


with st.sidebar:
    #st.write('請選擇股票代號:')
    #st.multiselect('請選擇股票代號:', codeFrame)
    st.multiselect("請選擇股票:",codeSeries, max_selections=4)