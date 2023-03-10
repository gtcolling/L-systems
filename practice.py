import turtle

board = turtle.Turtle()

for i in range(0, 400, 20):
    board.forward(i)
    board.right(90)

turtle.done()
