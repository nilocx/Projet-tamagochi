class Money():
    def __init__(self):
        self.argent=0

    def ajout(self,montant):
        self.argent += montant

    def perte(self,montant):
        if self.argent>montant:
            self.argent -= montant
        else:
            return "pas assez d'argent pour acheter"

    def retour(self):
        return self.argent



thunes=Money()



