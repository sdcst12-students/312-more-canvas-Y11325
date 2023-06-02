import tkinter as tk
from PIL import ImageTk,Image
import math
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.title("Garden Maze")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()

f = open('map1.txt')
map1 = f.readlines()

mapimg = tk.PhotoImage(file="assets/map.forest.png")

walls = []

for i in range (len(map1)):
    print(map1[i])
    for j in range(len(map1[i])):
        if map1[i][j] == "*":
            print(f"wall at {j},{i}")
            img = c.create_image(j*30+30,i*30+30,image=mapimg)
            walls.append(img)

rec = c.create_rectangle(50,50,70,70,fill="SkyBlue")


def keyPress(e):
    print(e)
    print(e.keycode, e.keysym, e.x, e.y)
    r = c.coords(rec)

    if e.keysym == 'Left':
        if r[0] > 50:
            c.move(rec,-5,0)
    elif e.keysym == 'Right':
        if r[2] < 850:
            c.move(rec,5,0)
    elif e.keysym == 'Up':
        if r[1] > 50:
            c.move(rec,0,-5)
    elif e.keysym == 'Down':
        if r[3] < 430:
            c.move(rec,0,5)


w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)


f.close()

w.mainloop()