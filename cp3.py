import streamlit as st



t1=st.text_input(f'{1}')
t2=st.text_input(f'{2}')
if st.button('ok'):
    
    
    f = open("/tmp/demofile.txt", "w")
    f.writelines([t1,'\n',t2])
    f.close()
    f = open("/tmp/demofile.txt", "r")
    a=f.readlines()
    st.write(a[0])
    
    
