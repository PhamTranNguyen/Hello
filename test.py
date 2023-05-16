import streamlit as st

def data():
	st.text('thank')

if st.button("pls click"):
	st.session_state.count += 1
	data()
  
