import streamlit as st
import pandas 


data = {
    'Series_1':[1,2,3,4,7], 
    'Series_2':[10,20,30,100,250]
}

df = pandas.DataFrame(data)

st.title('Out First Streamlit App')
st.subheader('Introducing Streamlit in Antomate Evertthing with python')
st.write('''This is our first web App. ''')


st.write(df)
st.line_chart(df)
