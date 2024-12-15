import streamlit as st

# App Title
st.title("Health Score Predictor")

# Description
st.write("""
Your Health Score Predictor Based on <br>
Age, BMI, Diet Quality, Sleep Hours, Alcohol Consumption and Exercse Frequency
""", unsafe_allow_html=True)

# User Inputs
c = 61.736133574711964  # Adjusted constant
Age = st.number_input("Please Enter your Age (0-100 years):", value=30.0, step=1.0)
BMI = st.number_input("Please Enter your BMI (10-40):", value=25.0, step=0.1)
DQ = st.number_input("Please Enter your Diet Quality (20-110):", value=60.0, step=1.0)
SH = st.number_input("Please Enter your Sleep Hours (2-12 hours):", value=7.0, step=0.1)
AC = st.number_input("Please Enter your Alcohol Consumption (0-10):", value=2.0, step=0.1)
EF = st.number_input("Please Enter your Exercise Frequency (0-6):", value=3.0, step=1.0)

# Calculate y
if st.button("Calculate Health Score"):
    y = (-0.22344237 * Age) - (1.15881011 * BMI) + (0.6065295 * DQ) + (2.56750147 * SH) - (1.01857043 * AC) + (1.78071941 * EF) + 61.606933040384845
    st.success(f"Your Health Score is: {y:.2f}")



