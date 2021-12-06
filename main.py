from tkinter import *
from tkinter import Entry
import time


def char_check(var, index, mode):
    global count

    if string_var.get()[:len(string_var.get())] == quote_split[count][:len(string_var.get())]:
        correct_label.config(text="👍", pady=5)
        if string_var.get() == quote_split[count]:
            typing_entry.delete(0, END)
            correct_label.config(text="")
            count += 1
            count_label.config(text=f"Words: {count}")
            current_word_label.config(text=f"Current Word: {quote_split[count]}")
            if count == len(quote_split):
                final = secs
                label.destroy()
                count_label.config(text=f"You wrote {str(count/final)} word/second")
    else:
        correct_label.config(text="👎", pady=5)


def time_string():
    return time.strftime('%S')


def update():
    global secs
    secs += 1
    label.config(text=secs)
    label.after(1000, update)


global clock_label
global count

root = Tk()
root.title("Typing Speed Tester")

title_label = Label(text="Typing Speed tester")
title_label.grid(column=0, row=0)

practice_text = Text(root, height=20, width=40, wrap=WORD, padx=10, pady=10, font=("Courier", 30))
quote = "If we start our little script we get a very unsatisfying result We can see in the window only the first line of the monologue. Executing the above code will display an Entry widget that stores the input in a variable. The callback function will trace the updated value of the variable and display it in a Label widget. Now, type something in the given Entry widget. The label widget will mimic the input value and display the output on the window "

quote_split = quote.split()

practice_text.insert(END, quote)
practice_text.grid(column=0, row=1, padx=10, pady=10)

count = 0
current_word_label = Label(text=f"Current Word: {quote_split[count]}", font=("Courier", 20))
current_word_label.grid(column=0, row=2)

string_var = StringVar()
typing_entry: Entry = Entry(root, textvariable=string_var, font=("Courier", 20))
typing_entry.grid(column=0, row=3, padx=5)

string_var.trace("w", callback=char_check)

correct_label = Label(text="", font=("Courier", 30))
correct_label.grid(column=0, row=4)

count_label = Label(text=f"Words: {count}", font=("Courier", 30))
count_label.grid(column=0, row=5, pady=5)

global secs
secs = 0
label = Label(text=secs, font=("Courier", 30))
label.grid(column=0, row=6)
label.after(1000, update)

root.mainloop()
