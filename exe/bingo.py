from tkinter import *
import random

def buttonClick(button):
    current_color = button.cget("bg")
    if current_color == "red":
        button.config(bg="white")  # Zurück auf weiß
    else:
        button.config(bg="red")  # Auf grün setzen

Fenster = Tk()
Fenster.title("Bingo")
Fenster.geometry("860x860")
#Fenster.resizable("false", "false")

Anzeige = Label(Fenster, text="Wir spielen BINGO!")
Anzeige.pack()

Buttons = []
k = 0
for i in range(5):
    for j in range(5):
        Buttons.append(Button(Fenster, text=str(k)+"LOL"))
        Buttons[k].place(x = 160 * j + 30, y = 160 * i + 30, width=150, height=150)
        Buttons[k].config(command=lambda b=Buttons[k]: buttonClick(b))
        k+=1
        
with open("bingosätze.txt", "r", encoding="utf-8") as file:
    saetze = [line.strip().replace("\t", "\n") for line in file]
    
random.shuffle(saetze)
    
for i in range(25):
    Buttons[i].config(text=saetze[i], wraplength=150, justify="left", font=("Arial", 14))
    
Fenster.mainloop()