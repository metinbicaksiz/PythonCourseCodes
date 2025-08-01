You are going to build an encryption and decryption program using the Caesar cipher.

Demo
https://appbrewery.github.io/python-day8-demo/

TODO-1:
Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.

TODO-2:
Inside the 'encrypt' function, shift each letter of the original_text forwards in the </br> alphabet by the shift_amount and print the encrypted text.

You can use the built-in Python index() function to find out the position of an item in a list. e.g.

fruits = ["Apple", "Pear", "Orange"] </br>
fruits.index("Pear") #1 </br>
e.g. If we have following values:  </br>

plain_text = "hello"  </br>
shift_amount = 1</br>
The final encrypted output should be:

Here is the encoded result: ifmmp

Where each of the letters of 'hello' is shifted up by 1.

 Hint 1 </br>
Let's breakdown the problem:
You need a for loop to loop through each of the letters in the plain_text. </br>
Find the position of each letter in the alphabet List </br>
Add the user desired shift_amount to the position to get the position of the encoded </br> letter.
Find the corresponding letter for that position. </br>
Add each encoded letter to a new string and print it out after the loop ends.</br></br>
TODO-3:
Call the encrypt() function and pass in the user inputs. </br>
 You should be able to test the code and encrypt a message.

TODO-4:
What happens if you try to shift the letter 'z' forwards by 9? </br>Can you fix the code?

 Hint 2 </br>
There are many approaches to do this. </br>
1. You can add more than 1 set of the alphabet into the List of alphabet letters. </br>
2. You can shift the shift_amount so that it is always within 0 - 25 and fits in the List. </br>
3. You can use the modulo to get the remainder.

<strong>Step 2</strong></br></br>
TODO-1:
Create a function called decrypt() that takes original_text and shift_amount as 2 inputs.

TODO-2:
Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text.

Hint 1 </br>
You can multiply any number by -1 to make it a negative number.

TODO-3:</br>
Combine the encrypt() and decrypt() functions into a single function called caesar().</br>
Use the value of the user chosen direction variable to determine which functionality to</br> use.
call the caesar function instead of encrypt/decrypt and pass in all three variables </br>direction/text/shift.
 </br>Hint 2 </br>
Remember that when you multiply a number by -1 it will reverse its sign. </br> e.g. 3 + ( 5 * -1) is the same as 3 - 5.
 </br>Hint 3 </br>
It should say:
Here is the encoded result: XXX

or

Here is the decoded result: XXX</br></br>
<strong>Step 3</strong></br></br>
TODO-1:</br>
Import and print the logo from art.py when the program starts.

TODO-2:</br>
What happens if the user enters a number/symbol/space that's not in the List alphabet?

Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

e.g.

original_text = "meet me at 3!"
cipher_text = "XXXX XX XX 3!"</br>
 Hint 1 </br>
If it's not a letter in the List alphabet, maybe you can just add it to the end of cipher_text as the unmodified character?
</br>TODO-3:</br>
Can you figure out a way to restart the cipher program?

e.g.

Type 'yes' if you want to go again. Otherwise, type 'no'.

If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again.

 Hint 2 </br>
Try creating a while loop that continues to execute the program if the user types 'yes'.

