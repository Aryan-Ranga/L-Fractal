import turtle

def generate(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for char in current:
            next_string += rules.get(char, char)
        current = next_string
    return current

def draw(instructions, angle, length):
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(0)
    t.hideturtle()
    
    t.penup()
    t.goto(-200, 50)
    t.setheading(0)
    t.pendown()

    for char in instructions:
        if char == "F" or char == "G":
            t.forward(length)
        elif char == "+":
            t.left(angle)
        elif char == "-":
            t.right(angle)

    screen.mainloop()

axiom = "F-G-G"

rules = {"F": "F-G+F+G-F","G": "GG"}

iterations = 5
angle = 120
length = 5

instructions = generate(axiom, rules, iterations)
draw(instructions, angle, length)
