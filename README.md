# Python Encryption Project
This repo is a personal favourite. It includes a series of python scripts (caesar.py, keyword.py, fileKeyword.py)

caesar.py - The Simplest
-

- Inspired by the famous [Caesar Cipher]https://en.wikipedia.org/wiki/Caesar_cipher approach.
- User enters an offset (number between -25 and 25 inclusive).
- User also enters a message as a string.
- The message gets encrypted (or decrypted), based on the choice of the user. Decryption negates the offset.
- Works by shifting each letter down the alphabet by a constant value.
- Precisely, this value is the offset - e.g if the offset was 2, the letter *a* would change to a *c*.
- Only letters are encrypted.
- Expect uppercase letters in the output of this particular algorithm, regardless of letter case.
