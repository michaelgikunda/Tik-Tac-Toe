# Packages Used
from customtkinter import *
import customtkinter
import random
import pygame.mixer as mixer


# Window Attributes
root = customtkinter.CTk()
root.geometry("500x400")
root.resizable(width=False, height=False)
root.config(bg="black")
root.title("Tik Tac Toe")
root.iconbitmap("images/icons.ico")
#root.attributes("-alpha", 0.99)

# Functions

def minimax(board, depth, isMaximizing):
    result = check_winner(board)
    if result is not None:
        return result

    if isMaximizing:
        bestScore = -float("inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = ""
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float("inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = ""
                bestScore = min(score, bestScore)
        return bestScore



moves = {}

def main(value):
    buttons[value].configure(text="X")
    moves[value] = 'X'
    play_sound("M")
    check_winner()
    empty_buttons = [i for i in range(9) if i not in moves]
    if empty_buttons:
        next_move = random.choice(empty_buttons)
        buttons[next_move].configure(text="O")
        moves[next_move] = 'O'
        play_sound("P")
        check_winner()
    
    player = None
    if player == "X":
        buttons[value].configure(text="X")
        moves[value] = "X"
        player = "O"
        check_winner()
        if len(moves) < 9:
            bestMove = -1
            bestScore = -float("inf")
            for i in range(len(buttons)):
                if moves.get(i) is None:
                    moves[i] = "O"
                    score = minimax(list(moves.values()), 0, False)
                    moves.pop(i)
                    if score > bestScore:
                        bestScore = score
                        bestMove = i
            moves[bestMove] = "O"
            buttons[bestMove].configure(text="O")
            check_winner()

        
mixer.init()
success_sound = mixer.Sound("sound/sucess.mp3")
lost_sound = mixer.Sound("sound/lost.mp3")
move_sound = mixer.Sound("sound/slide.mp3")

def play_sound(value):
    if value == "X":
        success_sound.play()
    elif value == "O":
        lost_sound.play()
    elif value == "M":
        move_sound.play()






def computer_move():
    
    empty_cells = [i for i in range(9) if buttons[i]["text"] == ""]
    if empty_cells:
        chosen_cell = random.choice(empty_cells)
        buttons[chosen_cell].configure(text="O")
        check_winner()
    player = "X"

def reset_board():
    for button in buttons:
        button.configure(text="")
    moves.clear()

def check_winner():
    winning_combinations = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for a, b, c in winning_combinations:
        if a in moves and b in moves and c in moves and moves[a] == moves[b] == moves[c]:
            label.configure(text=f"{moves[a]} wins!")
            play_sound(moves[a])
            reset_board()
            return
        if len(moves) == 9:
            label.configure(text="It's a tie!")
            reset_board()
            return




def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

# -------------- #

# Window Components

label = CTkLabel(root, text="Tik Tac Toe", font=("Bahnschrift", 12), bg_color="black", text_color="white")
label.pack(pady=5)

# Window Components
player = "X"
buttons = []
for i in range(0, 9):
    button = CTkButton(root, text="", font=("Baloo", 60), width=129, height=102, fg_color="#101010", bg_color="#101010", command=lambda v=i: main(v))
    button.configure(cursor="x_cursor")
    buttons.append(button)

buttons[0].place(x=57, y=63)
buttons[1].place(x=186, y=63)
buttons[2].place(x=315, y=63)
buttons[3].place(x=57, y=165)
buttons[4].place(x=186, y=165)
buttons[5].place(x=315, y=165)
buttons[6].place(x=57, y=267)
buttons[7].place(x=186, y=267)
buttons[8].place(x=315, y=267)

root.mainloop()
