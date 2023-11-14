from tkinter import*
import random
from STAT_du_Perso_Tamagochie_cslg import Statistique
from celui_pour_la_moula import Money
from TAP import createPigeon, movePigeon, point, temps, TireAP
global faim , energie , humeur , argent
import subprocess



class TamaGotshi:
    def __init__(self, faim, energie, humeur, argent):
        #Initialisation des variables dans la class
        self.faim = faim
        self.energie = energie
        self.humeur = humeur
        self.argent = argent
        self.dort = False
        self.vient_de_cliquer = True


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
        self.faim_label = Label(self.fenetre,text ="Faim:" + str(faim.total()) + "/10", font=("tahoma Bold", 13))
        self.faim_label.place(x = 5 , y = 900 )

        self.energie_label = Label(self.fenetre,text ="Energie" + str(energie.total()) + "/10", font=("tahoma Bold", 13))
        self.energie_label.place(x = 5 , y = 880)

        self.humeur_label = Label(self.fenetre,text ="Humeur" + str(humeur.total()) + "/10", font=("tahoma Bold", 13))
        self.humeur_label.place(x = 5 , y = 860)

        self.argent_label=Label(self.fenetre,text="Argent"+ str(argent.retour())+"₩", font=("tahoma Bold", 13))
        self.argent_label.place(x=5,y=930)



        self.mouvement_alea() # Appelle la fonction de mouvement aléatoire dès le lancement du jeu
        self.baisse_energie() # Appelle la fonction de mouvement pour baisser l'energie dès le lancement du jeu

        # Mise en place du bouton pour dormir
        self.btnDodo =  Button(self.fenetre, text="Dormir", font=("tahoma Bold", 13), fg='red', command=self.dormir)
        self.btnDodo.place(x=125, y=900)

        # Appelle la fonction correspondante au action fait par le joueur avec la souris
        self.can.bind("<Button-1>", self.canvas_clique)
        self.can.bind("<ButtonRelease-1>", self.canvas_relache)
        self.can.bind("<B1-Motion>", self.canvas_glisse)



    def parametre(self):
        self.fenetre3 = Tk()
        self.fenetre3.title("paramètre")
        self.fenetre3.configure(bg = "#878c94")
        self.fenetre3.geometry("528x356")
        self.fichierImage1 = PhotoImage(master=self.fenetre3, file = "Tamagotshi-1.png")
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
        self.BoutonTAP=Button(self.fenetre2,text="🦆TAP🦆",fg ="black", bg="#41edf2",height=2,width=5,command=TireAP)
        self.BoutonTAP.place(x=65, y=93)
        self.Boutonparametre=Button(self.fenetre2,text="⚙",fg ="black", bg="#e29723",height=2,width=4,command=self.parametre)
        self.Boutonparametre.place(x=20, y=36)
        self.BoutonShop=Button(self.fenetre2,text="💸",fg ="black", bg="#f44575",height=2,width=5,command=self.exec(open("Magasin_Prototype.py").read()))
        self.BoutonShop.place(x=65, y=35)

    def appel(self):
        subprocess.call("Magasin_Prototype.py",shell=True)

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
        if self.dort==True and self.vient_de_cliquer == False:
            self.energie.ajoute(1)
            self.energie_label['text'] = "Energie" + str(self.energie.total()) + "/10"
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
        if self.dort==False and self.vient_de_cliquer == False :
            self.energie.suprime(1)
            self.energie_label['text'] = "Energie" + str(self.energie.total()) + "/10"
            self.fenetre.after(60000, self.baisse_energie)
        else:
            self.vient_de_cliquer = False
            self.fenetre.after(60000, self.baisse_energie)

    def baisse_faim(self):
        self.faim.suprime(1)
        self.faim_label['text'] = "Faim: " + str(self.faim.total()) + "/10"
        self.fenetre.after(7000, self.baisse_faim)

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


#Initialisation de differente statistique
faim = Statistique()
energie = Statistique()
humeur = Statistique()
argent = Money()


app = TamaGotshi(faim, energie, humeur, argent)
app.run()
