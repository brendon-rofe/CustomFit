import streamlit as st

correct_username = "Brendon"
correct_password = "pass123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():

	st.title("CustomFit")
	st.header("Log in")
	username = st.text_input("Username")
	password = st.text_input("Password")

	if username == "":
		st.warning("Please enter your username")
	elif username != correct_username:
		st.error("Incorrect username")

	if password == "":
		st.warning("Please enter your password")
	elif password != correct_password:
		st.error("Incorrect password")

	if st.button("Log in") and username == correct_username and password == correct_password:
		st.session_state.logged_in = True
		st.rerun()

def logout():
    st.session_state.logged_in = False
    st.rerun()

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
ask_fitGPT = st.Page("app_pages/ask_fitGPT.py", title="Ask FitGPT", icon=":material/help:")
settings = st.Page("app_pages/settings.py", icon=":material/settings:")

pages = [ask_fitGPT, settings, logout_page]

if st.session_state.logged_in == True:
  pg = st.navigation(pages)
else:
  pg = st.navigation([st.Page(login)]) 

pg.run()
