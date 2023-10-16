from random import*
from STAT_du_Perso_Tamagochie_cslg import*
from tkinter import*
from PIL import Image, ImageTk

def createPigeon(delay):
    pigeon = ImageTk.PhotoImage(Image.open(r"pigeon.gif"))
    y_position = randint(200,475)
    my_photo = canvas.create_image(y_position, 80, image = piegon, anchor = 's')
    root.after(delay,createPigeon)

def movePigeon():
    for fruit in fruits_list:
        canvas.move(fruit[0], 0, fruit[1])
        if canvas.bbox(fruit[0])[3] >= canvas.winfo_height()+100:
            canvas.delete(fruit[0])
            fruits_list.remove(fruit)
    root.after(10, movePigeon)


#creation de la fenetre
fenetreTireauPigeon=Tk()
fenetreTireauPigeon.title("Tire Au Pigeon")
fenetreTireauPigeon.geometry("770x475")

fond = Image.open("fond.gif")
photo = ImageTk.PhotoImage(fond)

# #image de fond
# load = Image.open("fond.png")
# render = ImageTk.PhotoImage(load)
# load = Image.open("fond.png")
# render = ImageTk.PhotoImage(load)
# img = Label(fenetreTireauPigeon, image=render)
# img.image = render
# img.place(x=-1, y=0)

cvn=Canvas(fenetreTireauPigeon, width=770,height=475)
cvn.create_image(0,225, image=photo,anchor="center")
cvn.pack()

#Boutton de destruction TEMPORAIre
destruction=Button(fenetreTireauPigeon,text="DESTRUCTION",command=fenetreTireauPigeon.destroy)
destruction_w=cvn.create_window(200, 200, window=destruction)

fenetreTireauPigeon.mainloop()