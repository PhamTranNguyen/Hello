import streamlit as st

st.title("Ceasar Cipher")
st.header("by Charlie")

alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = st.number_input('key: ')
newMessage = ''


st.text("Deciphering or Encrypting")
st.text("1. Deciphering")
st.text("2. Encrypting")

def encrypt(key):
	key = key * -1
	st.text('Encrypting...')

if st.button('Encrypting'):
	encrypt()
	
def decipher():
	st.text('Deciphering...')

if st.button("Deciphering..."):
	decipher()
	

message =  st.text_input('please enter your Message: ')

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet(newPosition)
    #print('the new Character is:', newCharacter)
    newMessage += newCharacter
  
  else:
    newMessage += character

st.text(newMessage)


