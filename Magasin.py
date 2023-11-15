from tkinter import*
from PIL import Image, ImageTk
from STAT_du_Perso_Tamagochie_cslg import*
from celui_pour_la_moula import*

#fonctions
def bannane_eat():
    vie.ajoute(5)
    thunes.perte(100)
    return vie.total() and thunes.retour()

def poulet_eat():
    vie.ajoute(4)
    thunes.perte(75)
    return vie.total() and thunes.retour()

def pasteque_eat():
    vie.ajoute(3)
    thunes.perte(50)
    return vie.total() and thunes.retour()

def burger_eat():
    vie.ajoute(2)
    thunes.perte(25)
    return vie.total() and thunes.retour()

def brocoli_eat():
    thunes.perte(5)
    return vie.total() and thunes.retour()

#initialisation de la fenetre
magasin=Tk()
magasin.title("SuperMarcher")
magasin.geometry("1500x600")
magasin.configure(bg="Black")

#creation du canvas
cnv_fond=Canvas(magasin,width=1500,height=600,bg='black')
cnv_fond.place(x=-5,y=0)

#image des plats
img_bannane=Image.open("bannane.gif")
mon_image_bannane=ImageTk.PhotoImage(img_bannane)
cnv_fond.create_image(75,250,image=mon_image_bannane)

img_poulet=Image.open("poulet.gif")
mon_image_poulet=ImageTk.PhotoImage(img_poulet)
cnv_fond.create_image(360,250,image=mon_image_poulet)

img_pasteque=Image.open("pasteque.gif")
mon_image_pasteque=ImageTk.PhotoImage(img_pasteque)
cnv_fond.create_image(660,250,image=mon_image_pasteque)

img_burger=Image.open("burger.gif")
mon_image_burger=ImageTk.PhotoImage(img_burger)
cnv_fond.create_image(960,250,image=mon_image_burger)

img_brocoli=Image.open("brocoli.gif")
mon_image_brocoli = ImageTk.PhotoImage(img_brocoli)
cnv_fond.create_image(1260,250,image=mon_image_brocoli)

#creation et placement des bouttons
bannane=Button(magasin,text="Bannane",command=bannane_eat)
bannane.place(x=30,y=300)

poulet=Button(magasin,text="Poulet",command=poulet_eat)
poulet.place(x=310,y=300)

pasteque=Button(magasin,text="Pasteque",command=pasteque_eat)
pasteque.place(x=610,y=300)

burger=Button(magasin,text="Burger",command=burger_eat)
burger.place(x=910,y=300)

brocoli=Button(magasin,text="Brocoli",command=brocoli_eat)
brocoli.place(x=1210,y=300)

quitt=Button(magasin,text="quitter",command=magasin.destroy)
quitt.place(x=1400,y=550)

#○creation des label pour les prix
label_bannane=Label(magasin,text="Pix: 100 ₩",font=("",10))
label_bannane.place(x=30,y=350)

label_poulet=Label(magasin,text="Pix: 75 ₩",font=("",10))
label_poulet.place(x=310,y=350)

label_pasteque=Label(magasin,text="Pix: 50 ₩",font=("",10))
label_pasteque.place(x=610,y=350)

label_burger=Label(magasin,text="Pix: 25 ₩",font=("",10))
label_burger.place(x=910,y=350)

label_brocoli=Label(magasin,text="Pix: 5 ₩",font=("",10))
label_brocoli.place(x=1210,y=350)

magasin.mainloop()
