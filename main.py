import tkinter
import random
import time

#Classe ball gérant le fonctionnement global de la balle.
class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10, 30,30,fill = "black")
        self.canvas.move(self.id, 245,100)
        self.xspeed = random.randrange(-3,3) #valeur de la vitesse de la balle aléatoire au départ.
        self.yspeed = -1

    #Fonction de déplacement appelé en boucle.
    def move(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.yspeed = 3
        if pos[0] <= 0:
            self.xspeed = 3
        if pos[2] >= 800:
            self.xspeed = -3
        if pos[3] >= 600:
            self.yspeed = -3


w = tkinter.Tk()
w.title("Pong")
can = tkinter.Canvas (w, bg = "white", height = 600, width = 800)
can.pack()
ball = Ball(can)

while 1 :
    ball.move()
    w.update()
    time.sleep(0.01)

w.mainloop()
