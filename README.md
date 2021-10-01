# Rock / Paper / Scissors

Create a simple flask app to allow the user to play rock, paper, scissors in their browser.

## Contents
* [Brief](#brief)
* [Technologies](#technologies)
* [Setup](#setup)

## Brief
- You should be able to go to /rock/scissors and return the string "Player 1 wins by playing rock" to the page, for example.
- Write a class to represent the player. The player will have a name and their choice (rock/paper/scissors).
- Write a game class that has a function that takes in the 2 players and compares their choices and returns the winning player. If it is a draw the player should be None type.
- Change your route to use a template to display the users choices and the result.

### Extensions:
- Add a welcome page (and a route to get it) to explain the rules before the user picks their move. Add a link to this in the base template.
- Add some CSS to either/both of your pages.

### Further extension:
- Extend the game with a new page to allow the user to play against the computer.
- If they go to /play it will take the user to a form to allow them to enter their name and choose a move from a dropdown.
- Add a link to this page to the base template.
- Write a new method in the game class to generate a computer player with the name "Computer" and a random choice from rock, paper and scissors. (Look into the random.choice) library.
- Use the same game logic and results template to display the winner.

## Technologies
The project was created with:
- Python 3
- psycog2
- HTML/CSS
- Flask

## SetUp
Pre-requisites and usage:
- Install Python3 and pip3
- Install Flask: pip3 install flask
- Install psycopg2: pip3 install psycopg2
- Clone/download the project and navigate to that directory in your terminal client
- Start Flask:
```
flask run
```
Navigate to the site in your browser at http://localhost:5000/rock-paper-scissors/
