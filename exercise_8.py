#quit = input('Type "enter" to quit: ')
#while quit != "enter":
#    quit = input('Type "enter" to quit: ')
import sys

player_1 = input('Player 1 enter your name: ')
player_2 = input('Player 2 enter your name: ')
player_1_input = input(player_1 + ' choose rock, paper, or scissor: ')
player_2_input = input(player_2 + ' choose rock, paper, or scissor: ')

def compare(u1,u2):
    if u1 == u2:
        return('Its a tie!')
        
    elif u1 == 'rock' and u2 == 'scissors':
        return(player_1 + ' wins!')
    
    elif u1 == 'rock' and u2 == 'paper':
        return(player_2 + ' wins!')

    elif u1 == 'scissors' and u2 == 'paper':
        return(player_1 + ' wins!')

    elif u1 == 'scissors' and u2 == 'rock':
        return(player_2 + ' wins!')   
        
    elif u1 == 'paper' and u2 == 'rock':
        return(player_1 + ' wins!')   

    elif u1 == 'paper' and u2 == 'scissors':
        return(player_2 + ' wins!')

    else:
        return("Invalid input, you have not entered rock, paper, or scissors! Try again.") 
        sys.exit()
print(compare(player_1_input, player_2_input))