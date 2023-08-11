import random
from tkinter import *
import pandas as pd

to_learn = {}
current_word = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/kannada_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def show_new():
    global current_word
    global flip_time
    window.after_cancel(flip_time)
    current_word = random.choice(to_learn)
    word = current_word["Kannada"]
    my_canvas.itemconfig(card_title, text="Kannada")
    my_canvas.itemconfig(card_word, text=word)
    flip_time = window.after(5000, func=flip_card)


def flip_card():
    my_canvas.itemconfig(card_title, text="English")
    my_canvas.itemconfig(card_word, text=current_word["English"])


def i_know():
    to_learn.remove(current_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    show_new()


window = Tk()
window.title("Learn English For Kannada Talking People")
window.config(padx=50, pady=50, background="#B1DDC6")
flip_time = window.after(3000, func=flip_card)

my_canvas = Canvas(height=526, width=800, bg="white")
card_title = my_canvas.create_text(400, 150, text="Kannada", font=("Arial", 40, 'italic'))
card_word = my_canvas.create_text(400, 253, text="Learn English", font=("Arial", 60, 'bold'))

tick_image = PhotoImage(file="image/right.png")
cross_image = PhotoImage(file="./image/wrong.png")

tick_button = Button(image=tick_image, highlightthickness=0, command=i_know)
cross_button = Button(image=cross_image, highlightthickness=0, command=show_new)

my_canvas.grid(row=0, column=0, columnspan=2)
tick_button.grid(row=1, column=0)
cross_button.grid(row=1, column=1)

show_new()

window.mainloop()