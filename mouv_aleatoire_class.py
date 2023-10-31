import tkinter as tk
import random

class TamaGotshi:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("TamaGotshi")
        self.fenetre.geometry("1900x1000")

        self.canvas_width = 1900
        self.canvas_height = 1000

        self.can = tk.Canvas(self.fenetre, width=self.canvas_width, height=self.canvas_height, bg='black')
        self.can.pack()

        self.image = tk.PhotoImage(file="test.png")
        self.image_width = self.image.width()
        self.image_height = self.image.height()
        self.image_perso = self.can.create_image(250, 250, anchor=tk.NW, image=self.image)

        self.prev_x, self.prev_y = 250, 250
        self.img_prise = False

        self.can.bind("<Button-1>", self.canvas_clique)
        self.can.bind("<ButtonRelease-1>", self.canvas_relache)
        self.can.bind("<B1-Motion>", self.canvas_glisse)

        self.mouvement_alea()

    def mouvement_alea(self):
        if not self.img_prise:
            x, y = random.randint(0, self.canvas_width - self.image_width), random.randint(0, self.canvas_height - self.image_height)
            self.can.coords(self.image_perso, x, y)
        self.fenetre.after(60000, self.mouvement_alea)

    def canvas_clique(self, event):
        self.prev_x, self.prev_y = event.x, event.y
        self.img_prise = True

    def canvas_relache(self, event):
        self.img_prise = False

    def canvas_glisse(self, event):
        x, y = event.x, event.y
        self.can.move(self.image_perso, x - self.prev_x, y - self.prev_y)
        self.prev_x, self.prev_y = x, y

    def run(self):
        self.fenetre.mainloop()

if __name__ == "__main__":
    app = TamaGotshi()
    app.run()