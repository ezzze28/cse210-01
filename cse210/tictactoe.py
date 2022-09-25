"""
w02 Prove Assignment - Tic-Tac-Toe
CSE 210
Ezequiel Nicolidakis
"""

def main():
    print("\n-----Welcome to Tic-Tac-Toe-----\n\nPlease choose an option\n")    
    print("1- New game\n2- Game rules\n0- Quit\n")
    switch = input()
    while switch!="1" and switch!="2" and switch!="0":
        switch = input("\nPlease select a valid option ")
    while switch!="0":
        if switch == "1":
                players = next_player("")
                playground = new_board()
                new_game(playground, players)
        elif switch == "2":
            print("\n-----Rules----\n")
            print("The object of Tic Tac Toe is to get three in a row. \nYou play on a three by three game board. \nThe first player is known as X and the second is O. \nPlayers alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled. \nX always goes first, and in the event that no one has three in a row, the stalemate is called a cat game.")
        print("\n1- New game\n2- Game rules\n0- Quit\n")
        switch = input()
    print("See you soon!")

def new_game(board, player):
    while not (win(board) or draw(board)):
        print_board(board)
        make_move(player, board)
        player = next_player(player)
        print_board(board)
    if win(board):
        player = next_player(player)
        print(f"{player} Wins")
    elif draw(board):
        print("The match ends in a draw!!!")
    print("Good game. Thanks for playing!") 


def new_board():
    board = []
    for i in range(9):
        board.append(i + 1)
    return board

def print_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-----')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-----')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def draw(board):
    for i in range(9):
        if board[i] != "x" and board[i] != "o":
            return False
    return True 
    
def win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

main()