import re
from flask import render_template
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