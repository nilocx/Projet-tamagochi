### Classe permetant la gestion des statistique du personnage.

class Statistique:
    def __init__(self):
        #initialisation des variable
        self.stat=[1,2,3,4,5,6,7,8,9,10]
    def est_vide(self):
        #verifie si la liste choisie est remplie ou non
        if len(self.stat)==0:
            return True and print('Vide/mort')
        else:
            return False and print('Toujours vivant, toujhour la bannane')
    def ajoute(self,augmentation):
        #ajoute une element a la liste choisi
        if len(self.stat)==10:
            return "est plein"
        else:
            for i in range(augmentation):
                self.stat.append(1)
        return self.stat
    def suprime(self,supression):
        #suprime le dernier eleemnt de la liste choisie
        if len(self.stat)!=0:
            for j in range(supression):
                self.stat.pop()
        else :
            print('Vide/mort')
        return self.stat
    def total(self):
        #renvoi le contenue de la variable choisi
        return len(self.stat)

