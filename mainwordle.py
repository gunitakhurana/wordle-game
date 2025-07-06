import random as rd
from word_list import word_list
import json 
import os 


stats = { 'games_played':0 , 'games_won':0, 'current_streak': 0, 'max_streak' : 0}

stats_file = "stats.json"

if os.path.exists(stats_file):
    with open(stats_file, "r") as f:
        stats = json.load(f)

def play_wordle():

    target_word = rd.choice(word_list)
    max_guesses = 6

    for attempt in range(max_guesses):

        while True:
            guess = input('Enter a 5 letter guess: \n').lower()
            if len(guess) != 5:
                print('That was not a valid 5 letter guess! ')
                continue

            if guess not in word_list:
                print('Not a valid guess!')
                continue

            break

        feedback = [""]*5
        target_copy = list(target_word)

        for i in range(5):

            if guess[i] == target_word[i]:
                feedback[i] = f"\033[1;92m{guess[i].upper()}\033[0m"
                target_copy[i] = None
    
        for i in range(5):        
            if feedback[i] == "":
            
                if guess[i] in target_copy:
                    feedback[i] = f"\033[1;93m{guess[i].upper()}\033[0m"
                    target_copy[target_copy.index(guess[i])] = None
                else:
                    feedback[i] = f"\033[1;90m{guess[i].upper()}\033[0m"

        print(" ".join(feedback))

        stats['games_played'] += 1
        with open(stats_file, "w") as f:
            json.dump(stats, f)

        if guess == target_word:
                stats['games_won']+= 1
                stats['current_streak']+= 1
                stats['max_streak'] = max(stats['max_streak'], stats['current_streak'])
                
                print('Congratulations! You guessed the word!!')
                break
        else:
            stats['current_streak'] = 0

    else:
        print("You're out of guesses! Sorry!") 
        print('The word is', target_word)


while True:
    play_wordle()
    again = input('Do you want to play more? Enter (yes/no):').lower()
    
    print(f"\n📊 Game Stats:")
    print(f"Games Played: {stats['games_played']}")
    print(f"Games Won: {stats['games_won']}")
    print(f"Current Streak: {stats['current_streak']}")
    print(f"Max Streak: {stats['max_streak']}")
    
    if again != 'yes':
        print('Thank you for playing!')
        break

