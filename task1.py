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
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()

f = open('map1.txt')
map1 = f.readlines()
walls = []
for i in range(1,15):
    print(map1[i])
    for i in range (len(map1)):
        print(map1[i])
        for j in range(len(map1[i])):
            #print(map1[i][j])
            if map1[i][j] == "*":
                print(f"wall at {j},{i}")
                c.create_rectangle(j,i,j,i)


'''

for i in range(1,15):
    print(map1[i])
'''
f.close()

w.mainloop()