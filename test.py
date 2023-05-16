import streamlit as st

def video():
	st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if st.button("pls click"):
	st.session_state.count += 1
	video()
  
