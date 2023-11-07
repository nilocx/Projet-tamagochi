from tkinter import*

avertissement=Tk()
avertissement.title("ATTENTION")
attention=Label(avertissement,text="Attention vous n'avez pas de fusils'")
attention.pack
alternative=Label(avertissement,text="Mais vous pouvez compter les pigeons")
alternative.pack
bnt_lancer=Button(avertissement,text="lancer",command=avertissement.destroy)
bnt_lancer.pack()