The goal is to build a calculator program.

Demo </br>
https://appbrewery.github.io/python-day10-demo/

Storing Functions as a Variable Value </br>
You can store a reference to a function as a value to a variable. e.g.

def add(n1, n2): </br>
    return n1 + n2
    
    
my_favourite_calculation = add </br>
my_favourite_calculation(3, 5)  # Will return 8 </br>
In the starting file, you'll see a dictionary that references each of the mathematical calculations  </br>that can be performed by our calculator. Try it out and see if you can get it to perform addition, subtraction, multiplication and division.

PAUSE 1 </br>
TODO: Write out the other 3 functions - subtract, multiply and divide.

PAUSE 2 </br>
TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

PAUSE 3 </br>
TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary. </br>

Functionality </br>
Program asks the user to type the first number. </br>
Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/") </br>
Program asks the user to type the second number. </br>
Program works out the result based on the chosen mathematical operator. </br>
Program asks if the user wants to continue working with the previous result. </br>
If yes, program loops to use the previous result as the first number and then repeats the calculation process. </br>
If no, program asks the user for the fist number again and wipes all memory of previous calculations. </br>
Add the logo from art.py </br>
 Hint 1 
 </br>Try writing out a flowchart to plan your program.
 Hint 2  </br>
To call multiplication from the operations dictionary, you would write your code like this: </br>
result = operations["*"](n1= 5, n2= 3) </br>

result would then be equal to 1. </br>