import streamlit as st

st.title("Ceasar Cipher")
st.header("by Charlie")

alphabet = 'abcdefghijklmnopqrstuvwxyz'

keys = st.number_input('key ',1)
newMessage = ''


    
st.text("Deciphering or Encrypting")

def encrypt(keys):
	keys = keys * -1
	st.text('Encrypting...')

if st.button('Encrypting'):
	encrypt()
	
def decipher():
	st.text('Deciphering...')

if st.button("Deciphering"):
	decipher()
	
message =  st.text_input('please enter your Message: ')

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + keys) % 26
    newCharacter = alphabet[newPosition]
    #print('the new Character is:', newCharacter)
    newMessage += newCharacter
  
  else:
    newMessage += character

st.write('Your message is   :', newMessage)
