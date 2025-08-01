import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('linearmodel.pkl')

# App title
st.title("Salary Prediction App")

# User input
experience = st.number_input("Enter years of experience:", min_value=0.0, max_value=50.0, step=0.1)

# Predict button
if st.button("Predict Salary"):
    input_data = np.array([[experience]])
    predicted_salary = model.predict(input_data)[0]
    st.success(f"Predicted Salary: ₹{predicted_salary:,.2f}")









