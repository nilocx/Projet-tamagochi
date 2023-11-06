import tkinter as tk
import random

# Fonction pour déplacer l'image de manière aléatoire
def mouvement_alea():
    if not img_prise:  # Vérifier si l'image est tenue par le joueur
        x, y = random.randint(0, canvas_width - image_width), random.randint(0, canvas_height - image_height)
        can.coords(image_perso, x, y)  # Déplacer l'image à de nouvelles coordonnées aléatoires
    fenetre.after(60000, mouvement_alea)  # Appeler mouvement_alea toutes les minutes

# Fonction appelée lorsqu'un clic de souris est détecté sur le canvas
def canvas_clique(event):
    global prev_x, prev_y, img_prise
    prev_x, prev_y = event.x, event.y
    img_prise = True

# Fonction appelée lorsque le bouton de la souris est relâché
def canvas_relache(event):
    global img_prise
    img_prise = False

# Fonction appelée lorsqu'un glissement de souris est détecté sur le canvas
def canvas_glisse(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    can.move(image_perso, x - prev_x, y - prev_y)  # Déplacer l'image en fonction du glissement de souris
    prev_x, prev_y = x, y

# Initialisation de la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("TamaGotshi")
fenetre.geometry("1900x1000")

canvas_width = 1900
canvas_height = 1000

# Création d'un canvas pour afficher l'image
can = tk.Canvas(fenetre, width=canvas_width, height=canvas_height, bg='black')
can.pack()

# Chargement de l'image à afficher sur le canvas
image = tk.PhotoImage(file="test.png")
image_width = image.width()
image_height = image.height()
image_perso = can.create_image(250, 250, anchor=tk.NW, image=image)

prev_x, prev_y = 250, 250
img_prise = False  # Variable pour indiquer si l'image est tenue

# appelle la fonction correspondante au action fait par le joueur avec la souris
can.bind("<Button-1>", canvas_clique)
can.bind("<ButtonRelease-1>", canvas_relache)
can.bind("<B1-Motion>", canvas_glisse)

mouvement_alea()  # Appelle la fonction de mouvement aléatoire dès le lancement du jeu

fenetre.mainloop()

