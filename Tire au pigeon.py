from random import*
from tkinter import*
from PIL import Image, ImageTk
from STAT_du_Perso_Tamagochie_cslg import*
from celui_pour_la_moula import*
from Tire_au_pigeon_ANNEXE import*


#definition des fonction
#creation des pigeons
def createPigeon():
    '''
    Affiche les pigeon et les compte. Renvoi: le nombre de pigeons generer.
    '''
    global pigeons
    global compteurpigeon
    pigeons=[]
    x_position = randint(-250,425)
    y_position = 100
    pigeonne = ImageTk.PhotoImage(Image.open("pigeon.gif"))
    my_pigeon = cvn.create_image(x_position, y_position, image = pigeonne, anchor = 's')
    pigeons.append([my_pigeon,randint(5,10),pigeonne])
    compteurpigeon+=1
    if not timer==58:
        fenetreTireauPigeon.after(randint(700,3000),createPigeon)
    return compteurpigeon

#mouvement des pigeons
def movePigeon():
    '''
    Deplace les pigeons sur l'axe y
    '''
    for i in pigeons:
        cvn.move(i[0],0,i[1])
    if not timer==58:
        fenetreTireauPigeon.after(randint(5,15), movePigeon)

#gestion du score
def point(event):
    '''
    Compte et affiche a la fin du timer le nombre de clique et le renvoi
    '''
    global score
    X = event.x
    Y = event.y
    score+=1
    score_label['text'] = "Compteur: " + str(score)
    if timer==61:
        score_label['text'] = "Votre comte:" + str(score) + "Nombre reel de pigeon:" + str(compteurpigeon)
    return score

#gestion du temps
def temps():
    """
    Incrémente le timer à chaque seconde. Affiche le temps toute les seconde. Affiche si le joueur a gangner ou perdu. Renvoi: le
    timer.
    """
    global timer
    timer += 1
    timer_label['text'] = "Timer: " + str(timer)
    if timer==61:
        cvn.delete('all')
        if compteurpigeon==score:
            timer_label['text'] = "VICTOIRE!!!! Le nombre de pigeons est juste! Vous aez comptez :" +str(score) + "pigeons"
            thunes.ajout(100)
            humeur.ajout(1)
        else:
            humeur.suprime(2)
            timer_label['text'] = "PERDUUUUUUUUUUUUUUUUU"
        return timer
    fenetreTireauPigeon.after(1000, temps)


#creation de la fenetre
fenetreTireauPigeon=Tk()
fenetreTireauPigeon.title("Tire Au Pigeon")
fenetreTireauPigeon.geometry("800x600")

#affichage du temp
timer = 0
timer_label = Label(fenetreTireauPigeon, text="Timer: " + str(timer),font=("",10))
timer_label.pack()

#affichage du score
score=0
compteurpigeon=0
score_label = Label(fenetreTireauPigeon,text="Compteur: " + str(score),font=("",10))
score_label.pack()

bnt_quiter= Button(fenetreTireauPigeon,text="Quitter",command=fenetreTireauPigeon.destroy)
bnt_quiter.pack()

#creation du canvas pour le fond
fond = Image.open("fond.gif")
photo = ImageTk.PhotoImage(fond)
cvn=Canvas(fenetreTireauPigeon, width=1000,height=1000)
cvn.create_image(0,0, image=photo, anchor="nw")
cvn.pack(padx=15,pady=15)

#gestion du clique
cvn.bind('<Button-1>',point)
cvn.pack()

#actualisation de la fenetre toutes les secondes
fenetreTireauPigeon.after(1000, temps)

#appele des fonction
createPigeon()
movePigeon()

fenetreTireauPigeon.mainloop()
