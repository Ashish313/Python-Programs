import time
import random


# display the board
def display_board(board):
    print('\t       |       |       ')
    print('\t___' + board[0] + '___|___' + board[1] + '___|___' + board[2]+'___')
    print('\t       |       |       ')
    print('\t___' + board[3] + '___|___' + board[4] + '___|___' + board[5]+'___')
    print('\t       |       |       ')
    print('\t   ' + board[6] + '   |   ' + board[7] + '   |   ' + board[8])
    print()


# check if player won or not
def won(board,turn):
    if board[0] == turn and board[1]  == turn and board[2] == turn:
        return True

    elif board[0] == turn and board[3]  == turn and board[6] == turn:
        return True

    elif board[0] == turn and board[4]  == turn and board[8] == turn:
        return True

    elif board[1] == turn and board[4]  == turn and board[7] == turn:
        return True

    elif board[2] == turn and board[4]  == turn and board[6] == turn:
        return True

    elif board[2] == turn and board[5]  == turn and board[8] == turn:
        return True

    elif board[3] == turn and board[4]  == turn and board[5] == turn:
        return True

    elif board[6] == turn and board[7]  == turn and board[8] == turn:
        return True

    else:
        return False



def play():   

    while True:
        
        # display th board showing available moves
        print()
        print('The moves are as according:-')
        print()
        print('\t       |       |       ')
        print('\t___1___|___2___|___3___')
        print('\t       |       |       ')
        print('\t___4___|___5___|___6___')
        print('\t       |       |       ')
        print('\t   7   |   8   |   9')
        print()

        # initializing the board list
        board=['_','_','_','_','_','_',' ',' ',' ']

        # asking the player to choose their symbol
        symbol = input('Choose you symbol (X or O): ')
        if symbol.upper() == 'X':
            player_symbol = 'X'
            computer_symbol = 'O'

        elif symbol.upper() == 'O':
            player_symbol = 'O'
            computer_symbol = 'X'

        else:
            print('Please choose either X or O')
            continue


        count = 0 
        occupied = set()                        # all occupied positions on the board
        comp_occupied = set()                   # occupied positions by computer/player2
        total_positions = {0,1,2,3,4,5,6,7,8}   # total positions available

        # winning positions for computer/player2 to choose from
        win_combo=[(0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,4,6),(2,5,8),(3,4,5),(6,7,8)]

        while count < 9:

            # get a position from the winning comninations
            for i in win_combo:
                if i[0] in comp_occupied and i[1] in comp_occupied and i[2] not in occupied:
                    index = i[2]
                    break
                elif i[0] in comp_occupied and i[2] in comp_occupied and i[1] not in occupied:
                    index = i[1]
                    break
                elif i[1] in comp_occupied and i[2] in comp_occupied and i[0] not in occupied:
                    index = i[0]
                    break

                else:
                    continue

            # get a random unoccupied position on the board
            else:
                remain = list(total_positions - occupied)
                random.shuffle(remain)
                index = remain[0]


            
            if index or index == 0:
                board[index] = computer_symbol
                count += 1
                occupied.add(index)
                comp_occupied.add(index)
                display_board(board)

                if won(board,computer_symbol):
                    print('You Lose!\n')
                    break

                elif count > 8:
                    print('Game Tied!\n')
                    break



            print('Your Turn!')
            move = int(input('Enter the position of your move: '))
            move = move - 1

            if board[move] == '_' or board[move] == ' ':
                board[move] = player_symbol
                count += 1
                occupied.add(move)
                display_board(board)

                if won(board,player_symbol):
                    print('Yay! You Won\n')
                    break

                elif count > 8:
                    print('Game Tied!\n')
                    break


            elif move in occupied:
                print(f'The position {move} is already filled\n')
                continue

            else:
                print('Please make an appropriate move.\n')
                continue

            
            print('Wait...\n')
            time.sleep(2)

    

        # asking player to play again
        choice = input('Do you want to play again?  Y/N: ')

        while choice.lower() not in ('y,yes,n,no'):
            print('Please give a valid answer.\n')
            choice = input('Do you want to play again?  Y/N: ')

        if choice.lower() == 'y' or choice.lower() == 'yes':
            continue

        elif choice.lower() == 'n' or choice.lower() == 'no':
            print('Good Bye!')
            break



# driver code
if __name__ == '__main__':
    play()

