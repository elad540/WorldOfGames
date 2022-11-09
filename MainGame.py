from games import CurrencyRoulette, GuessGame, MemoryGame
import Live

name = input('Please enter your name: ')
Live.welcome(name)
while True:
    game = Live.load_game()
    if game == "q":
        exit()
    diff = int(Live.difficulty())
    if int(game) == 1:
        MemoryGame.play(diff)
    elif int(game) == 2:
        GuessGame.play(diff)
    else:
        CurrencyRoulette.play(diff)
