import streamlit as st


def button_click():
    st.write(st.session_state)

if st.button("say Hello!",key='myButton', on_click=button_click):
    st.write("Why hello there")
else:
    st.write("Goodbye")



    agree = st.checkbox("我同意")

    if agree : 
        st.write('Great')


