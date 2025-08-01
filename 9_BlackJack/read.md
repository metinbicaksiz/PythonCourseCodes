Chose your difficulty</br>
Normal 😎: Use all Hints below to complete the project.</br>
Hard 🤔: Use only Hints 1, 2, 3 to complete the project.</br>
Extra Hard 😭: Only use Hints 1 & 2 to complete the project.</br>
Expert 🤯: Only use Hint 1 to complete the project.</br>
Our Blackjack Game House Rules</br>
The deck is unlimited in size.</br>
There are no jokers.</br>
The Jack/Queen/King all count as 10.</br>
The Ace can count as 11 or 1.</br>
Use the following list as the deck of cards:</br>
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]</br></br>

The cards in the list have equal probability of being drawn.</br>
Cards are not removed from the deck as they are drawn.</br>
The computer is the dealer.</br>
 Hint 1 </br>
Go to this website and try out the Blackjack game:</br>
https://games.washingtonpost.com/games/blackjack/

Then try out the completed Blackjack project here:

https://appbrewery.github.io/python-day11-demo/

 Hint 2 </br>
Read this breakdown of program requirements:</br>
http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

Then try to create your own flowchart for the program.</br>

 Hint 3 </br>
Download and read this flow chart I've created:</br>
https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

 Hint 4 </br>
Create a deal_card() function that uses the List below to return a random card.</br>
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

Remember that 11 is the Ace.

 Hint 5 </br>
Deal the user and computer 2 cards each using deal_card() and append().</br>
user_cards = []</br>

computer_cards = []</br>

 Hint 6 </br>
Create a function called calculate_score() that takes a List of cards as input and returns the sum of all the cards</br> in the List as the score. Google the sum() function to help you do this.</br>
 Hint 7 </br>
Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.</br>
 Hint 8 </br>
Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to Google to find the documentation on the Python built-in functions append() and remove().
https://developers.google.com/edu/python/lists#list-methods</br>

 Hint 9 </br>
Call the functioncalculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.</br>
 Hint 10 </br>
If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.</br>
 Hint 11 </br>
The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.</br>
 Hint 12 </br>
Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
 </br>Hint 13 </br>
Create a function called compare() and pass in the user_score and computer_score.</br>
If the computer and user both have the same score, then it's a draw.</br>
If the computer has a blackjack (0), then the user loses.</br>
If the user has a blackjack (0), then the user wins.</br>
If the user_score is over 21, then the user loses.</br>
If the computer_score is over 21, then the computer loses.</br>
If none of the above, then the player with the highest score wins.</br>
 Hint 14 </br>
Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of </br>blackjack and show the logo from art.py.