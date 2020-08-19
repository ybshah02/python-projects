import random

#==========================================
# Purpose: The function computes the power of x^y
# Input Parameter(s):
# x = base
# y = exponent
# Return Value(s): value of power
#==========================================

def expo(x,y):
    i = 0
    j = 0
    prod = 1
    while i < y:
        total = 0
        while j < x:
            total += prod
            j+=1
        prod = total
        i+=1
        j=0
    return prod

#==========================================
# Purpose: The function creates a round of the game Rock, Paper, and Scissors, in which
# a player chooses R, P, or S and the computer randomly chooses R, P, or S as well. The compter
# then declares the winner of the round
# Input Parameter(s): None
# Return Value(s): returns 1 if player wins the round, returns -1 if computer wins the round, returns 0 if round ends in a tie
#==========================================

def rps_round():
    player_choice = input('Enter R, P, or S: ')
    if player_choice != "R" and player_choice != "P" and player_choice != "S":
        while player_choice != "R" and player_choice != "P" and player_choice != "S":
            print("Invalid Input")
            player_choice = input('Enter R, P, or S: ')

    comp_move = random.choice('RPS')
    print("Computer selects " + comp_move)
    if player_choice == 'R' and comp_move == 'P':
        print("Computer Wins!")
        return -1
    elif player_choice == 'R' and comp_move == 'S':
        print("Player Wins!")
        return 1
    elif player_choice == 'P' and comp_move == 'S':
        print("Computer Wins!")
        return -1
    elif player_choice == 'P' and comp_move == 'R':
        print("Player Wins!")
        return 1
    elif player_choice == 'S' and comp_move == 'R':
        print("Computer Wins!")
        return -1
    elif player_choice == 'S' and comp_move == 'P':
        print("Player Wins!")
        return 1
    elif player_choice == comp_move:
        print("It was a tie!")
        return 0

#==========================================
# Purpose: (What does the function do?)
# Input Parameter(s): The function creates a game of Rock, Paper, and Scissors that is played
# until a player reaches a certain amount of wins, declared by the user
# num_wins = number of wins a player has to receive until they win the game
# Return Value(s): returns 1 if the player wins the game, returns -1 if the computer wins the game
#==========================================

def rps_game(num_wins):
    player_wins = 0
    comp_wins = 0
    while player_wins <= num_wins or comp_wins <= num_wins:
        round_result = rps_round()
        if round_result == 1:
            player_wins+=1
        elif round_result == -1:
            comp_wins+=1
        print("Player:", player_wins)
        print("Computer:", comp_wins,"\n")
        if player_wins == num_wins:
            return 1
        elif comp_wins == num_wins:
            return -1
