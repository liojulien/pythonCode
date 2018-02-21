userMessage = input("Enter msg: ")
shiftValue = int(input("Enter a shift value: "))
encryptedMsg = ""
for character in userMessage:
    if character.isalpha() == True:
        x = ord(character)
        x += shiftValue
        encryptedMsg += chr(x)
    else:
        encryptedMsg += character
print("Encrypted message is: ",encryptedMsg)
