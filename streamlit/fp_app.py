import streamlit as st
import pickle


# LOADING THE MODEL
def load_model():
    with open("maize_ml.pkl", "rb") as file:
        loaded_model = pickle.load(file)
        return loaded_model

# FUNCTION FOR MAKING PREDICTIONS
def make_prediction(loaded_model, date, commodity):
    prediction = 0  # Replace with your prediction code
    return prediction

# DEFINING THE FUNCTION TO RUN THE STREAMLIT APP
def main():
    # Set up the Streamlit app structure
    st.title("Food Prices Prediction - A Machine Learning Forecasting Model")
    st.text("This model has been trained to predict the potential cost of food prices in Kenya")

    # User Input and Data Collection Section - Sidebar
    st.sidebar.header("User Input Data")
    st.sidebar.text("Provide the date and commodity for Prediction")

    date = st.sidebar.date_input("Provide Date")
    commodity = st.sidebar.selectbox("Select Food Product", ["Maize", "Beans", "Milk", "Food Basket"])

    # Load the model only once
    loaded_model = load_model()

    if st.sidebar.button("Make Prediction"):
        prediction = make_prediction(loaded_model, date, commodity)
        st.write("Prediction:", prediction)

if __name__ == "__main__":
    main()
