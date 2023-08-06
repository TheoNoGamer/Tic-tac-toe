import PySimpleGUI as sg

button_size = (6, 3)

# Initialize the game board
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

layout = [
    [sg.Button('Reset')],
    [sg.Button(board[0][0], key='1a', size=button_size), sg.Button(board[0][1], key='1b', size=button_size),
     sg.Button(board[0][2], key='1c', size=button_size)],
    [sg.Button(board[1][0], key='2a', size=button_size), sg.Button(board[1][1], key='2b', size=button_size),
     sg.Button(board[1][2], key='2c', size=button_size)],
    [sg.Button(board[2][0], key='3a', size=button_size), sg.Button(board[2][1], key='3b', size=button_size),
     sg.Button(board[2][2], key='3c', size=button_size)]
]

window = sg.Window('Tic-Tac-Toe', layout)

def reset_board():
    global board
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    for i in range(3):
        for j in range(3):
            window[(i+1, j+1)].update(board[i][j])

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Reset':
        reset_board()
    else:
        row, col = int(event[0]), int(event[1])
        if board[row - 1][col - 1] == '':
            board[row - 1][col - 1] = ''
            window[event].update(board[row - 1][col - 1])

window.close()
