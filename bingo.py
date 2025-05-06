from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import random
import yaml

Buttons = []                        #Feld für Buttons
with open("config.yaml", "r") as f: #config datei laden
    config = yaml.load(f, Loader=yaml.FullLoader)

def buttonClick(button):
    current_color = button.cget("bg")
    if current_color == config["button"]["colourmarked"]:
        button.config(bg=config["button"]["colourdefault"])
    else:
        button.config(bg=config["button"]["colourmarked"])

def openFile():
    datei = filedialog.askopenfilename(filetypes=(("Textdateien","*txt" ), ("Alle Dateien",".")))
    buttonwrite(open(datei, "r", encoding="utf-8"))
    
def buttonplace():
    index = 0
    for i in range(5):
        for j in range(5):
            Buttons.append(Button(Rahmen, width=12, height=6, bg=config["button"]["colourdefault"]))
            Buttons[index].config(command=lambda b=Buttons[index]: buttonClick(b))
            Buttons[index].grid(row=i, column=j, padx=5, pady=5)
            index+=1
        
def buttonwrite(fileeingabe):
    with fileeingabe as file:
        saetze = [line.strip().replace("\t", "\n") for line in file]
    
    random.shuffle(saetze)
    
    for i in range(25):
        Buttons[i].config(text=saetze[i], wraplength=125, justify="center", font=(config["text"]["textfont"], config["text"]["textsize"]))
    
def buttonreset():
    for i in range(25):
        Buttons[i].config(bg=config["button"]["colourdefault"])        
    buttonwrite(open("bingosätze.txt", "r", encoding="utf-8"))

def buttoncolour(background, text, acbackground, acforeground):
    for i in range(25):
        Buttons[i].config(bg=background,fg=text,activebackground=acbackground,activeforeground=acforeground)

def settings():
    # Neues Einstellungsfenster (Toplevel)
    einstellungsfenster = Toplevel()
    einstellungsfenster.title("Einstellungen")
    einstellungsfenster.geometry("300x250")
    einstellungsfenster.iconbitmap("favicon.ico")

    # Eingabefeld: Benutzername
    #Label(einstellungsfenster, text="Benutzername:").pack(pady=(10, 0))
    #eintrag_name = Entry(einstellungsfenster)
    #eintrag_name.pack(pady=5)

    #Checkbox: Dark Mode
    dark_mode_var = BooleanVar()
    dark_mode_var.set(config["window"]["darkmode"])
    Checkbutton(einstellungsfenster, text="Dark Mode", variable=dark_mode_var).pack(pady=5)

    # Dropdown: Farbe
    #Label(einstellungsfenster, text="Sprache wählen:").pack(pady=(10, 0))
    #auswahl = StringVar()
    #auswahl.set(sprachen[0])  # Standardwert
    #OptionMenu(einstellungsfenster, auswahl, *sprachen).pack(pady=5)

    # Speichern-Button
    def speichern():
        #name = eintrag_name.get()
        config["window"]["darkmode"] = dark_mode_var.get()
        #sprache = auswahl.get()
        #print(f"Name: {name}, Dark Mode: {dark}, Sprache: {sprache}")
        with open("config.yaml", "w") as f:
            yaml.safe_dump(config, f)
        einstellungsfenster.destroy()
        update()        

    Button(einstellungsfenster, text="Speichern", command=speichern).pack(pady=10)

def update():
    if(config["window"]["darkmode"] == True):
        config["button"]["colourdefault"] = "#555555"
        config["button"]["colourmarked"] = "#3c5e00"
        config["button"]["colourtext"] = "white"
        buttoncolour(config["button"]["colourdefault"], config["button"]["colourtext"], config["button"]["colourdefault"], "white")
        Fenster.config(background="#2e2e2e")
        Rahmen.config(background="#2e2e2e")   
        
    else:
        config["button"]["colourdefault"] = "SystemButtonFace"
        config["button"]["colourmarked"] = "red"
        config["button"]["colourtext"] = "black"
        buttoncolour(config["button"]["colourdefault"], config["button"]["colourtext"], config["button"]["colourdefault"], "black")
        Fenster.config(bg="SystemButtonFace")
        Rahmen.config(bg="SystemButtonFace")
    with open("config.yaml", "w") as f:
            yaml.safe_dump(config, f)
    
Fenster = Tk()
Fenster.title("Bingo-Tool")
Fenster.geometry(config["window"]["windowgeometry"])
Fenster.iconbitmap("favicon.ico")

Rahmen = Frame(Fenster)
Rahmen.place(relx=0.5, rely=0.5, anchor="center")
    
Menueleiste = Menu(Fenster)
Fenster.config(menu=Menueleiste)

Dateimenu = Menu(Menueleiste, tearoff=0)
Menueleiste.add_cascade(label="Neu", menu=Dateimenu)
Dateimenu.add_command(label="Öffnen", command=openFile)
Dateimenu.add_command(label="Reset", command=buttonreset)

Menueleiste.add_cascade(label="Einstellungen", command=settings)

buttonplace()
buttonwrite(open("bingosätze.txt", "r", encoding="utf-8"))
update()

Fenster.mainloop()