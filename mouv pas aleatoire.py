from tkinter import*
from random import randrange
import tkinter as tk


def on_can_click(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def on_can_drag(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    can.move(image_id, x - prev_x, y - prev_y)
    prev_x, prev_y = x, y



fenetre=Tk()           #crée la fenêtre appelée fenetre
fenetre.configure(bg="white")
fenetre.title("LE PENDU") #Affiche le titre en haut de la fenêtre
fenetre.geometry("1300x800")  #redimensionner la fenêtre, l'unité est le pixel
can = Canvas(fenetre, width=1300, height=800, bg='black')

can.pack()

image = tk.PhotoImage(file="test.png")
# Afficher l'image sur le canvas
image_id = can.create_image(0, 0, anchor=tk.NW, image=image)

# Lier des événements pour le déplacement de l'image
prev_x, prev_y = 0, 0
can.bind("<Button-1>", on_can_click)
can.bind("<B1-Motion>", on_can_drag)



fenetre.mainloop()


