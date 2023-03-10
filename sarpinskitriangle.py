# Fractal and graphic interpretation of strings
# Sarpinski's Triangle
# Alphabet: "F, G"
# Constants: "+", "-"
# Angle = 120 degrees
# Axiom = "F"
# Rules: (F -> F-G+F+G-F), (G -> GG)
# "F", "G" - Draw a line segment
# "+" - Right turn by angle
# "-" - Left turn by angle

import time
import turtle


def main():
    # starting string
    axiom = "F"
    # number of generations
    gen = 7

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
            # programming our rule p: F -> F+F-F-FF+F+F-F
            if s[y] == 'F':
                temp += 'F-G+F+G-F'
            elif s[y] == 'G':
                temp += 'GG'
            elif s[y] == '+':
                temp += s[y]
            elif s[y] == '-':
                temp += s[y]
        s = temp


def draw(s):
    d = 10
    angle = 120
    turtle.setup(width=1.0, height=1.0)
    turtle.bgcolor("black")
    turtle.color("Green")
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300, -300)
    turtle.pendown()
    for z in range(len(s)):
        if s[z] == 'F':
            turtle.forward(d)
        elif s[z] == 'G':
            turtle.forward(d)
        elif s[z] == '+':
            turtle.right(angle)
        elif s[z] == "-":
            turtle.left(angle)

    turtle.done()
    return


main()
