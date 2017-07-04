"""A practical use of lists"""
from random import randint
from tkinter import *


def getRandomColor():
    """Generate random hexadecimal colours"""
    color = "#"
    for number in range(6):
        color += toHexChar(randint(0, 15))
    return color

# --------------------------------------------------------------------------------------------------

def toHexStr(hexValue):
    """Return a string format of HEX color"""
    if 0 <= hexValue <= 9:
        return str(hexValue + ord('0'))
    else:
        return str(hexValue - 10 + ord('A'))

# --------------------------------------------------------------------------------------------------

def toHexChar(hexValue):
    """Returns a unicode string of @param: hexValue"""
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))
# --------------------------------------------------------------------------------------------------

class Ball:
    """Primary model class for defining a ball"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 10
        self.dy = 10
        self.radius = 10
        self.color = getRandomColor()
# --------------------------------------------------------------------------------------------------

class BounceBalls:
    """Primary class for displaying GUI, command actions, and animations"""
    def __init__(self):
        self.ballList = []

        window = Tk()
        window.title("Bouncing Balls")

        self.width = 680
        self.height = 420
        self.canvas = Canvas(window, bg="white", width= self.width, height=self.height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text="Stop", command=self.stop)
        btStop.pack(side=LEFT)
        btResume = Button(frame, text="Resume", command=self.resume)
        btResume.pack(side=LEFT)
        btAdd = Button(frame, text="+", command=self.add)
        btAdd.pack(side=LEFT)
        btRemove = Button(frame, text="-", command=self.remove)
        btRemove.pack(side=LEFT)
        btnFaster = Button(frame, text="Faster", command=self.faster)
        btnFaster.pack(side=LEFT)
        btnSlower = Button(frame, text="Slower", command=self.slower)
        btnSlower.pack(side=LEFT)
        btnBiggerBalls = Button(frame, text="Bigger Balls", command=self.bigger_balls)
        btnBiggerBalls.pack(side=LEFT)
        self.lblCounter = Label(frame, text=0)
        self.lblCounter.pack(side=LEFT)

        self.sleepTime = 30
        self.isStopped = False
        self.biggerBalls = False
        self.animate()

        window.mainloop()
    # --------------------------------------------------------------------------------------------------

    def stop(self):
        """Stop animation of balls"""
        if len(self.ballList) > 0:
            self.isStopped = True
        else:
            # This is for a case where we do not want the animation to be stopped where there is an empty screen
            self.count(False) 
    # --------------------------------------------------------------------------------------------------

    def count(self, flag):
        """Count the number of balls on screen"""
        if flag == True: # A Python way would be: if flag:
            self.lblCounter["text"] = str(len(self.ballList))
        elif flag == False: # A Python way would be: elif not flag:
            self.lblCounter["text"] = "Sorry, no balls in the list"
    # --------------------------------------------------------------------------------------------------

    def resume(self):
        """Resume animation of balls"""
        self.isStopped = False
        self.animate()
    # --------------------------------------------------------------------------------------------------

    def add(self):
        """Add a new ball to the list of balls"""
        self.ballList.append(Ball())
        self.count(True)
    # --------------------------------------------------------------------------------------------------

    def remove(self):
        """Remove a ball from the list of balls"""
        if len(self.ballList) > 0:
            self.ballList.pop()
            self.count(True)
        else:
            self.count(False)
    # --------------------------------------------------------------------------------------------------
    
    def faster(self):
        """Increase the speed of animation"""
        self.sleepTime -= 2
        print (self.sleepTime)

    def slower(self):
        """Decrease the speed of animation"""
        self.sleepTime += 2
        print (self.sleepTime)

    def bigger_balls(self):
        """Make the balls appear bigger or smaller"""
        self.biggerBalls = True

    def animate(self):
        """Animate balls within the screen boundary"""
        while not self.isStopped:
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            self.canvas.delete("ball")

            for ball in self.ballList:
                if self.biggerBalls:
                    ball.radius = 30
                    self.redisplayBall(ball)
                else:
                    self.redisplayBall(ball)
    # --------------------------------------------------------------------------------------------------
    
    def redisplayBall(self, ball):
        """Display previously removed ball on new position"""
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx

        if  ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy
        
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius,
        ball.y - ball.radius, ball.x + ball.radius, 
        ball.y + ball.radius, fill = ball.color, tags = "ball")
    # --------------------------------------------------------------------------------------------------

BounceBalls() # Create GUI