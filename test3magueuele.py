from tkinter import*
from test4magueuele import TAP





def menu():
    fenetre2 = Tk()
    fenetre2.title("menu") #Affiche le titre en haut de la fenêtre
    fenetre2.configure(bg = "#878c94")
    fenetre2.geometry("150x250")
    #Création d'un bouton Quitter
    BoutonQuitter=Button(fenetre2,text="Quitter",fg ="#660066", bg="black",command=fenetre2.destroy)
    BoutonQuitter.pack(side=LEFT,padx=10,pady=10)
    #Création d'un bouton TAP
    BoutonTAP=Button(fenetre2,text="TAP",fg ="#660066", bg="black",command=TAP)
    BoutonTAP.pack(side=RIGHT,padx=10,pady=10)




