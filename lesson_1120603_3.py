import streamlit as st


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