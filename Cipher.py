alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('key: '))
newMessage = ''

while True:
    print("Deciphering or Encrypting")
    print("1. Deciphering")
    print("2. Encrypting")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
      
        print("Decyphering...")
      
    elif choice == "2":
      key = key * -1
      print("Encrypting...")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")
    break  


message =  input('please enter your Message: ')

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    #print('the new Character is:', newCharacter)
    newMessage += newCharacter
  
  else:
    newMessage += character

print('Your new message is:', newMessage)
