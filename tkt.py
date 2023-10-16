from tkinter import *
from random import randint
from PIL import Image, ImageTk

#make the fruits appear on the screen
def create_fruits():

    global fruits_list

    #choose random fruits with different possibilities
    which_fruit = randint(1,3)

    this_fruit = ImageTk.PhotoImage(Image.open(fruit_dic[which_fruit]))
    #randomly generate which colum (four in total) the fruits will be
    choose_position = randint (1,4)

    x_position = x_positions_dic[choose_position]  # choose the position from dict

    my_photo = canvas.create_image(x_position, 80, image = this_fruit, anchor = 's')

    #append it to the list(image_id, x position, image)
    fruits_list.append([my_photo, randint(5,10), this_fruit])

    #repeatedly generate fruit images every 3 second
    root.after(3000,create_fruits)


def move_fruits():

    for fruit in fruits_list:

        canvas.move(fruit[0], 0, fruit[1])

        if canvas.bbox(fruit[0])[3] >= canvas.winfo_height()+100:
            canvas.delete(fruit[0])
            fruits_list.remove(fruit)

    root.after(10, move_fruits)  # calls the move_fruits after every 10 seconds

root = Tk()

canvas = Canvas (root, height = 1200, width = 800, bg = 'black')
canvas.pack()

fruits_list = []

x_positions_dic = {1: 112.5, 2: 287.5, 3: 462.5, 4:637.5}
fruit_dic = {1: r"test.png" , 2: r"test.png" , 3: r"test.png"} # your path here

create_fruits()
move_fruits()

root.mainloop()