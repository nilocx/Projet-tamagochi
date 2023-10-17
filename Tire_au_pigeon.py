from random import*
from STAT_du_Perso_Tamagochie_cslg import*
from tkinter import*
from PIL import Image, ImageTk
"""
def createPigeon():
    x_position = randint(100,200)
    y_position = randint(100,200)
    pigeon = ImageTk.PhotoImage(Image.open("pigeon.gif"))
    my_photo = cvn.create_image(x_position, y_position, image = pigeon, anchor = 's')
    fenetreTireauPigeon.after(3000,createPigeon)
    print("teste")

# def movePigeon(x,y):
#     cvn.move(x,y)
#     fenetreTireauPigeon.after(10, movePigeon)


#creation de la fenetre
fenetreTireauPigeon=Tk()
fenetreTireauPigeon.title("Tire Au Pigeon")
fenetreTireauPigeon.geometry("768x492")

fond = Image.open("saiboubakar.png")
photo = ImageTk.PhotoImage(fond)

# #image de fond
# load = Image.open("fond.png")
# render = ImageTk.PhotoImage(load)
# load = Image.open("fond.png")
# render = ImageTk.PhotoImage(load)
# img = Label(fenetreTireauPigeon, image=render)
# img.image = render
# img.place(x=-1, y=0)

cvn=Canvas(fenetreTireauPigeon, width=768,height=492)
# cvn.create_image(0,0, image=photo, anchor="nw")
# cvn.pack()

#Boutton de destruction TEMPORAIre
destruction=Button(fenetreTireauPigeon,text="DESTRUCTION",command=fenetreTireauPigeon.destroy)
destruction.pack()
destruction_w=cvn.create_window(200, 200, window=destruction)
teste=Button(fenetreTireauPigeon,text="test",command=createPigeon())
teste.pack()
teste_w=cvn.create_window(100,100,window=teste)

fruits_list = []

# movePigeon(5,2)

fenetreTireauPigeon.mainloop()"""
class fenetres():
    def __init__(self):
        self.f = Tk()
        champ_label = Label(self.f, text="Salut !")
        champ_label.pack()
        bouton = Button(self.f,text="Acceuil", command=self.test)
        bouton.pack()
        self.f.mainloop()
    def acceuil(self):
        self.f2 = Tk()
        c_l = Label(self.f2, text="ACCEUILL")
        c_l.pack()
        self.f2.mainloop()
    def test(self):
        self.f.destroy()
        self.acceuil()

sart = fenetres()