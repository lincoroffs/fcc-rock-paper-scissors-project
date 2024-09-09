# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

moves = ['R', 'P', 'S']
ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
use_mc = True
key_tuples = ['RR', 'RP', 'RS', 'PR', 'PP', 'PS', 'SR', 'SP', 'SS']
mat = {}
mmr = 0.9
my_history = []

def player(prev_play, opponent_history=[]):
    
    guess = random.choice(moves)
    
    if use_mc == True:
        
        global mat, my_history
        
        if prev_play == '':
            for key_tuple in key_tuples:
                mat[key_tuple] = {'R': 1 / 3, 'P': 1 / 3, 'S': 1 / 3}
                
            opponent_history = []
            my_history = []
        else:
            opponent_history.append(prev_play)
        
        if len(my_history) >= 2:
            prev_pair = my_history[-2] + opponent_history[-2]
            for rps_key in mat[prev_pair]:
                mat[prev_pair][rps_key] = mmr * mat[prev_pair][rps_key]
            
            mat[prev_pair][prev_play] += 1
            
            last_pair = my_history[-1] + opponent_history[-1]
            
            if max(mat[last_pair].values()) != min(mat[last_pair].values()):
                prediction = max([(v, k) for k, v in mat[last_pair].items()])[1]
                guess = ideal_response[prediction]
        
        my_history.append(guess)

    return guess
