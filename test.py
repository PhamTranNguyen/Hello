import streamlit as st

st.title("Ceasar Cipher")
st.header("by Charlie")

alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = st.number_input('key: ')
newMessage = ''


st.text("Deciphering or Encrypting")
st.text("1. Deciphering")
st.text("2. Encrypting")
choice = st.number_input("Enter your choice (1 or 2): ")

if choice == "1":
  
    st.text("Decyphering...")
  
elif choice == "2":
  key = key * -1
  st.text("Encrypting...")

else:
    st.text("Invalid choice. Please enter 1 or 2.")

message =  st.text_input('please enter your Message: ')

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    #print('the new Character is:', newCharacter)
    newMessage += newCharacter
  
  else:
    newMessage += character

st.text(newMessage)

def data():
	st.text('thank')

if st.button("pls click"):
	data()
