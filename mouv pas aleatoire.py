from tkinter import*
from random import randint
import tkinter as tk
import time
global image_perso


class Mouvement_alea(tk.Canvas):
    def __init__(self,*args, **kwargs):
        self.img=image_perso

    def bas(self):
        for i in range (3):
            can.move(self.img,0,50)

    def haut(self):
        for i in range (3):
            can.move(self.img,0,(-50))

    def gauche(self):
        for i in range (3):
            can.move(self.img,-25,0)

    def droite(self):
        for i in range (3):
            can.move(self.img,25,0)







def canvas_clique(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def canvas_glisse(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    can.move(image_perso, x - prev_x, y - prev_y)
    prev_x, prev_y = x, y

def canvas_bouge_alea() :
    tps_testeur=time.time()
    bouge=Mouvement_alea(can)
    if time.time()-tps_testeur >= 5.0:
        bouge.bas()
        can.after(800,canvas_bouge_alea())




fenetre=tk.Tk()           #crée la fenêtre appelée fenetre
fenetre.configure(bg="white")
fenetre.title("TamaGotsho") #Affiche le titre en haut de la fenêtre
fenetre.geometry("1300x800")  #redimensionner la fenêtre, l'unité est le pixel
can = Canvas(fenetre, width=1300, height=800, bg='black')


can.pack()


image = tk.PhotoImage(file="test.png")
# Afficher l'image sur le canvas
image_perso = can.create_image(250, 250, anchor=tk.NW, image=image)

# Lier des événements pour le déplacement de l'image
prev_x, prev_y = 250, 250
can.bind("<Button-1>", canvas_clique)
can.bind("<B1-Motion>", canvas_glisse)

bouge=Mouvement_alea(can)

yBouton=220
btnAjoute = tk.Button(fenetre, text="bouge", font=("tahoma Bold", 13), command=canvas_bouge_alea())
btnAjoute.place(x=100, y=yBouton)




fenetre.mainloop()
















