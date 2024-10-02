import random # Imports the random module

# Function to get the AI's choice and compare with the player's input
def get_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return 'tie'
    elif (player_choice == '1' and ai_choice == '3') or (player_choice == '2' and ai_choice == '1') or (player_choice == '3' and ai_choice == '2'):
        return 'win'
    else:
        return 'lose'

def validate_input(): #input validation for the best of 3 and best of 7 game modes
    rps = ''
    while rps not in ['1','2','3']:
        rps = input('Please type \'1\', \'2\', or \'3\', for rock, paper, and scissors, respectively: ')
    return rps


def validate_twoplayer(nPlayer): # input validation for 2 player game mode (has custom rps msg)
    rps = ''
    while rps not in ['1','2','3']:
        rps = input(f'Player {nPlayer}, Please type \'1\', \'2\', or \'3\', for rock, paper, and scissors, respectively: ')
    return rps


def validate_endless(): # input validation for endless game mode(has different valid inputs and a custom rps message)
    rps=''
    while rps not in ['1','2','3','q']:
        rps = input('Please type \'1\', \'2\', or \'3\', for rock, paper, and scissors, respectively (or \'q\' to quit.): ')
    return rps


def best3(): # Defines best of 3 game mode
    print('Let\'s begin the classic game mode!\n')
    points1 = 0
    points2 = 0
    while points1 < 3 and points2 < 3:
        rps = validate_input()
        ai_rps = str(random.randint(1, 3))
        result = get_winner(rps, ai_rps)

        if result == 'tie':
            print(f'It\'s a tie! (AI chose {ai_rps})')
        elif result == 'win':
            points1 += 1
            print(f'You win! (AI chose {ai_rps})')
        else:
            points2 += 1
            print(f'You lose! (AI chose {ai_rps})')
        
        print(f'Score: You {points1} - AI {points2}\n')

    print('Congrats! You won!' if points1 > points2 else 'Game over, you lost. Thanks for playing!')


def best7(): # Best of 7 gm
    print('Best of 7! First to 5 points wins.\n')
    points1 = 0
    points2 = 0
    while points1 < 5 and points2 < 5:
        rps = validate_input()
        ai_rps = str(random.randint(1, 3))
        result = get_winner(rps, ai_rps)

        if result == 'tie':
            print(f'It\'s a tie! (AI chose {ai_rps})')
        elif result == 'win':
            points1 += 1
            print(f'You win! (AI chose {ai_rps})')
        else:
            points2 += 1
            print(f'You lose! (AI chose {ai_rps})')
        
        print(f'Score: You {points1} - AI {points2}\n')

    print('Congrats! You won!' if points1 > points2 else 'Game over, you lost. Thanks for playing!')

def twoPlayer(): # Defines 2 player game mode
    print('Let\'s begin the two player game mode!\n')
    points1 = 0
    points2 = 0
    while points1 < 3 and points2 < 3:
        rps = validate_twoplayer(1)
        ai_rps = validate_twoplayer(2)
        result = get_winner(rps, ai_rps)

        if result == 'tie':
            print(f'It\'s a tie!')
        elif result == 'win':
            points1 += 1
            print(f'Player 1 wins!')
        else:
            points2 += 1
            print(f'Player 2 wins!')
        
        print(f'Score: P1 {points1} - P2 {points2}\n')

    print('Congrats! Player 1 won!' if points1 > points2 else 'Congrats! Player 2 won!')

def endless():
    points1 = 0
    points2 = 0
    print('Welcome to the endless gamemode! How many points can you score?')
    rps = ''
    while rps != 'q':
        rps = validate_endless()
        if rps =='q':
            break
        ai_rps = str(random.randint(1,3))
        result = get_winner(rps, ai_rps)
        if result == 'tie':
            print(f'It\'s a tie!')
        elif result == 'win':
            points1 += 1
            print(f'You win! (AI chose {ai_rps})')
        else:
            points2 += 1
            print(f'You lose! (AI chose {ai_rps})')
        
        print(f'Score: You {points1} - AI {points2}\n')

    print('Congrats! You won!' if points1 > points2 else 'Game over, you lost. Thanks for playing!')

    
def main():
    print('Welcome to Chris\' Rock Paper Scissors in Python!')
    print('1: Classic, first to 3') # First to 3 game mode
    print('2: Best of 7') # Best of 7 game mode
    print('3: 2 Player (Best of 3)') # Best of 3 2 player
    print('4: Endless\n')# Endless game mode
    print('Enter either 1, 2, 3, or 4 for your desired game mode! (or enter \'q\' to quit)')

    valid_input=['1','2','3','4','q']
    ask = input('')
    while ask not in valid_input:
        print('Invalid input, please try again.')
        ask=input('')
    if ask == '1':
        best3() # calls best of 3 function
    elif ask == '2':
        best7() # calls best of 7 function
    elif ask == '3': 
        twoPlayer() # calls 2 player function
    elif ask == '4':
        endless() # calls endless function
    elif ask.lower() == 'q':
        print('Bye!')

if __name__ == '__main__':
    main()
