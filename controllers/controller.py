import random
from flask import render_template, request
from app import app
from models.player import *
from models.game import *

@app.route('/rock-paper-scissors/')
def welcome():
    return render_template('welcome.html', title='Rock, Paper, Scissors')

@app.route('/rock-paper-scissors/play/')
def index():
    return render_template('index.html', title='Rock, Paper, Scissors')

@app.route('/rock-paper-scissors/play/<choice_1>/')
def player_1_play(choice_1):
    return render_template('player_2.html', title='Rock, Paper, Scissors', choice_1=choice_1)

@app.route('/rock-paper-scissors/play/<choice_1>/<choice_2>/')
def display_winner(choice_1, choice_2):
    player_1 = Player("You", choice_1)
    player_2 = Player("The Other You", choice_2)
    game_on = Game(player_1, player_2)
    winner_is = game_on.play_game(choice_1, choice_2)
    return render_template('result.html', title='Rock, Paper, Scissors', winner_is=winner_is, choice_1=choice_1, choice_2=choice_2)

@app.route('/rock-paper-scissors/play/computer/')
def play_vs_computer():
    return render_template('computer.html', title='Rock, Paper, Scissors')

@app.route('/rock-paper-scissors/play/computer/result/', methods=['GET', 'POST'])
def display_winner_vs_computer():
    player_name = request.values['name']
    player_choice = request.values['choice']
    new_player = Player(player_name, player_choice)

    computer_name = "Computer"
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    computer = Player(computer_name, computer_choice)
    
    game_on = Game(new_player, computer)
    winner_is = game_on.play_game(player_choice, computer_choice)
    return render_template('result_computer.html', title='Rock, Paper, Scissors', winner_is=winner_is, player_choice=player_choice, computer_choice=computer_choice, computer_name=computer_name, player_name=player_name)