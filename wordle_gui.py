import tkinter as tk
import random
from word_list import word_list 
from tkinter import messagebox

target_word = random.choice(word_list)
max_attempts = 6
attempts = 0
game_over = False
play_again_button = None

root = tk.Tk()
root.title('Wordle')
root.geometry('400x500')
root.config(bg ="#f3c0d9")

title = tk.Label(root, text = 'WORDLE', font = ('Lucida Handwriting', 20,'bold'), bg = "#f3c0d9" )
title.pack(pady = (10,0))

label = tk.Label(root, text = 'Enter your 5 letter guess', font = ('Bradley Hand', 14), bg = '#f3c0d9')
label.pack(pady = (20,10))

entry = tk.Entry(root , font = ('Kristen ITC', 16), justify= 'center', width= 10, bg = '#f3c0d9', fg ='#6b1839', relief = 'ridge', bd =2, insertbackground= '#6b1839' )
entry.pack(pady = 5)
entry.bind('<Return>', lambda event: check_guess())

canvas_frame = tk.Frame(root)
canvas_frame.pack(pady = 10, fill = 'both', expand = True)

canvas = tk.Canvas(canvas_frame, bg = '#f3c0d9',highlightthickness=0, bd = 0 )
scrollbar = tk.Scrollbar(canvas_frame, orient = 'vertical', command = canvas.yview)
scrollable_frame = tk.Frame(canvas, bg = '#f3c0d9')

scrollable_frame.bind(
    '<Configure>', lambda e: canvas.configure(scrollregion= canvas.bbox('all'))
)

canvas.create_window((0,0), window = scrollable_frame, anchor = 'nw')
canvas.configure(yscrollcommand = scrollbar.set)

canvas.pack( side = 'left', fill = 'both', expand = 'true')
scrollbar.pack(side = 'right', fill = 'y')


def check_guess():
    global attempts, game_over

    if game_over:
        return


    guess= entry.get().lower()
    
    if len(guess) != 5:
        messagebox.showerror('Invalid Guess', 'Your word must be exactly 5 letters')
        return
    
    if guess not in word_list:
        messagebox.showwarning('Invalid Word', 'That word is not in the list!')
        return
    
   

    feedback = ['']*5
    target_copy = list(target_word)

    for i in range(5):
        if guess[i] == target_word[i]:
            feedback[i] = '#ff66a3'
            target_copy[i] = None

    for i in range(5):
        if feedback[i] =='':
            if guess[i] in target_copy:
                feedback[i] = "#f07c0f"
                target_copy[target_copy.index(guess[i])] = None
            else:
                feedback[i] = "#55f1c0"

    row = tk.Frame(scrollable_frame, bg="#ffeaf4")
    row.pack(pady=5)

    
    tk.Frame(row, bg="#ffeaf4").pack(side="left", expand=True)

    for i in range(5):
        letter = guess[i].upper()
        color = feedback[i]
        tk.Label(
            row,
            text=letter,
            width=4,
            height=2,
            font=("Kristen ITC", 16),
            bg=color,
            fg="white"
        ).pack(side="left", padx=2)

    tk.Frame(row, bg="#ffeaf4").pack(side="left", expand=True)

    if guess == target_word:
        win_label = tk.Label(scrollable_frame, text = 'You guessed the word!', fg = 'green', font = ('Kristen ITC', 12))
        win_label.pack()
        entry.config(state = 'disabled')
        game_over = True
        show_play_again()

    else:
        attempts+=1

        if attempts >= max_attempts:
            game_over_label = tk.Label(scrollable_frame, text = f'Game Over! The word was :{target_word.upper()}', fg = 'black')
            game_over_label.pack()
            entry.config(state = 'disabled')
            game_over = True
            show_play_again()

        else:
            result = tk.Label(scrollable_frame,text=f'Attempt {attempts} of {max_attempts}', font= ('Kristen ITC', 14))
            result.pack()
    
    entry.delete(0, tk.END)
    
def show_play_again():
        global play_again_button
        play_again_button = tk.Button(root, text = 'Play Again', font = ('Kristen ITC', 12, 'bold'), bg ="#4a90e2",fg = '#f3c0d9', padx =10, pady =5, relief = 'raised', command = reset_game)
        play_again_button.pack(pady = 10)

def reset_game():
    global target_word, attempts, game_over,play_again_button

    target_word = random.choice(word_list)
    attempts = 0
    game_over =False

    entry.config(state = 'normal')
    entry.delete(0, tk.END)

    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    if play_again_button:
        play_again_button.destroy()

button = tk.Button(root, text = 'Submit', bg= '#ff4d88', command= check_guess)
button.pack(pady = 10)

root.mainloop() 
