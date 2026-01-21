def generate(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for char in current:
            next_string += rules.get(char, char)
        current = next_string
    return current

import turtle

def draw(instructions, angle, length):
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-100, 0)
    t.setheading(0)
    t.pendown()

    stack = []

    for char in instructions:
        if char == "F":
            t.forward(length)
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)
        elif char == "[":
            stack.append((t.position(), t.heading()))
        elif char == "]":
            position, heading = stack.pop()
            t.penup()
            t.setposition(position)
            t.setheading(heading)
            t.pendown()

    screen.mainloop()

axiom = "F"
rules = {"F": "F[+F]F[-F]F"}

iterations = 9
angle = 25
length = 5

instructions = generate(axiom, rules, iterations)
draw(instructions, angle, length)
