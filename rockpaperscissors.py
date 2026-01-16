import random
from collections import Counter

def get_moves(history):
    if len(history) < 3:
        return random.choice(["rock", "paper", "scissors"])
    common_move = Counter(history).most_common(1)[0][0]
    counters = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    return counters[common_move]

def play():

    choices= ['rock', 'paper', 'scissors']
    history= []
    

    print("------Rock, Paper, Scissors------")
    print("Type 'quit' to exit")

    while True:
        user_move= input("Enter rock, paper or scissors: ").lower()

        if user_move == 'quit':
            break
        if user_move not in choices:
            print("Invalid choice. Try again!")
            continue
    
        ai_move = get_moves(history)
        history.append(user_move)

        print(f"AI chose: {ai_move}")
        
        if user_move == ai_move:
            print("It's a tie!")
        elif (user_move == "rock" and ai_move == "scissors") or \
        (user_move == "paper" and ai_move == "scissors") or \
              user_move == "scissors" and ai_move == "rock":
            print("You win!")
        else:
            print("You lost!")
        

if __name__ == "__main__":
    play()
            