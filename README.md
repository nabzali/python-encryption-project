# Python Encryption Project
This repo is a personal favourite. It includes a series of python scripts (caesar.py, keyword.py, fileKeyword.py)

caesar.py - [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
-

- User enters an offset (integer between -25 and 25 inclusive).
- User also enters a message to encrypt, which will be a string.
- The message gets encrypted. Decryption will essentially work in the same way as encryption except that the offset is negated.
- Works by shifting each letter down the alphabet by a constant value, i.e by the offset.
- *e.g*: if the offset was 2, the letter *a* would change to a *c*.
- If the newly encrypted value is outside the range of the alphabet, then the algorithm ensures that we wrap around
- Only letters are encrypted.
- Expect uppercase letters in the output of this particular algorithm, regardless of letter case.

keyword.py - Vigenère cipher
-

- Invented by [Blaise de Vigenère ](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
- As well as a message to encrypt, the user enters a keyword, both of which are strings.
- The depending on the length of the message, this algorithm would concatenate the keyword with as many copies of itself as necessary until the length of the newly created keyword would match or exceed the length of the message. Once that condition is satisfied, the keyword would truncate so that its length precisely matched the length of the message.
- Encryption works by lining up the two strings and considering each corresponding pair of letters. In other words, the first letter of the keyword would pair up with the first letter of message, likewise with the second letter, and so on.
- Then, each message letter's numerical value (position in the alphabet) would be added to that of it's corresponding letter in the keyword. This would generate a new number and ultimately return a new, encrypted letter.
- *e.g*: if *tangerine* is the message and *apple* is the keyword, the new keyword would become *appleappl*
- the first letter, *t* in *tangerine* would then line up with *a*, the first letter in *appleappl* and then essentially the first newly encrypted letter would become *u*
- This is because *t* is the 20th letter of the alphabet and *a* is the 1st letter of the alphabet. 20 + 1 = 21 therefore the newly encrypted letter becomes the 21st letter of the alphabet, which is of course *u* 
- Only letters are encrypted.
- Expect uppercase letters in the output of this particular algorithm, regardless of letter case.


March 2018
