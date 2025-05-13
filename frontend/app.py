import streamlit as st

correct_username = "Brendon"
correct_password = "pass123"

if "login_status" not in st.session_state:
  st.session_state.login_status = None

def login():

	st.title("CustomFit")
	st.header("Log in")
	username = st.text_input("Username")
	password = st.text_input("Password")

	if st.button("Log in") and username == correct_username and password == correct_password:
		st.session_state.login_status = "Logged In"
		st.rerun()

ask_fitGPT = st.Page("app_pages/ask_fitGPT.py", title="Ask FitGPT", icon=":material/help:")
settings = st.Page("app_pages/settings.py", icon=":material/settings:")

pages = [ask_fitGPT, settings]

if st.session_state.login_status == "Logged In":
  pg = st.navigation(pages)
else:
  pg = st.navigation([st.Page(login)]) 

pg.run()
