import os
import numpy as np
print(os.getcwd())

with open('./day2/input2.txt','r') as file:
    inputs = [x.strip() for x in file]

cond = {'red': 12,
        'green': 13,
        'blue': 14}

cnt = {'red': 0,
       'green': 0,
       'blue': 0}

valid_games = []
game_pow = []
for game in inputs:
    idx = game.find(':')
    game_id = int(game[5:idx])
    game = game[idx+2:]
    sets = game.split('; ')

    valid = True
    for set in sets:
        colors = set.split(', ')

        for color in colors:
            id_color = color.split(' ')
            if int(id_color[0]) > cnt[id_color[1]]:
                cnt[id_color[1]] = int(id_color[0])
            if id_color[1] in cond:
                if int(id_color[0]) > cond[id_color[1]]:
                    valid = False

    if valid:
        valid_games.append(game_id)
    
    game_pow.append(np.array(np.prod(list(cnt.values()))))
    
    cnt = {'red': 0,
           'green': 0,
           'blue': 0}
    
    
print(f'Part 1: {sum(valid_games)}')
print(f'Part 2: {sum(game_pow)}')