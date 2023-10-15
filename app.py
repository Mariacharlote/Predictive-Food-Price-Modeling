import streamlit as st
import pickle
import numpy as np
import os

# Define a dictionary to map commodities to their respective model files
model_files = {
    "Maize": "maize1.pkl",
    "Beans": "beans_ml.pkl",
    "Milk":  "milk_ml.pkl",
    "Food Basket": "basket_ml.pkl"
}

# Load the model based on the selected commodity
#@st.cache_data  # Cache the results of this function
def load_model(commodity):
    """Load the model file for the given commodity."""
    model_file = model_files.get(commodity, None)
    if model_file:
        # Use os.path.join to construct the path of the model file
        model_path = os.path.join("models", model_file)
        try:
            # Use a try-except block to handle any errors when loading the file
            with open(model_path, "rb") as file:
                loaded_model = pickle.load(file)
            return loaded_model
        except FileNotFoundError:
            return None
        except Exception as e:
            return None
    else:
        return None

# Define the function for making predictions
def make_prediction(loaded_model, date):
    """Make a prediction using the loaded model."""
    try:
        # Using a try-except block to handle any errors when making predictions
        prediction = loaded_model.predict(np.array([date]))
        return prediction
    except Exception as e:
        return None

def main():
    st.title("Food Prices Prediction - A Machine Learning Forecasting Model")
    st.text("This model has been trained to predict the potential cost of food prices in Kenya")

    st.sidebar.header("User Input Data")
    st.sidebar.text("Provide the date and commodity for Prediction")

    date = st.sidebar.date_input("Provide Date")
    commodity = st.sidebar.selectbox("Select Food Product", ["Maize", "Beans", "Milk", "Food Basket"])

    # Load the model based on the selected commodity
    loaded_model = load_model(commodity)

    if loaded_model and st.sidebar.button("Make Prediction"):
        prediction = make_prediction(loaded_model, date)
        # Use st.markdown or st.latex to display the prediction results in a formatted way
        st.markdown(f"The predicted price of **{commodity}** on **{date}** is **{prediction}** KES per kg.")
    elif not loaded_model:
        st.error(f"No model found for {commodity}.")
        st.sidebar.text("Error: Not valid")

if __name__ == "__main__":
    main()
