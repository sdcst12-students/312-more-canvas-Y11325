#!python3

# Find an image to use as a sprite from the Internet.
# Modify the image (flipping horizontally is a quick way to do that) so that you have
# a second, different image. Use the tkObject.after() method to animate it.
# Note: You can find sprite sheets or tile sheets on the internet to help you!

import tkinter as tk
from PIL import Image,ImageTk

w = tk.Tk()
w.title("task3")
w.attributes("-topmost",True)
w.geometry("500x500")

c = tk.Canvas(width=480,height=480)
c.pack()

x = 0
y = 0
i = 0

def getSprite(x,y):
    img = Image.open("assets/catspritesheet.png").convert("RGBA")
    xi = x*78
    yi = y*92
    img2 = img.crop([xi,yi,xi+72,yi+92])
    return ImageTk.PhotoImage(img2)    

def catUpdate():
    global i,c,img,w,cat
    #print(len(cat))
    i+=1
    i%=len(cat)
    c.itemconfig(img,image=cat[i])
    #print(i)
    w.after(100,catUpdate)

image = tk.PhotoImage(file="assets/catspritesheet.png")

cat=[]
for i in range(3):
    firstX = i + 4*x 
    cat.append( getSprite(firstX,y))
cat.append( getSprite(firstX+1,y))

img = c.create_image(72,92,image=cat[i])

w.after(100,catUpdate)


w.mainloop()