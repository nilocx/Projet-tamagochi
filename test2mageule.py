from tkinter import*
from test3magueuele import menu
from STAT_du_Perso_Tamagochie_cslg import*
from random import*
from PIL import Image, ImageTk


###fonctions
def on_canvas_click(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def on_canvas_drag(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    canvas.move(image_id, x - prev_x, y - prev_y)
    prev_x, prev_y = x, y


###fenetre 1(jeu)

# Créer la fenêtre tkinter
fenetre = Tk()
fenetre.title("TAMAGOTSHI") #Affiche le titre en haut de la fenêtre
fenetre.configure(bg = "#878c94")
fenetre.geometry("1300x800")  #redimensionner la fenêtre, l'unité est le pixel



#Création d'un bouton Quitter
BoutonQuitter=Button(fenetre,text="Quitter",fg ="#660066", bg="black",command=fenetre.destroy)
BoutonQuitter.pack(side=LEFT,padx=10,pady=10)

#Création d'un bouton Menu
BoutonMenu=Button(fenetre,text="Menu",fg ="#660066", bg="black",command=menu)
BoutonMenu.pack(side=LEFT,padx=10,pady=10)



# Charger l'image
image = PhotoImage(file="test.png")  # Assurez-vous de remplacer "votre_image.gif" par le chemin de votre image

# Créer un canvas
canvas = Canvas(fenetre, width=1250, height=870,background='white')
canvas.pack()

# Afficher l'image sur le canvas
image_id = canvas.create_image(0, 0, anchor=NW, image=image)

# Lier des événements pour le déplacement de l'image
prev_x, prev_y = 50, 50
canvas.bind("<Button-1>", on_canvas_click)
canvas.bind("<B1-Motion>", on_canvas_drag)



# Lancer la boucle principale de la fenêtre tkinter
fenetre.mainloop()