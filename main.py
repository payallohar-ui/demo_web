import streamlit as st


name = st.text_input("Enter you name: ")
fname = st.text_input("Enter you father's name: ")
add = st.text_area("Enter your text: ")
classdata = st.selectbox("Enter you class: ",(1,2,3,4,5))

button = st.button("Done")
if button : 
    st.markdown(f"""
    Name : {name} 
    Father's Name : {fname}
    Address : {add} 
    class : {classdata} 
""")
