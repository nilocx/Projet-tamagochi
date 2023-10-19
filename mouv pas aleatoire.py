from tkinter import*
import random
import tkinter as tk
import time
global image_perso
global img1,img2



class Mouvement_alea(tk.Canvas):
    def __init__(self,*args, **kwargs):
        self.img=image_perso
        self.tk=can

    def bas(self):
            self.move(self.img,0,25)

    def haut(self):
            self.move(self.img,0,(-25))

    def gauche(self):
            self.move(self.img,-25,0)

    def droite(self):
            self.move(self.img,25,0)




def alea(event):
    global prev_x, prev_y
    event.x=1
    event.y=0
    can.move(image_perso, event.x-prev_x, event.y-prev_y)
    fenetre.after(5000,alea)


def canvas_clique(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def canvas_glisse(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    can.move(image_perso, x - prev_x, y - prev_y)
    prev_x, prev_y = x, y

def bouffe():
    img1=tk.PhotoImage(file="banane.PNG")
    img2=tk.PhotoImage(file="banane.PNG")
    fenetre.after(5000,bouffe)




fenetre=tk.Tk()           #crée la fenêtre appelée fenetre
fenetre.configure(bg="white")
fenetre.title("TamaGotshi") #Affiche le titre en haut de la fenêtre
fenetre.geometry("1300x800")  #redimensionner la fenêtre, l'unité est le pixel
can = Canvas(fenetre, width=2000, height=1200, bg='black')
liste_bouffe=["banane.PNG","burger_apres_modif.PNG","wings_de_poulet.PNG","brocoli.PNG","past_que.PNG"]

can.pack()




image = tk.PhotoImage(file="test.png")
img1=tk.PhotoImage(file="banane.PNG")
img2=tk.PhotoImage(file="banane.PNG")
# Afficher l'image sur le canvas
image_perso = can.create_image(250, 250, anchor=tk.NW, image=image)
image_bouffe1 = can.create_image(600, 250, anchor=tk.NW, image=img1)
image_bouffe2 = can.create_image(500, 250, anchor=tk.NW, image=img2)

# Lier des événements pour le déplacement de l'image
prev_x, prev_y = 250, 250
can.bind("<Button-1>", canvas_clique)
can.bind("<ButtonRelease-1>", alea)
can.bind("<B1-Motion>", canvas_glisse)


bouge=Mouvement_alea(can)
bouffe()

fenetre.mainloop()
