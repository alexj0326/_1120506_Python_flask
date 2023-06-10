
import streamlit  as st
import pandas as pd

codeFrame = pd.read_csv('codeSearch.csv',usecols=['code','name'])
codeSeries = codeFrame['code'].astype(str) + codeFrame['name']


with st.sidebar:
    #st.write('請選擇股票代號:')
    #st.multiselect('請選擇股票代號:', codeFrame)
    select_Codes  = st.multiselect("請選擇股票:",codeSeries, max_selections=4)

for code in select_Codes : 
    code = code[:4] + '.TW'
    st.write(code)



