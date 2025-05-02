from tkinter import *
import random
import config

def buttonClick(button):
    current_color = button.cget("bg")
    if current_color == config.buttoncolourmarked:
        button.config(bg=config.buttoncolourdefault)
    else:
        button.config(bg=config.buttoncolourmarked)

Fenster = Tk()
Fenster.title("Bingo-Tool")
Fenster.geometry(config.windowgeometry)
Fenster.iconbitmap("favicon.ico")


Anzeige = Label(Fenster, text="Wir spielen BINGO!")
Anzeige.place(relx=0.5, anchor="n")

Rahmen = Frame(Fenster)
Rahmen.place(relx=0.5, rely=0.5, anchor="center")

Buttons = []
index = 0
for i in range(5):
    for j in range(5):
        Buttons.append(Button(Rahmen, width=12, height=6, bg=config.buttoncolourdefault))
        Buttons[index].config(command=lambda b=Buttons[index]: buttonClick(b))
        Buttons[index].grid(row=i, column=j, padx=5, pady=5)
        index+=1
        
with open("bingosätze.txt", "r", encoding="utf-8") as file:
    saetze = [line.strip().replace("\t", "\n") for line in file]
    
random.shuffle(saetze)
    
for i in range(25):
    Buttons[i].config(text=saetze[i], wraplength=125, justify="center", font=(config.textfont, config.textsize))
    
Fenster.mainloop()