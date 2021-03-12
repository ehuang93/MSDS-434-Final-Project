#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sb
#import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn import metrics
import pickle as pkl
import streamlit as st
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


model = pkl.load(open('deployment.pkl','rb'))


# In[8]:


def predict(model, input_df):
    predictions_df = model.predict(input_df)
    predictions = predictions_df
    return predictions


# In[9]:


def run():
    add_selectbox = st.sidebar.selectbox("How would you like to predict?",("Online","Batch"))
    
    st.sidebar.info('This application is intended to predict yearly amount spent based on session and membership length')
    st.title("Yearly Amount Spent Prediction App")
    
    if add_selectbox == 'Online':
        
        Average_Session_Length = st.number_input('Avg. Session Length (minutes)', min_value = 1.00000, max_value = 40.00000, value=30.00000)
        Time_on_App = st.number_input('Time on App (minutes)', min_value = 1.00000, max_value = 40.00000, value=12.00000)
        Time_on_Website = st.number_input('Time on Website (minutes)', min_value = 1.00000, max_value = 40.00000, value=37.00000)
        Length_of_Membership = st.number_input('Length of Membership (Years)', min_value = 1.00000, max_value = 7.00000, value=3.00000)
        
        output=""
        
        input_dict = {'Avg. Session Length':Average_Session_Length, 'Time on App':Time_on_App, 'Time on Website':Time_on_Website, 'Length of Membership':Length_of_Membership}
        input_df = pd.DataFrame([input_dict])
        
        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = '$' + str(output)
            
        st.success('The output is {}'.format(output))
        
    if add_selectbox == 'Batch':
        
        file_upload = st.file_uploader("Upload csv file for predictionos", type=["csv"])
        
        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = model.predict(data)
            st.write(predictions)
            s = pd.DataFrame(predictions)
            s2 = s.to_json(orient="index")
            st.json(s2)
            
if __name__ == '__main__':
    run()


# In[ ]:




