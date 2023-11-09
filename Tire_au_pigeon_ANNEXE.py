from tkinter import*
from PIL import Image, ImageTk

#creation de la fenetre
avertissement=Tk()
avertissement.geometry("500x500")
avertissement.title("ATTENTION")

#affichage du texte
attention=Label(avertissement,text="Ha mince... Vous n'avez pas de fusils...")
attention.pack()

ironie=Label(avertissement,text="Domage  ¯\_(ツ)_/¯ ")
ironie.pack()

alternative=Label(avertissement,text="Mais vous pouvez les compter, pendant 1 minute !")
alternative.pack()

consigne=Label(avertissement,text=" Pour cela cliquez quand vous voyez un pigeon apparaitre.")
consigne.pack()

recompense=Label(avertissement,text="Si votre compte est juste vous recervrez de l' argent pour vous nourrir.")
recompense.pack()

#creation du bouton pour fermer la fenetre et lancer le jeu
bnt_lancer=Button(avertissement,text="lancer",command=avertissement.destroy)
bnt_lancer.pack()

avertissement.mainloop()
