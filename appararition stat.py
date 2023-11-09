# coding: utf-8
from tkinter import*
from STAT_du_Perso_Tamagochie_cslg import Statistique
maFenetre = Tk()
maFenetre.geometry("1900x1000")
faim = Statistique()
energie = Statistique()
humeur = Statistique()

faim_label = Label(maFenetre,text ="Faim:" + str(faim.stat[-1]) + "/10")
faim_label.place(x = 5 , y = 900 )

energie_label = Label(maFenetre,text =f"Energie" + str(energie.stat[-1]) + "/10")
energie_label.place(x = 5 , y = 880)

humeur_label = Label(maFenetre,text =f"Humeur" + str(humeur.stat[-1]) + "/10")
humeur_label.place(x = 5 , y = 860)

maFenetre.mainloop()