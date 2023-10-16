from tkinter import*
from random import randint
import tkinter as tk


def canvas_clique(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def canvas_glisse(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    can.move(image_perso, x - prev_x, y - prev_y)
    prev_x, prev_y = x, y

def canvas_bouge_alea() :
    for i in range (0,25):
        can.move(image_perso,randint(5,10),randint(5,10))






fenetre=Tk()           #crée la fenêtre appelée fenetre
fenetre.configure(bg="white")
fenetre.title("TamaGotsho") #Affiche le titre en haut de la fenêtre
fenetre.geometry("1300x800")  #redimensionner la fenêtre, l'unité est le pixel
can = Canvas(fenetre, width=1300, height=800, bg='black')

can.pack()

image = tk.PhotoImage(file="test.png")
# Afficher l'image sur le canvas
image_perso = can.create_image(0, 0, anchor=tk.NW, image=image)

# Lier des événements pour le déplacement de l'image
prev_x, prev_y = 0, 0
can.bind("<Button-1>", canvas_clique)
can.bind("<B1-Motion>", canvas_glisse)

yBouton=220
btnAjoute = tk.Button(fenetre, text="bouge", font=("tahoma Bold", 13), command=canvas_bouge_alea())
btnAjoute.place(x=100, y=yBouton)


fenetre.mainloop()
















