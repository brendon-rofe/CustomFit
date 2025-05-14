import streamlit as st
import requests

st.header("Ask FitGPT")

prompt = st.text_area("Enter your fitness question")

if st.button("Ask"):
  if prompt.strip():
    with st.spinner("Thinking..."):
      try:
        response = requests.post("http://localhost:8000/ask", json={"prompt": prompt})
        if response.status_code == 200:
          st.success("Response:")
          if response.json()["response"] == 'I am sorry, but can you please stick to health and fitness questions.':
            st.warning('I am sorry, but can you please stick to health and fitness questions.')
          else:
            st.write(response.json()["response"])
        else:
          st.error(f"API error: {response.status_code}")
      except Exception as e:
        st.error(f"Request failed: {e}")
else:
  st.warning("Please enter a prompt")
