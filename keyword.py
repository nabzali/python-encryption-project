#Nabeel Ali | March 2018 | Keyword Cipher Code

def encrypt(m, k): #encrypts by adding numerical values in corresponding letters to output a new encrypted letter
    m = m.upper()
    newM = ""
    for i in range(0,len(m)):
        asciiM, asciiK = ord(m[i])-64, ord(k[i])-64 #ints
        new = asciiK + asciiM + 64
        if new < 65: #error checking - verifies that the ascii value for the new letter is in an appropriate range
            new += 26
        elif new > 90:
            new -= 26
        newM += chr(new)
    print(newM)

def decrypt(m, k): #This basically works in the same way but uses subtraction
    m = m.upper()
    newM = ""
    for i in range(0,len(m)):
        asciiM, asciiK = ord(m[i])-64, ord(k[i])-64 #ints
        new = asciiM - asciiK + 64
        if new < 65:
            new += 26
        elif new > 90:
            new -= 26
        newM += chr(new)
    print(newM)

message = input("Please enter a message")
keyword = input("Please enter a keyword")
option = input("Would you like to encrypt or decrypt")
while not (option == "e" or option == "d" or option == "E" or option == "D"):
    option = input("Invalid option, enter again")

while len(keyword) < len(message): #makes sure that the keyword and message are the same length
#if necessary - extend the keyword string by adding itself on itself as appropriate until the string
#matches the length of the message
    keyword += keyword
if len(keyword) > len(message):
    x = len(keyword)-len(message)
    keyword = keyword[:-x]

if option == "e" or option == "E":
    encrypt(message, keyword)
else:
    decrypt(message, keyword)
