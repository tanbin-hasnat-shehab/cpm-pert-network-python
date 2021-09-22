import streamlit as st

my_text=st.text_input('label')
    
if st.button('ok'):
    
    f = open("/tmp/demofile.txt", "w")
    f.write(my_text)
    f.close()
    f = open("/tmp/demofile.txt", "r")
    st.write(f.read())
    
