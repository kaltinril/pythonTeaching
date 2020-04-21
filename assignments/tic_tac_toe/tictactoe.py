# We'll ignore spot 0 and waste the small bit of memory for that
# Create a list of 10 elements, 0 is going to be empty
# 1-9 are going to be the places, example below
# [X][O][ ]
# [O][X][ ]
# [ ][ ][X]
empty = ' '
board = [empty] * 11
valid_placement_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

player_score = [0, 0]
player_piece = ['X', 'O']
max_players = 2


def reset_board():
    return [empty] * 11


def draw_board():
    print('Player 1: ' + str(player_score[0]) + ' --- Player 2: ' + str(player_score[1]) + ' --- BEST OF: ' + str(best_of))
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def get_user_placement(turn):
    valid = False
    place = -1
    while not valid:
        place = input('Player ' + str(turn + 1) + ': select your spot.')

        if place in valid_placement_values:
            valid = True
        else:
            valid = False
            print('Invalid: Enter a number from 1-9 for the place!')

        if valid:
            place = int(place)
            if board[place] != empty:
                valid = False
                print('Invalid: Spot is already taken!')

    return place


def check_for_round_win(place):
    won = False

    # columns
    board[0] = board[9]  # Hack to fix column 3 (9, 6, 3) issue where mode 9 is 0
    if board[place] == board[(place + 3) % 9] == board[(place + 6) % 9] != empty:
        won = True

    # rows
    row_start = (int(((place - 1) / 3)) * 3) + 1
    if board[row_start] == board[row_start + 1] == board[row_start + 2] != empty:
        won = True

    # diagonal
    if board[7] == board[5] == board[3] != empty:
        won = True
    elif board[9] == board[5] == board[1] != empty:
        won = True

    return won


def assign_point(turn):
    player_score[whose_turn] += 1


def check_if_game_over():
    if (player_score[0] + player_score[1]) == best_of:
        return True
    else:
        return False


def pick_who_goes_first():
    valid = False
    goes_first = 1
    while not valid:
        goes_first = int(input('Who Goes First, 1 or 2? '))
        if goes_first in (1, 2):
            valid = True
        else:
            print('Invalid: Enter a number between 1 and ' + str(max_players))

    return goes_first - 1


def pick_player_pieces():
    valid = False
    p = 'X'
    while not valid:
        p = input('Player 1, X or O? ').upper().strip()
        if p not in player_piece:
            print('Invalid: Enter X or O!')
        else:
            valid = True

    if p == 'O':
        player_piece[0] = 'O'
        player_piece[1] = 'X'


def print_winner():
    if player_score[0] > player_score[1]:
        print('Player 1 WON !')
    else:
        print('Player 2 WON !')


def pick_rounds():
    valid = False
    how_many = 3
    while not valid:
        how_many = int(input('How many Rounds do you want to go? '))
        if (how_many % 2) == 1:
            valid = True

    return how_many


def is_tie_round():
    board[0] = ' '

    # Expected output in a tie is 9 characters of X and/or O.
    # Expected output otherwise is less than 9 characters
    # Spaces are stripped out by the mechanics of splitting and re-joining
    # Example of how this works:
    # [' ', 'O', 'X', ' ', 'X', 'O', 'X', 'O', ' ', 'O' ]       # board
    # ' OX XOXO O'                                              # .join
    # ['O', 'X', 'X', 'O', 'X', 'O', 'O' ]                      # .split
    # 'OXXOXOO'                                                 # .join
    # This causes all empty places to be removed, and we only get 1 character per placed X or O
    joined = "".join("".join(board).split())

    if len(joined) == 9:
        return True
    else:
        return False


pick_player_pieces()
whose_turn = pick_who_goes_first()
best_of = pick_rounds()
winner_found = False
while not winner_found:
    draw_board()

    # Ask user for their input and Validate input
    placement = get_user_placement(whose_turn)

    # Update Board
    board[placement] = player_piece[whose_turn]

    # Check for a win
    round_won = check_for_round_win(placement)

    # Give player who won a point
    if round_won:
        print('---------------------------------------')
        assign_point(whose_turn)
        draw_board()
        throw_away = input("Player " + str(whose_turn + 1) + ' won this round!  Press enter for next round!')
        print('---------------------------------------')
        board = reset_board()
    elif is_tie_round():
        print('---------------------------------------')
        draw_board()
        throw_away = input('Tie round!  Press key to try again!')
        print('---------------------------------------')
        board = reset_board()

    # Check if game over
    winner_found = check_if_game_over()

    # Change turns
    whose_turn = (whose_turn + 1) % 2

    # Pick who goes first now
    if round_won and not winner_found:
        whose_turn = pick_who_goes_first()
        round_won = False


print_winner()
