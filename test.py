import streamlit as st

def video():
	st.video(https://www.youtube.com/watch?v=dQw4w9WgXcQ)

if st.button("Add new row"):
	st.session_state.count += 1
	video()
  
