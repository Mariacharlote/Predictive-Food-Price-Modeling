#IMPORTING THE NECCESARY LIBRARIES
import numpy as np
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from datetime import date
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from math import sqrt
import pickle



#DEFINING WEB-APP STRUCTURE
header = st.container()
data = st.container()
features =st.container()
models = st.container()




#SETTING UP THE HEADER SECTION
with header:
    st.title("Food Prices Prediction - A Machine Learning Forecasting Model")
    st.text("This model has been trained to predict the potential cost of food prices in kenya")





#SETTING UP THE DATA USER DATA COLLECTION FORM - SIDEBAR
# User Input and Data Collection Section - Sidebar
with st.sidebar:
    st.header("User Input Data")
    st.text("Provide the date and commodity for Prediction")

def display_data_collection_form():
    with st.sidebar:
        with st.form("Data Collection Form"):
            # Add input widgets for collecting data
            date = st.date_input("Provide Date")
            commodity = st.selectbox("Select Food Product", ["Maize", "Beans", "Milk", "Food Basket"])





# LOADING THE MODEL FROM PICKLE FILE FOR MAKING PREDICTIONS
with models:
    st.header("Commodity Price Predictions")

    # Load the model from the pickle file
    with open("../notebooks/maize_ml.pkl", "rb") as file:
        loaded_model = pickle.load(file)


    # Create a function to make predictions
    def make_prediction(date, commodity):
        prediction = loaded_model.predict(input_data)
        return prediction

    #Display the predictions
    st.write("Prediction:", prediction)






