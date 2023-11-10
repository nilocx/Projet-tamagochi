from tkinter import*
#from PIL import Image, ImageTk
from STAT_du_Perso_Tamagochie_cslg import*
from celui_pour_la_moula import*

#Dicitonnaire contenant les aliments et leurs valeur en vie
nourriture={"banane": 5, "ailes de poulet": 4, "hamburger": 3, "pasteque": 2, "brocoli": 1}
vie=Statistique()

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
    vie.ajoute(1)
    thunes.perte(1)
    return vie.total() and thunes.retour()

#initialisation de la fenetre
magasin=Tk()
# fond = Image.open("fond.gif")
# Icon = ImageTk.PhotoImage(fond)
# magasin.iconbitmap(Icon)
magasin.title("SuperMarcher")
magasin.geometry("1500x600")
magasin.configure(bg="Black")

#image des plats


#creation et placement des bouttons
bannane=Button(magasin,text="Bannane",command=bannane_eat)
bannane.place(x=10,y=400)
poulet=Button(magasin,text="Poulet",command=poulet_eat)
poulet.place(x=310,y=400)
pasteque=Button(magasin,text="Pasteque",command=pasteque_eat)
pasteque.place(x=610,y=400)
burger=Button(magasin,text="Burger",command=burger_eat)
burger.place(x=910,y=400)
brocoli=Button(magasin,text="Brocoli",command=brocoli_eat)
brocoli.place(x=1210,y=400)
quitt=Button(magasin,text="quiter",command=magasin.destroy)
quitt.place(x=1400,y=550)

magasin.mainloop()
