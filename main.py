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
        #Manque conditions de rebonds sur les paddles
        if pos[1] <= 0:
            self.yspeed = 3
        if pos[0] <= 0:
            self.xspeed = 3
        if pos[2] >= 400:
            self.xspeed = -3
        if pos[3] >= 600:
            self.yspeed = -3

class Paddle:
    def __init__(self, canvas, top) :
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0, 100, 10, fill="blue")
        if(top == "true"):
            self.canvas.move(self.id, 200,50)
            self.canvas.bind_all('<KeyPress-q>', self.move_left)
            self.canvas.bind_all('<KeyPress-d>', self.move_right)
        else :
            self.canvas.move(self.id, 200,550)
            self.canvas.bind_all('<KeyPress-Left>', self.move_left)
            self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.xspeed = 0

    def draw(self):
        self.canvas.move(self.id, self.xspeed, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 :
            self.xspeed = 0
        if pos[2] >= 400:
            self.xspeed = 0

    def move_left(self, evt):
        self.xspeed = -2
    def move_right (self, evt):
        self.xspeed = 2

w = tkinter.Tk()
w.title("Pong")
can = tkinter.Canvas (w, bg = "white", height = 600, width = 400)
can.pack()
paddle_bot = Paddle(can,"false")
paddle_top = Paddle(can,"true")
ball = Ball(can)

while 1 :
    ball.move()
    paddle_bot.draw()
    paddle_top.draw()
    w.update()
    time.sleep(0.01)

w.mainloop()
