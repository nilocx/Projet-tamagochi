from random import*
from tkinter import*
from PIL import Image, ImageTk





def TAP():
    #creation de la fenetre
    fenetreTireauPigeon=Tk()
    fenetreTireauPigeon.title("Tire Au Pigeon")
    fenetreTireauPigeon.geometry("768x492")

    fond = Image.open("fond.gif")
    photo = ImageTk.PhotoImage(fond)



    cvn=Canvas(fenetreTireauPigeon, width=770,height=475)
    cvn.create_image(0,225, image=photo,anchor="center")
    cvn.pack()

    #Boutton de destruction TEMPORAIre
    destruction=Button(fenetreTireauPigeon,text="DESTRUCTION",command=fenetreTireauPigeon.destroy)
    destruction_w=cvn.create_window(200, 200, window=destruction)



    fenetreTireauPigeon.mainloop()


