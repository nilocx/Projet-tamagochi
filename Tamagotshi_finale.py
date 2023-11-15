from tkinter import*
import random
from STAT_du_Perso_Tamagochie_cslg import*
from celui_pour_la_moula import*
global faim , energie , humeur , argent , en_jeu
from PIL import Image, ImageTk







### Class principale contenant le personnage.
class TamaGotshi:
    def __init__(self, faim, energie, humeur, argent):
        #Initialisation des variables dans la class
        self.faim = faim
        self.energie = energie
        self.humeur = humeur
        self.argent = argent
        self.dort = False
        self.vient_de_cliquer = True


        self.argent.ajout(10) # donne un peu d'argent dès le debut du jeu /peut servir pour des test en changeant le montant


        self.fenetre = Tk()
        self.fenetre.title("TamaGotshi")
        self.fenetre.geometry("1900x1000")

        self.canvas_width = 1700
        self.canvas_height = 800

        self.BoutonQuitter=Button(self.fenetre,text="Quitter",fg ="#660066", bg="black",height=4,width=25,command=self.fenetre.destroy)
        self.BoutonQuitter.pack(side=BOTTOM,padx=10,pady=20)

        self.BoutonMenu=Button(self.fenetre,text="📱 : menu",fg ="white", bg="black",height=52,width=13,command=self.menu)
        self.BoutonMenu.place(x=0,y=0)

        # Création d'un canvas pour afficher l'image
        self.can = Canvas(self.fenetre, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.can.pack()

        # Chargement de l'image du lit à afficher sur le canvas
        self.img_lit =  PhotoImage(file="lit_vide.png")
        self.image_lit = self.can.create_image(0,0,anchor= NW, image=self.img_lit)


        # Chargement de l'image du personnage à afficher sur le canvas
        self.image =  PhotoImage(file="stickman_immmobile.PNG")
        self.image_width = self.image.width()
        self.image_height = self.image.height()
        self.image_perso = self.can.create_image(250, 250, anchor= NW, image=self.image)


        self.prev_x, self.prev_y = 250, 250
        self.img_prise = False # Variable pour indiquer si l'image est tenue


        #mise en place des label pour les differente statistique et pour l'argent
        self.faim_label = Label(self.fenetre,text ="Faim: " + str(faim.total()) + "/10", font=("tahoma Bold", 13))
        self.faim_label.place(x = 5 , y = 900 )

        self.energie_label = Label(self.fenetre,text ="Energie: " + str(energie.total()) + "/10", font=("tahoma Bold", 13))
        self.energie_label.place(x = 5 , y = 880)

        self.humeur_label = Label(self.fenetre,text ="Humeur: " + str(humeur.total()) + "/10", font=("tahoma Bold", 13))
        self.humeur_label.place(x = 5 , y = 860)

        self.argent_label=Label(self.fenetre,text="Argent: "+ str(argent.retour())+"₩", font=("tahoma Bold", 13))
        self.argent_label.place(x=5,y=930)




        self.mouvement_alea() # appelle la fonction de mouvement aléatoire dès le lancement du jeu
        self.baisse_energie() # appelle la fonction de mouvement pour baisser l'energie dès le lancement du jeu
        self.baisse_faim() # appelle la fonction de mouvement pour baisser la faim dès le lancement du jeu
        self.refresh_stat() # appelle la fonction pour toutes les  stats soit toujours bonnes sur l'ecran

        # Mise en place du bouton pour dormir
        self.btnDodo =  Button(self.fenetre, text="Dormir", font=("tahoma Bold", 13), fg='red', command=self.dormir)
        self.btnDodo.place(x=125, y=900)

        # Appelle la fonction correspondante au action fait par le joueur avec la souris
        self.can.bind("<Button-1>", self.canvas_clique)
        self.can.bind("<ButtonRelease-1>", self.canvas_relache)
        self.can.bind("<B1-Motion>", self.canvas_glisse)

    def ouvrir_uber_eats(self):
        #fonction pour ouvrir le magasin
        uber_eats=Magasin(self.fenetre)


    def annexeTAP(self):

        #creation de la fenetre
        self.avertissement=Tk()
        self.avertissement.geometry("500x500")
        self.avertissement.title("ATTENTION")

        #affichage du texte
        self.attention=Label(self.avertissement,text="Ha mince... Vous n'avez pas de fusils...")
        self.attention.pack()

        self.ironie=Label(self.avertissement,text="Domage  ¯\_(ツ)_/¯ ")
        self.ironie.pack()

        self.alternative=Label(self.avertissement,text="Mais vous pouvez les compter, pendant 1 minute !")
        self.alternative.pack()

        self.consigne=Label(self.avertissement,text=" Pour cela cliquez quand vous voyez un pigeon apparaitre.")
        self.consigne.pack()

        self.attention=Label(self.avertissement,text="(ATTENTION il y en a toujours 1 qui apparait a la fin en haut de l'écran et il compte quand même 🙂)",font=("", 8))
        self.attention.pack()

        self.recompense=Label(self.avertissement,text="Si votre compte est juste vous recervrez de l' argent pour vous nourrir.")
        self.recompense.pack()

        #creation du bouton pour fermer la fenetre et lancer le jeu
        self.bnt_lancer=Button(self.avertissement,text="lancer",command=self.lancement)
        self.bnt_lancer.pack()

    def lancement(self) :
        #fonction pour lancer le TAP
        en_jeu = True
        self.clique = True
        self.avertissement.destroy()
        if self.clique == True and en_jeu == True :
            tire_au_pigeon = TAP(self.fenetre)
            self.clique = False





    def parametre(self):

        self.fenetre3 = Tk()
        self.fenetre3.title("paramètre")
        self.fenetre3.configure(bg = "#878c94")
        self.fenetre3.geometry("528x356")
        self.fichierImage1 = PhotoImage(master=self.fenetre3, file = "Tamagotchi-1.png")
        self.labelImageDeFond1 = Label(self.fenetre3, image=self.fichierImage1)
        self.labelImageDeFond1.place(x=0, y=0)
        self.BoutonQuitter=Button(self.fenetre3,text="Quitter",fg ="#660066", bg="black",command=self.fenetre3.destroy)
        self.BoutonQuitter.place(x=0, y=0)

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

        self.BoutonTAP=Button(self.fenetre2,text="🦆TAP🦆",fg ="black", bg="#41edf2",height=2,width=5,command=self.annexeTAP)
        self.BoutonTAP.place(x=65, y=93)

        self.Boutonparametre=Button(self.fenetre2,text="⚙",fg ="black", bg="#e29723",height=2,width=4,command=self.parametre)
        self.Boutonparametre.place(x=20, y=36)

        self.BoutonShop=Button(self.fenetre2,text="💸",fg ="black", bg="#f44575",height=2,width=5,command=self.ouvrir_uber_eats)
        self.BoutonShop.place(x=65, y=35)



    def dormir(self):
        #enlève l'image du lit vide
        self.image_lit =self.can.delete

        #met le perso en dehors de la fenetre et le supprime
        self.can.coords(self.image_perso, 2000, 0)
        self.image_perso =self.can.delete


        #crée l'image du lit avec le perso dedans
        self.img_lit =  PhotoImage(file="stickman_dors_dans_un_lit.PNG")
        self.image_lit = self.can.create_image(0,0,anchor= NW, image=self.img_lit)

        # Mise en place du bouton pour se reveiller
        self.btnDodo.destroy()
        self.btnPasDodo =  Button(self.fenetre, text="Se reveiller", font=("tahoma Bold", 13), fg='red', command=self.se_reveiller)
        self.btnPasDodo.place(x=125, y=900)

        self.vient_de_cliquer=True
        self.dort=True

        self.aug_energie()

    def aug_energie(self):
        global en_jeu
        if self.dort==True and self.vient_de_cliquer == False and en_jeu == False:
            self.energie.ajoute(1)
            self.fenetre.after(10000, self.aug_energie)
        else:
            self.vient_de_cliquer = False
            self.fenetre.after(10000, self.aug_energie)



    def se_reveiller(self):
        #enlève l'image du lit avec le perso dedans
        self.image_lit =self.can.delete

        #crée l'image du lit vide
        self.img_lit =  PhotoImage(file="lit_vide.png")
        self.image_lit = self.can.create_image(0,0,anchor= NW, image=self.img_lit)

        #recrée le perso dans la fenetre
        self.image =  PhotoImage(file="stickman_immmobile.PNG")
        self.image_width = self.image.width()
        self.image_height = self.image.height()
        self.image_perso = self.can.create_image(250, 250, anchor= NW, image=self.image)

        # Mise en place du bouton pour dormir
        self.btnPasDodo.destroy()
        self.btnDodo =  Button(self.fenetre, text="dormir", font=("tahoma Bold", 13), fg='red', command=self.dormir)
        self.btnDodo.place(x=125, y=900)

        self.dort = False
        self.vient_de_cliquer = True
        self.baisse_energie()

    def baisse_energie(self):
        global en_jeu
        if self.dort==False and self.vient_de_cliquer == False and en_jeu == False :
            self.energie.suprime(1)
            self.fenetre.after(20000, self.baisse_energie)
        else:
            self.fenetre.after(20000, self.baisse_energie)

    def baisse_faim(self):
        global en_jeu
        if self.vient_de_cliquer == False and en_jeu == False :
            self.faim.suprime(1)
            self.fenetre.after(15000, self.baisse_faim)
        else:
            self.vient_de_cliquer = False
            self.fenetre.after(15000, self.baisse_faim)


    def refresh_stat(self):
        self.energie_label['text'] = "Energie: " + str(self.energie.total()) + "/10"
        self.faim_label['text'] = "Faim:" + str(self.faim.total()) + "/10"
        self.humeur_label['text'] = "Humeur: " + str(self.humeur.total()) + "/10"
        self.argent_label['text'] = "Argent: " + str(self.argent.retour()) +"₩"
        self.fenetre.after(1000, self.refresh_stat)

    def mouvement_alea(self): # Fonction pour déplacer l'image de manière aléatoire
        liste = [60000,55000,50000,45000,40000,35000,30000,25000,20000,15000,10000,5000,1000,1000,1000,10000,50000,60000,25000]
        if not self.img_prise: # Vérifier si l'image est tenue par le joueur
            x, y = random.randint(0, self.canvas_width - self.image_width), random.randint(0, self.canvas_height - self.image_height)
            self.can.coords(self.image_perso, x, y)  # Déplacer l'image à de nouvelles coordonnées aléatoires
        self.fenetre.after(random.choice(liste), self.mouvement_alea)

    def canvas_clique(self, event):  # Fonction appelée lorsqu'un clic de souris est détecté sur le canvas
        self.prev_x, self.prev_y = event.x, event.y
        self.img_prise = True

    def canvas_relache(self, event):  # Fonction appelée lorsque le bouton de la souris est relâché
        self.img_prise = False

    def canvas_glisse(self, event): # Fonction appelée lorsqu'un glissement de souris est détecté sur le canvas
        x, y = event.x, event.y
        self.can.move(self.image_perso, x - self.prev_x, y - self.prev_y)
        self.prev_x, self.prev_y = x, y

    def run(self):
        self.fenetre.mainloop()



### Class contenant le mini-jeu du Tire au pigeon.

class TAP:
    def __init__(self,tama):
        self.fenetreTireauPigeon = Toplevel(tama)
        self.fenetreTireauPigeon.title("Tire Au Pigeon")
        self.fenetreTireauPigeon.geometry("800x600")

        self.timer = 0
        self.score = 0
        self.compteurpigeon = 0
        self.pigeons=[]

        self.timer_label = Label(self.fenetreTireauPigeon, text="Timer: " + str(self.timer), font=("", 10))
        self.timer_label.pack()

        self.score_label = Label(self.fenetreTireauPigeon, text="Compteur: " + str(self.score), font=("", 10))
        self.score_label.pack()

        self.bnt_quitter = Button(self.fenetreTireauPigeon, text="Quitter", command=self.fenetreTireauPigeon.destroy)
        self.bnt_quitter.pack()


        self.fond = Image.open("fond.gif")
        self.photo = ImageTk.PhotoImage(self.fond)
        self.cvn = Canvas(self.fenetreTireauPigeon, width=1000, height=1000)
        self.cvn.create_image(0, 0, image=self.photo, anchor="nw")
        self.cvn.pack(padx=15, pady=15)

        self.cvn.bind('<Button-1>', self.point)
        self.cvn.pack()

        self.fenetreTireauPigeon.after(1000, self.temps)

        self.createPigeon()
        self.movePigeon()

        self.fenetreTireauPigeon.mainloop()

    def createPigeon(self):
        x_position = random.randint(-250, 425)
        y_position = 100
        self.pigeonne =  PhotoImage(file="pigeon.gif")
        self.my_pigeon = self.cvn.create_image(x_position,y_position,anchor= 's', image=self.pigeonne)
        self.pigeons.append([self.my_pigeon, random.randint(5, 10), self.pigeonne])
        self.compteurpigeon += 1
        if not self.timer == 58:
            self.fenetreTireauPigeon.after(random.randint(700, 3000), self.createPigeon)

    def movePigeon(self):
        for i in self.pigeons:
            self.cvn.move(i[0], 0, i[1])
        if not self.timer == 60:
            self.fenetreTireauPigeon.after(random.randint(5, 15), self.movePigeon)

    def point(self, event):
        X = event.x
        Y = event.y
        self.score+=1
        self.score_label['text'] = "Compteur: " + str(self.score)



    def temps(self):
        global en_jeu
        self.timer += 1
        self.timer_label['text'] = "Timer: " + str(self.timer)
        if self.timer == 60:
            self.fin_label = Label(self.fenetreTireauPigeon, text="Compteur: " + str(self.score)+ "Nombre reel de pigeon:" + str(self.compteurpigeon), font=("", 15))
            self.fin_label.place(x=250 ,y=250 )
            self.cvn.delete('all')
            if self.compteurpigeon == self.score:
                self.timer_label['text'] = "VICTOIRE!!!! Le nombre de pigeons est juste!"
                argent.ajout(100)
                humeur.ajoute(1)
                en_jeu = False
                self.fenetreTireauPigeon.after(5000, self.fenetreTireauPigeon.destroy)
            else:
                humeur.suprime(2)
                self.timer_label['text'] = "PERDUUUUUUUUUUUUUUUUU"
                en_jeu = False
                self.fenetreTireauPigeon.after(5000, self.fenetreTireauPigeon.destroy)
        self.fenetreTireauPigeon.after(1000, self.temps)



### Class contenant le magasin pour que le personnage puisse manger(la nourriture est mangé dès qu'elle est achetée).

class Magasin:
    def __init__(self,tama):
        self.faim = faim
        self.argent = argent

        # creation de la fenetre du magasin
        self.magasin = Toplevel(tama)
        self.magasin.title("SuperMarcher")
        self.magasin.geometry("1500x600")
        self.magasin.configure(bg="Black")

        # creation du canvas
        self.cnv_fond = Canvas(self.magasin, width=1500, height=600, bg='black')
        self.cnv_fond.place(x=-5, y=0)

        # image de la nourriture
        self.char_img()

        # crea et posi des btn
        self.crea_btn()

        # crea des label pour les prix
        self.crea_prix()

        self.magasin.mainloop()

    def char_img(self):
        self.img_bannane=Image.open("bannane.gif")
        self.mon_image_bannane=ImageTk.PhotoImage(self.img_bannane)
        self.cnv_fond.create_image(75,250,image=self.mon_image_bannane)

        self.img_poulet=Image.open("poulet.gif")
        self.mon_image_poulet=ImageTk.PhotoImage(self.img_poulet)
        self.cnv_fond.create_image(360,250,image=self.mon_image_poulet)

        self.img_pasteque=Image.open("pasteque.gif")
        self.mon_image_pasteque=ImageTk.PhotoImage(self.img_pasteque)
        self.cnv_fond.create_image(660,250,image=self.mon_image_pasteque)

        self.img_burger=Image.open("burger.gif")
        self.mon_image_burger=ImageTk.PhotoImage(self.img_burger)
        self.cnv_fond.create_image(960,250,image=self.mon_image_burger)

        self.img_brocoli=Image.open("brocoli.gif")
        self.mon_image_brocoli = ImageTk.PhotoImage(self.img_brocoli)
        self.cnv_fond.create_image(1260,250,image=self.mon_image_brocoli)


    def crea_btn(self):
        self.bannane=Button(self.magasin,text="Bannane",command=self.bannane_eat)
        self.bannane.place(x=30,y=300)

        self.poulet=Button(self.magasin,text="Poulet",command=self.poulet_eat)
        self.poulet.place(x=310,y=300)

        self.pasteque=Button(self.magasin,text="Pasteque",command=self.pasteque_eat)
        self.pasteque.place(x=610,y=300)

        self.burger=Button(self.magasin,text="Burger",command=self.burger_eat)
        self.burger.place(x=910,y=300)

        self.brocoli=Button(self.magasin,text="Brocoli",command=self.brocoli_eat)
        self.brocoli.place(x=1210,y=300)

        self.quitt=Button(self.magasin,text="quitter",command=self.magasin.destroy)
        self.quitt.place(x=1400,y=550)



    def crea_prix(self):

        self.label_bannane=Label(self.magasin,text="Pix: 100 ₩",font=("",10))
        self.label_bannane.place(x=30,y=350)

        self.label_poulet=Label(self.magasin,text="Pix: 75 ₩",font=("",10))
        self.label_poulet.place(x=310,y=350)

        self.label_pasteque=Label(self.magasin,text="Pix: 50 ₩",font=("",10))
        self.label_pasteque.place(x=610,y=350)

        self.label_burger=Label(self.magasin,text="Pix: 25 ₩",font=("",10))
        self.label_burger.place(x=910,y=350)

        self.label_brocoli=Label(self.magasin,text="Pix: 5 ₩",font=("",10))
        self.label_brocoli.place(x=1210,y=350)


    # les differentes valeur que la nourriture donnent
    def bannane_eat(self):
        faim.ajoute(5)
        argent.perte(100)

    def poulet_eat(self):
        self.faim.ajoute(4)
        argent.perte(75)

    def pasteque_eat(self):
        faim.ajoute(3)
        argent.perte(50)

    def burger_eat(self):
        self.faim.ajoute(2)
        self.argent.perte(25)

    def brocoli_eat(self):
        self.argent.perte(5)






#Initialisation de differente statistique
faim = Statistique()
energie = Statistique()
humeur = Statistique()
argent = Money()
en_jeu = False



app = TamaGotshi(faim, energie, humeur, argent)
app.run()
