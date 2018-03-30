#Nabeel Ali | March 2018 | Double Keyword Cipher Code - For Text File Encryption

def encrypt(contents, k, k2):
    contents = contents.upper()
    k = k.upper()
    k2 = k2.upper()
    newContents = ""
    for i in range(0, len(contents)):
        asciiC, asciiK, asciiK2 = ord(contents[i])-64, ord(k[i])-64, ord(k2[i])-64
        new = asciiC + asciiK + asciiK2
        if new > 26:
            if new > 52:
                new -= 52
            else:
                new -= 26
        elif new < 1:
            if new < -25:
                new+= 52
            else:
                new += 26
        new += 64
        newContents += chr(new)
    f.write(newContents)

def decrypt(contents, k, k2):
    contents = contents.upper()
    k = k.upper()
    k2 = k2.upper()
    newContents = ""
    for i in range(0, len(contents)):
        asciiC, asciiK, asciiK2 = ord(contents[i])-64, ord(k[i])-64, ord(k2[i])-64
        new = asciiC - (asciiK + asciiK2)
        if new > 26:
            if new > 52:
                new -= 52
            else:
                new -= 26
        elif new < 1:
            if new < -25:
                new+= 52
            else:
                new += 26
        new += 64
        newContents += chr(new)
    f.write(newContents)

keyword = input("Please enter a keyword")
keyword2 = input("Please enter a second keyword")
option = input("Would you like to encrypt or decrypt")
while not(option == "e" or option == "d" or option == "E" or option == "D"):
    option = input("Invalid option, enter again")

fileName = input("Please enter the name of the file")
if fileName[4:] != ".txt":
    fileName += ".txt"
f = open(fileName, "r")
contents = f.read()
f.close()

while len(keyword) < len(contents):
    keyword += keyword
if len(keyword) > len(contents):
    x = len(keyword)-len(contents)
    keyword = keyword[:-x]

while len(keyword2) < len(contents):
    keyword2 += keyword2
if len(keyword2) > len(contents):
    x = len(keyword2)-len(contents)
    keyword2 = keyword2[:-x]


f = open(fileName, "w")
if option == "e" or option == "E":
    encrypt(contents, keyword, keyword2)
else:
    decrypt(contents, keyword, keyword2)
f.close()
