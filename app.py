import streamlit as st # python -m streamlit run app.py
import joblib
import numpy as np
import base64
import streamlit.components.v1 as components
# background
def set_bg_video():
    video_file = open("138962-770800093.mp4", "rb")
    video_bytes = video_file.read()
    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: transparent;
        }}

        #bg-video {{
            position: fixed;
            top: 0;
            left: 0;
            min-width: 100vw;
            min-height: 100vh;
            object-fit: cover;
            z-index: -1;
        }}

        .overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.4);
            z-index: -1;
        }}
        .block-container {{
            background: rgba(255, 255, 255,0.9);
            padding: 2rem;
            border-radius: 20px;
        }}
          <h1 style='color:black; text-align:center;'>☀ SOLAR POWER PREDICTION MODEL</h1>
        </style>

        <div class="overlay"></div>

        <video autoplay muted loop id="bg-video">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )

set_bg_video()

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






















