class Game():

    def __init__(self, choice_1, choice_2):
        self.choice_1 = choice_1
        self.choice_2 = choice_2

    def play_game(self, choice_1, choice_2):
        if choice_1 == choice_2:
            return "It's a draw, dude!"  
        if choice_1 == "rock" and choice_2 == "scissors":
            result = "Player 1 wins by playing rock"
        elif choice_1 == "rock" and choice_2 == "paper":
            result = "Player 2 wins by playing paper"
        elif choice_1 == "paper" and choice_2 == "rock":
            result = "Player 1 wins by playing paper"
        elif choice_1 == "paper" and choice_2 == "scissors":
            result = "Player 2 wins by playing scissors"
        elif choice_1 == "scissors" and choice_2 == "paper":
            result = "Player 1 wins by playing scissors"
        elif choice_1 == "scissors" and choice_2 == "rock":
            result = "Player 2 wins by playing rock"
        return result