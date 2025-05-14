import streamlit as st

st.header("Daily Calorie & Macro Calculator")

gender = st.selectbox("What is your gender", ("Male", "Female"))

age = st.slider("How old are you?", 0, 100, 25)

height = st.number_input("What is your height? (In meters)", value=None, placeholder=0)

weight = st.number_input("How much do you weigh? (In kilograms)", value=None, placeholder=0)

st.button("Submit")
