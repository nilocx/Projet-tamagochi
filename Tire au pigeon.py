from random import*
from STAT_du_Perso_Tamagochie_cslg import*
from celui_pour_la_moula import*
from tkinter import*
from PIL import Image, ImageTk

#definition des fonction
def createPigeon():
    global pigeons
    global compteurpigeon
    pigeons=[]
    x_position = randint(-250,425)
    y_position = 100
    pigeonne = ImageTk.PhotoImage(Image.open("pigeon.gif"))
    my_pigeon = cvn.create_image(x_position, y_position, image = pigeonne, anchor = 's')
    pigeons.append([my_pigeon,randint(5,10),pigeonne])
    compteurpigeon+=1
    if not timer==60:
        fenetreTireauPigeon.after(randint(700,3000),createPigeon)
    print ("compteur:",compteurpigeon)
    return compteurpigeon

def movePigeon():
    for i in pigeons:
        cvn.move(i[0],0,i[1])
    if not timer==60:
        fenetreTireauPigeon.after(randint(5,15), movePigeon)

#gestion du score
def point(event):
    global score
    X = event.x
    Y = event.y
    score+=1
    score_label['text'] = "Compteur: " + str(score)
    print("scor:",score)
    return score

#gestion du temps
def temps():
    """
    Incrémente le timer à chaque seconde
    """
    global timer
    timer += 1
    timer_label['text'] = "Timer: " + str(timer)
    if timer==5:
        cvn.delete('all')
        print("timer:",timer)
        return timer
    fenetreTireauPigeon.after(1000, temps)


#creation de la fenetre
fenetreTireauPigeon=Tk()
fenetreTireauPigeon.title("Tire Au Pigeon")
fenetreTireauPigeon.geometry("775x550")

#affichage du temp
timer = 0
timer_label = Label(fenetreTireauPigeon, text="Timer: " + str(timer),font=("",10))
timer_label.pack()

#affichage du score
score=0
score_label = Label(fenetreTireauPigeon,text="Compteur: " + str(score),font=("",10))
score_label.pack()

#affichage fin du jeu
compteurpigeon=0
if timer==5:
    if compteurpigeon==score:
        cvn.delete('all')
        victoire_label = Label(fenetreTireauPigeon, text="VICTOIRE!!!! Le nombre de pigeons est juste!")
        victoire_label.pack()
        thunes.ajout(100)
        fenetreTireauPigeon.after(30000,fenetreTireauPigeon.destroy)
    else:
        cvn.delete('all')
        defaite_label = Label(fenetreTireauPigeon,text="PERDUUUUUUUUUUUUUUUUU")
        defaite_label.pack()
        fenetreTireauPigeon.destroy

#creation du canvas pour le fond
fond = Image.open("fond.gif")
photo = ImageTk.PhotoImage(fond)
cvn=Canvas(fenetreTireauPigeon, width=1000,height=1000)
cvn.create_image(0,0, image=photo, anchor="nw")
cvn.pack()

#Boutton de destruction TEMPORAIre.............................................................
destruction=Button(fenetreTireauPigeon,text="DESTRUCTION",command=fenetreTireauPigeon.destroy)
destruction.pack()
destruction_w=cvn.create_window(200, 200, window=destruction)
teste=Button(fenetreTireauPigeon,text="test",command=createPigeon)
teste.pack()
teste_w=cvn.create_window(100,100,window=teste)
#...............................................................................................

cvn.bind('<Button-1>',point)
cvn.pack()

fenetreTireauPigeon.after(1000, temps)

createPigeon()
movePigeon()

fenetreTireauPigeon.mainloop()