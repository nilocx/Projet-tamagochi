from tkinter import*
import random
from PIL import Image, ImageTk
from TAP import createPigeon, movePigeon, point, temps, TireAP
from subprocess import run


class TamaGotshi:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title("TamaGotshi")
        self.fenetre.geometry("1900x950")

        self.canvas_width = 1700
        self.canvas_height = 800

        self.can = Canvas(self.fenetre, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.can.pack()

        self.BoutonQuitter=Button(self.fenetre,text="Quitter",fg ="#660066", bg="black",height=4,width=25,command=self.fenetre.destroy)
        self.BoutonQuitter.pack(side=BOTTOM,padx=10,pady=10)

        self.BoutonMenu=Button(self.fenetre,text="Menu",fg ="#660066", bg="black",height=4,width=25,command=self.menu)
        self.BoutonMenu.pack(side=LEFT,padx=10,pady=10)

        self.image = PhotoImage(file="stickman_immobile.PNG")
        self.image_width = self.image.width()
        self.image_height = self.image.height()
        self.image_perso = self.can.create_image(250, 250, anchor=NW, image=self.image)

        self.prev_x, self.prev_y = 250, 250
        self.img_prise = False

        self.can.bind("<Button-1>", self.canvas_clique)
        self.can.bind("<ButtonRelease-1>", self.canvas_relache)
        self.can.bind("<B1-Motion>", self.canvas_glisse)

        self.mouvement_alea()




    def parametre(self):
        self.fenetre3 = Tk()
        self.fenetre3.title("paramètre")
        self.fenetre3.configure(bg = "#878c94")
        self.fenetre3.geometry("150x250")
        self.BoutonQuitter=Button(self.fenetre3,text="Quitter",fg ="#660066", bg="black",command=self.fenetre3.destroy)
        self.BoutonQuitter.pack(side=LEFT,padx=10,pady=10)
    def menu(self):
        self.fenetre2 = Tk()
        self.fenetre2.title("menu")
        self.fenetre2.configure(bg = "#878c94")
        self.fenetre2.geometry("164x245")
        self.fichierImage = PhotoImage(master=self.fenetre2, file = "bigoo.png")
        self.labelImageDeFond = Label(self.fenetre2, image=self.fichierImage)
        self.labelImageDeFond.place(x=0, y=0)
        self.BoutonQuitter=Button(self.fenetre2,text="Quitter",fg ="#660066", bg="black",height=1,width=5,command=self.fenetre2.destroy)
        self.BoutonQuitter.place(x=43, y=188)
        self.BoutonTAP=Button(self.fenetre2,text="TAP",fg ="#660066", bg="black",command=TireAP)
        self.BoutonTAP.place(x=72, y=110)
        self.Boutonparametre=Button(self.fenetre2,text="⚙",fg ="black", bg="#e29723",height=2,width=4,command=self.parametre)
        self.Boutonparametre.place(x=20, y=36)


    def mouvement_alea(self):
        liste = [60000,55000,50000,45000,40000,35000,30000,25000,20000,15000,10000,5000,1000,1000,1000,10000,50000,60000,25000]
        if not self.img_prise:
            x, y = random.randint(0, self.canvas_width - self.image_width), random.randint(0, self.canvas_height - self.image_height)
            self.can.coords(self.image_perso, x, y)
        self.fenetre.after(random.choice(liste), self.mouvement_alea)

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