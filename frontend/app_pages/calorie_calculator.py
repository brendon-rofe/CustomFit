import streamlit as st
import requests

st.header("Daily Calorie & Macro Calculator")

gender = st.selectbox("What is your gender", ("Male", "Female"))

age = st.slider("How old are you?", 0, 100, 25)

height = st.number_input("What is your height? (In meters)", value=None, placeholder=0)

weight = st.number_input("How much do you weigh? (In kilograms)", value=None, placeholder=0)

if st.button("Submit"):
  with st.spinner("Calculating..."):
    response = requests.post("http://localhost:8000/calorie-calculator", json={"gender": gender, "age": age, "height": height, "weight": weight})
    st.success("Here are your total daily calories and macros:")
    st.write("Total daily calories:", response.json()["calories"])
    st.write("Total daily protein:", response.json()["protein"])
    st.write("Total daily carbs:", response.json()["carbs"])
    st.write("Total daily fat:", response.json()["fat"])
