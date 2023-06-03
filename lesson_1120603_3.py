import streamlit as st
import datetime

def button_click():
    st.write(st.session_state)

if st.button("say Hello!",key='myButton', on_click=button_click):
    st.write("Why hello there")
else:
    st.write("Goodbye")

st.divider()

agree = st.checkbox("我同意")
if agree : 
        st.write('Great')

st.divider()

genre = st.radio(
    "您喜歡的節目是什麼",
    ('卡通', '戲劇', '愛情'))

if genre == '卡通':
    st.write('您選擇:卡通')
elif genre == "戲劇" :
    st.write("您選擇:戲劇")
elif genre == '愛情':
    st.write("您選擇:愛情")

st.divider()


option = st.selectbox(
    '您想要如何聯絡?',
    ('請選擇...','Email', '電話', '手機'))

st.write('You selected:', option)


st.divider()



options = st.multiselect(
    '請選擇您喜歡的顏色',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow'])

st.write('您選擇:', options)


st.divider()

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.divider()

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.divider()


title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


number = st.number_input('Insert a number')
st.write('The current number is ', number)


d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
