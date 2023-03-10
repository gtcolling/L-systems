# Fractal and graphic interpretation of strings
# Quadratic Koch's Island
# Alphabet: "F"
# Constants: "+", "-"
# Angle = 90 degrees
# Axiom = "F+F+F+F
# Rules: (F -> F+F-F-FF+F+F-F)
# "F" - Draw a line segment
# "+" - Right turn by angle
# "-" - Left turn by angle

import time
import turtle


def main():
    # starting string
    axiom = "F+F+F+F"
    # number of generations
    gen = 4

    start = time.time()
    create_system(axiom, gen)
    end = time.time()
    ex1 = str(end - start) + " seconds"

    print(ex1)

# generate our final string of commands
def create_system(s, gen):
    count = 0
    for x in range(gen):
        print("Generation " + str(x + 1) + ": " + str(s))
        count += 1
        # when we reach our targeted generation and final string, draw the system
        if gen - count == 0:
            draw(s)
            return
        temp = ''
        for y in range(len(s)):
            # programming our rule p: F -> F+F-F-FF+F+F-F
            if s[y] == 'F':
                temp += 'F+F-F-FF+F+F-F'
            elif s[y] == '+':
                temp += s[y]
            elif s[y] == '-':
                temp += s[y]
        s = temp


def draw(s):
    d = 5

    #position the turtle
    turtle.setup(width=1.0, height=1.0)
    turtle.bgcolor("black")
    turtle.color("red")
    turtle.penup()
    turtle.goto(-300, -300)
    turtle.pendown()
    turtle.speed(0)
    #go through the whole string and execute the commands
    for z in range(len(s)):
        if s[z] == 'F':
            turtle.forward(d)
        elif s[z] == '+':
            turtle.left(90)
        elif s[z] == "-":
            turtle.right(90)
    #fin
    turtle.done()
    return

main()
