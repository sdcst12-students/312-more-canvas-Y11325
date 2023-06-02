import tkinter as tk
"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountain
5 Swamp
6 City
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()

f = open('map2.txt')
map2 = f.readlines()

water = tk.PhotoImage(file="assets/map.water.png")
plains = tk.PhotoImage(file="assets/map.plains.png")
forest = tk.PhotoImage(file="assets/map.forest.png")
hills = tk.PhotoImage(file="assets/map.hills.png")
mountain = tk.PhotoImage(file="assets/map.mountain.png")
swamp = tk.PhotoImage(file="assets/map.swamp.png")
city = tk.PhotoImage(file="assets/map.city.png")
walls = []

for i in range(len(map2)):
    for j in range (len(map2[i])):
        print(f"walls at {j},{i}")
        if map2[i][j] == "0":
            img = c.create_image(j*30+30,i*30+30,image=water)
            walls.append(img)
        elif map2[i][j] == "1":
            img = c.create_image(j*30+30,i*30+30,image=plains)
            walls.append(img)
        elif map2[i][j] == "2":
            img = c.create_image(j*30+30,i*30+30,image=forest)
            walls.append(img)
        elif map2[i][j] == "3":
            img = c.create_image(j*30+30,i*30+30,image=hills)
            walls.append(img)
        elif map2[i][j] == "4":
            img = c.create_image(j*30+30,i*30+30,image=mountain)
            walls.append(img)
        elif map2[i][j] == "5":
            img = c.create_image(j*30+30,i*30+30,image=swamp)
            walls.append(img)
        elif map2[i][j] == "6":
            img = c.create_image(j*30+30,i*30+30,image=city)
            walls.append(img)
        


w.mainloop()