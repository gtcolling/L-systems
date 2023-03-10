# Fractal and graphic interpretation of strings
# Pentaplexity
# Alphabet: "F", "|"
# Constants: "+", "-"
# Angle = 90 degrees
# Axiom = "F++F++F++F++F"
# Rules: (F -> F++F++F|F-F++F)
# "F" - Draw a line segment
# "|" - Turn backwards (180 degrees)
# "+" - Right turn by angle
# "-" - Left turn by angle

import time
import turtle


def main():
    # starting string
    axiom = "F++F++F++F++F"
    # number of generations
    gen = 5

    # ex_1 nested forloop
    start = time.time()
    create_system(axiom, gen)
    end = time.time()
    ex1 = str(end - start) + " seconds"

    print(ex1)


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
                temp += 'F++F++F|F-F++F'
            elif s[y] == '|':
                temp += s[y]
            elif s[y] == '+':
                temp += s[y]
            elif s[y] == '-':
                temp += s[y]
        s = temp


def draw(s):
    d = 5
    angle = 36
    turtle.setup(width=1.0, height=1.0)
    turtle.bgcolor("black")
    turtle.color("blue")
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300, -450)
    turtle.pendown()
    # programming the moves for each piece of the string
    for z in range(len(s)):
        if s[z] == 'F':
            turtle.forward(d)
        elif s[z] == '|':
            turtle.left(180)
        elif s[z] == '+':
            turtle.left(angle)
        elif s[z] == "-":
            turtle.right(angle)

    turtle.done()
    return


main()