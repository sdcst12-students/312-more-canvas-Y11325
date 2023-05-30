import tkinter as tk
from PIL import ImageTk,Image

"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map1.txt')


def getImage(x,y):
    img = Image.open("assets/tiles.png").convert("RGBA")
    xi = x*50
    yi = y*50
    img2 = img.crop([xi,yi,xi+50,yi+50])
    return ImageTk.PhotoImage(img2)


#img = tk.PhotoImage(file="assets/tiles.png")
map = [ (0,1) , (3,4) , (5,10) , (9,0) , (10,3)]
walls = []
img = [[]]
img.append(getImage(2,300))
walls.append(c.create_image(2*50+32,1*50+32,image=img[-1]))
'''
for j in range(4):
        print(i,j)
        img.append(getImage(i,j+8))
        walls.append(c.create_image(i*64+32,j*64+32,image=img[-1]))
'''
w.mainloop()