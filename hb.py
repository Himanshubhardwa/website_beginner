import streamlit as st
import pandas as pd

#st.title("welcome to HB world....")
#st.header("python")
#st.subheader("java")
#st.markdown(" 1. Add two number  ")
#st.code(""" a=10
#b=20
#c=a+b
#print(c)""")
#data=pd.read_csv("data.csv")
#st.dataframe(data)
name=st.text_input("Enter your name")
fname=st.text_input("Enter your father name")
address=st.text_area("Enter your text")
classdata=st.selectbox("Enter your class :",(1,2,3,4,5))
button=st.button("submit")
if button:
    st.markdown(f"""
    Name:{name}
    Father name:{fname}
    address:{address}
    class:{classdata} """)
    



                     
