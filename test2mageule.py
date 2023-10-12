import tkinter as tk

def on_canvas_click(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def on_canvas_drag(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    canvas.move(image_id, x - prev_x, y - prev_y)
    prev_x, prev_y = x, y

# Créer la fenêtre tkinter
root = tk.Tk()
root.title("Déplacer une image")

# Charger l'image
image = tk.PhotoImage(file="jsp.jpg")  # Assurez-vous de remplacer "votre_image.gif" par le chemin de votre image

# Créer un canvas
canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.pack()

# Afficher l'image sur le canvas
image_id = canvas.create_image(0, 0, anchor=tk.NW, image=image)

# Lier des événements pour le déplacement de l'image
prev_x, prev_y = 0, 0
canvas.bind("<Button-1>", on_canvas_click)
canvas.bind("<B1-Motion>", on_canvas_drag)

# Lancer la boucle principale de la fenêtre tkinter
root.mainloop()