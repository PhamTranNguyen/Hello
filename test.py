import streamlit as st

st.title("Ceasar Cipher")
st.header("by Charlie")

alphabet = 'abcdefghijklmnopqrstuvwxyz'

keys = st.number_input('key ',1)
newMessage = ''

message =  st.text_input('please enter your Message: ')

    
st.text("Deciphering or Encrypting")


def encrypt(keys,message):
    keys = (keys * -1)
    newMessage = ''
    for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + keys) % 26
        newCharacter = alphabet[newPosition]
        #print('the new Character is:', newCharacter)
        newMessage += newCharacter

      else:
        newMessage += character

    st.write('Your message is   :',newMessage)

if st.button('Encrypting'):
	encrypt(keys,message)
	
def decipher():
  newMessage = ''
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position + keys) % 26
      newCharacter = alphabet[newPosition]
      #print('the new Character is:', newCharacter)
      newMessage += newCharacter

    else:
      newMessage += character

  st.write('Your message is   :',newMessage)

if st.button("Deciphering"):
	decipher()
	


