# Fractal and graphic interpretation of strings
# Harter-Heighway Dragon
# Alphabet: "X", "Y"
# Constants: "F", "+", "-"
# Angle = 90 degrees
# Axiom = "FX"
# Rules: (X -> X+YF+), (Y -> -FX-Y)

import time
import turtle


def main():
    # starting string
    axiom = "FX"
    # number of generations
    gen = 13

    # ex_1 nested forloop
    start = time.time()
    create_system(axiom, gen)
    end = time.time()
    thing = str(end - start) + " seconds"

    print(thing)


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
            # programming our rule
            if s[y] == 'X':
                temp += 'X+YF+'
            elif s[y] == 'Y':
                temp += '-FX-Y'
            else:
                temp += s[y]
        s = temp


def draw(s):
    d = 2
    angle = 90
    turtle.setup(width=1.0, height=1.0)
    turtle.bgcolor("black")
    turtle.color("purple")
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()
    for z in range(len(s)):
        #programming the rules
        #in this case 'X' & 'Y' don't move the turtle and are just there for the curviture of the shape
        if s[z] == 'F':
            turtle.forward(d)
        elif s[z] == 'X':
            continue
        elif s[z] == 'Y':
            continue
        elif s[z] == '+':
            turtle.right(angle)
        elif s[z] == "-":
            turtle.left(angle)

    turtle.done()
    return


main()
