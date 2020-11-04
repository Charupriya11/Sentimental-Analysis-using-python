import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 
  
# loading in the model to predict on the data 
pickle_in = open('classifier.pkl', 'rb') 
model = pickle.load(pickle_in) 
  
def welcome(): 
    return 'Welcome all'
def prediction(user_input):   
   
    prediction = model.predict([[user_input]])
    print(prediction) 
    return prediction 
def main(): 
    st.title("Major project") 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Sentimental Analysis ML App </h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html = True) 
    user_input = st.text_area("Enter your comments")
    result ="" 
    if st.button("Predict"): 
        result = prediction(user_input) 
     
if __name__=='__main__': 
    main() 