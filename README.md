# Python Encryption Project (Part of 2016/17 CS Coursework)
Encryption allows data to be sent securely across public networks (such as the internet) by masking the data in a manner that only the intended recipient should be able to interpret it, provided they have the correct 'key' to decode the data.

In the 1940s (during WW2), the art of cryptography was something exploited by the Germans, who encrypted their messsages to their compatriots, ensuring Britain could not eavesdrop on them.

Now, cryptography plays a huge role in the foundation of the internet, where millions (or perhaps billions) of people are communicating and sharing sensitive data, such as bank details.

In this repository, you will find 3 scripts. *caesar.py* and *keyword.py* and *fileKeyword.py*.
Each script contains the implementation of an encryption algorithm, but have varying levels of strength/security.
**No third party libraries are used in this project.**

1: caesar.py - [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
-
<br><img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Caesar_cipher_left_shift_of_3.svg/1200px-Caesar_cipher_left_shift_of_3.svg.png" alt = "Caesar Cipher" style="margin:auto" width = "500px" height = "200px"><br>

- User enters an `offset` (integer between -25 and 25 inclusive).
- User also enters a `message` to encrypt, which will be a string.
- The message gets encrypted. Decryption will basically work in the same way as encryption except that the offset is negated.
- Works by shifting each letter down the alphabet by a constant value, i.e by the offset.
- *e.g*: if the offset was 2, the letter *a* would change to a *c*.
- If the newly encrypted value exceeds the letter *z*, then we continue by going back to the beginning of the alphabet, and so the letter *a* will follow the *z*. Similarly, we wrap around to the back of the alphabet when a newly encrypted value preceeds the letter *a*.
- Only letters are encrypted.
- Expect uppercase letters in the output of this particular algorithm, regardless of letter case.

2: keyword.py - [Vigenère Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
-

- Invented by Blaise de Vigenère
- As well as a `message` to encrypt, the user enters a `keyword`, both of which are strings.
- The depending on the length of the `message`, this algorithm would concatenate the `keyword` with as many copies of itself as necessary until the length of the newly created `keyword` would match or exceed the length of the `message`. Once that condition is satisfied, the `keyword` would truncate so that its length precisely matched the length of the `message`.
- Encryption works by lining up the two strings and considering each corresponding pair of letters. In other words, the first letter of the `keyword` would pair up with the first letter of `message`, likewise with the second letter, and so on.
- Then, the numerical value (position in the alphabet) of each letter in the message would be added to that of it's corresponding letter in the `keyword`. This would generate a new number and ultimately return a new, encrypted letter.
- *e.g*: if *tangerine* is the `message` and *apple* is the `keyword`, the new `keyword` would become *appleappl*
- the first letter, *t* in *tangerine* would then line up with *a*, the first letter in *appleappl* and then essentially the first newly encrypted letter would become *u*
- This is because *t* is the 20th letter of the alphabet and *a* is the 1st letter of the alphabet. 20 + 1 = 21 therefore the newly encrypted letter becomes the 21st letter of the alphabet, which is of course *u* 
- Only letters are encrypted.
- Expect uppercase letters in the output of this particular algorithm, regardless of letter case.

3: fileKeyword.py - Double Keyword Cipher (with file handling)
-
- Fundamentally, this is the same algorithm as that used in the Vigenère Cipher except that there are two keywords used, which makes this the most secure method of encryption amongst these three.
- Apart from this, there is also file handling in this particular python script and as such the user has the ability to encrypt text files
- It is worth noting that the use of two keywords means there is more error checking involved to ensure that a valid ecnrypted letter is returned.
