import math
import random
import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound  # Only works on Windows. Use pygame for cross-platform.

# Game state
board = [' ' for _ in range(9)]
difficulty = 'hard'  # Default difficulty
current_player = 'X'
buttons = []
timer_label = None
timer_running = False
start_time = 0

# Check for a winner
def check_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(brd[i] == player for i in condition):
            return True
    return False

def is_tie(brd):
    return ' ' not in brd

def minimax(brd, depth, is_maximizing, alpha, beta, max_depth=None):
    if check_winner(brd, 'O'):
        return 1
    elif check_winner(brd, 'X'):
        return -1
    elif is_tie(brd) or (max_depth is not None and depth == max_depth):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                eval = minimax(brd, depth + 1, False, alpha, beta, max_depth)
                brd[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                eval = minimax(brd, depth + 1, True, alpha, beta, max_depth)
                brd[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def play_sound():
    try:
        winsound.Beep(1000, 150)  # Frequency, Duration in ms
    except:
        pass  # On non-Windows systems, winsound will fail

def ai_move():
    global board
    if difficulty == 'easy':
        move = random.choice([i for i in range(9) if board[i] == ' '])
    elif difficulty == 'medium':
        move = None
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, 0, False, -math.inf, math.inf, max_depth=2)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
    else:
        move = None
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
    board[move] = 'O'
    buttons[move].config(text='O', state='disabled')
    play_sound()
    if check_winner(board, 'O'):
        messagebox.showinfo("Game Over", "AI wins!")
        reset_board()
    elif is_tie(board):
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_board()

def on_click(index):
    global board
    if board[index] == ' ':
        board[index] = 'X'
        buttons[index].config(text='X', state='disabled')
        play_sound()
        if check_winner(board, 'X'):
            messagebox.showinfo("Game Over", "You win!")
            reset_board()
        elif is_tie(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()
        else:
            ai_move()

def reset_board():
    global board, start_time
    board = [' ' for _ in range(9)]
    for btn in buttons:
        btn.config(text=' ', state='normal')
    start_time = time.time()

def set_difficulty(diff):
    global difficulty
    difficulty = diff
    reset_board()

def update_timer():
    global timer_running
    if timer_running:
        elapsed = int(time.time() - start_time)
        timer_label.config(text=f"Time: {elapsed}s")
        root.after(1000, update_timer)

# GUI setup
root = tk.Tk()
root.title("Tic-Tac-Toe AI")

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text=' ', font=('Arial', 24), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

diff_frame = tk.Frame(root)
diff_frame.pack(pady=10)

for diff in ['easy', 'medium', 'hard']:
    tk.Button(diff_frame, text=diff.capitalize(), command=lambda d=diff: set_difficulty(d)).pack(side='left', padx=5)

timer_label = tk.Label(root, text="Time: 0s", font=("Arial", 14))
timer_label.pack(pady=10)
timer_running = True
start_time = time.time()
update_timer()

root.mainloop()
