# Fractal and graphic interpretation of strings
# Bracketed L-systems and models of plants architecture
# Alphabet: "F", "[", "]"
# Constants: "+", "-"
# Angle = 22.5 degrees
# Axiom = "F"
# Rules: (F -> F[-F]F[+F][F])
# "F" - Draw a line segment
# "+" - Right turn by angle
# "-" - Left turn by angle

# Two new alphabet symbols introduced, allows us to create plant like L-Systems:
# "[" - Push the state of the turtle onto the stack
# "]" - Pop the stack and move the turtle to the state
# in between the brackets ( Ex. '[-F]' ) is like a 'branch' of our L-System

import time
import turtle


def main():
    # starting string
    axiom = "F"
    # number of generations
    gen = 6

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
                temp += 'F[-F]F[+F][F]'
            else:
                temp += s[y]
        s = temp


def draw(s):
    d = 10
    angle = 22.5
    turtle.setup(width=1.0, height=1.0)
    turtle.bgcolor("black")
    turtle.color("orange")
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(-300, -300)
    turtle.pendown()

    stack = []
    for z in range(len(s)):
        #if we encouter a pop bracket, pop the former state and move the turtle there
        if s[z] == ']':
            if not stack:
                continue
            else:
                state = stack.pop()
                turtle.penup()
                # move turtle to (xcor, ycor)
                turtle.goto(state[0], state[1])
                # move turtle head to (angle)
                turtle.setheading(state[2])
                turtle.pendown()
        # if we encounter a 'push' bracket, get the state of the turtle, x = xcor, y = ycor, a = angle, push onto the stack
        if s[z] == '[':
            #(xcor, ycor, angle)
            state = [turtle.xcor(), turtle.ycor(), turtle.heading()]
            # python version of 'push' is append, not a traditional stack
            stack.append(state)
        elif s[z] == 'F':
            turtle.forward(d)
        elif s[z] == '+':
            turtle.right(angle)
        elif s[z] == "-":
            turtle.left(angle)

    turtle.done()
    return


main()
