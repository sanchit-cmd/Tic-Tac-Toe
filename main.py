positions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
current_player = 'X'
run = True


def display(position):
    print(f"""
    {position[0]} | {position[1]} | {position[2]}
    {position[3]} | {position[4]} | {position[5]}
    {position[6]} | {position[7]} | {position[8]}
    """)


def user_input():
    choice = ''
    while choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        choice = int(input('Enter a position(1-9): '))
    return choice - 1


def change_player(current_player):
    return 'X' if current_player == 'O' else 'O'


def replace(positions, current_player, user_input):
    if positions[user_input] == ' ':
        positions[user_input] = current_player
    else:
        print('Invalid Move')


def check_winner(positions, current_player):
    global run
    if positions[0] == positions[1] == positions[2] != ' ':
        print(current_player, 'wins!')
        run = False
    if positions[3] == positions[4] == positions[5] != ' ':
        print(current_player, 'wins!')
        run = False
    if positions[6] == positions[7] == positions[8] != ' ':
        print(current_player, 'wins!')
        run = False
    if positions[0] == positions[3] == positions[6] != ' ':
        print(current_player, 'wins!')
        run = False
    if positions[1] == positions[4] == positions[7] != ' ':
        print(current_player, 'wins!')
        run = False
    if positions[2] == positions[5] == positions[8] != ' ':
        print(current_player, 'wins!')
        run = False
    if positions[0] == positions[4] == positions[8] != ' ':
        print(current_player, 'wins!')
        run = False
    if positions[2] == positions[4] == positions[6] != ' ':
        print(current_player, 'wins!')
        run = False
    if ' ' not in positions:
        print('Tie!')
        run = False


display([1, 2, 3, 4, 5, 6, 7, 8, 9])
display(positions)

while run:
    choice = user_input()
    replace(positions, current_player, choice)
    display(positions)
    check_winner(positions, current_player)
    current_player = change_player(current_player)
