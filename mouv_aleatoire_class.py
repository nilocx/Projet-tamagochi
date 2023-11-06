import tkinter as tk
import random

class TamaGotshi:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("TamaGotshi")
        self.fenetre.geometry("1900x1000")

        self.canvas_width = 1900
        self.canvas_height = 1000

        # Création d'un canvas pour afficher l'image
        self.can = tk.Canvas(self.fenetre, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.can.pack()

        # Chargement de l'image du lit à afficher sur le canvas
        self.img_lit = tk.PhotoImage(file="lit_vide.png")
        self.image_lit = self.can.create_image(0,0,anchor=tk.NW, image=self.img_lit)


        # Chargement de l'image du personnage à afficher sur le canvas
        self.image = tk.PhotoImage(file="test.png")
        self.image_width = self.image.width()
        self.image_height = self.image.height()
        self.image_perso = self.can.create_image(250, 250, anchor=tk.NW, image=self.image)


        self.prev_x, self.prev_y = 250, 250
        self.img_prise = False # Variable pour indiquer si l'image est tenue

        # appelle la fonction correspondante au action fait par le joueur avec la souris
        self.can.bind("<Button-1>", self.canvas_clique)
        self.can.bind("<ButtonRelease-1>", self.canvas_relache)
        self.can.bind("<B1-Motion>", self.canvas_glisse)

        self.mouvement_alea() # Appelle la fonction de mouvement aléatoire dès le lancement du jeu

    def mouvement_alea(self): # Fonction pour déplacer l'image de manière aléatoire
        if not self.img_prise: # Vérifier si l'image est tenue par le joueur
            x, y = random.randint(0, self.canvas_width - self.image_width), random.randint(0, self.canvas_height - self.image_height)
            self.can.coords(self.image_perso, x, y)  # Déplacer l'image à de nouvelles coordonnées aléatoires
        self.fenetre.after(60000, self.mouvement_alea)

    def canvas_clique(self, event):  # Fonction appelée lorsqu'un clic de souris est détecté sur le canvas
        self.prev_x, self.prev_y = event.x, event.y
        self.img_prise = True

    def canvas_relache(self, event):  # Fonction appelée lorsque le bouton de la souris est relâché
        self.img_prise = False

    def canvas_glisse(self, event): # Fonction appelée lorsqu'un glissement de souris est détecté sur le canvas
        x, y = event.x, event.y
        self.can.move(self.image_perso, x - self.prev_x, y - self.prev_y)
        self.prev_x, self.prev_y = x, y

    def run(self):
        self.fenetre.mainloop()

if __name__ == "__main__":
    app = TamaGotshi()
    app.run()
