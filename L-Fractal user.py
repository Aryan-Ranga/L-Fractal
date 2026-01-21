import tkinter as tk
import turtle

def generatel(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for ch in current:
            next_string += rules.get(ch, ch)
        current = next_string
    return current


def drawl(t, instructions, angle, length):
    stack = []

    total_F = instructions.count("F")
    step = 0

    for ch in instructions:
        if ch == "F":
            green = 0.3 + 0.7 * (step / total_F)
            t.pencolor(0, green, 0)

            t.forward(length)
            step += 1

        elif ch == "+":
            t.right(angle)
        elif ch == "-":
            t.left(angle)
        elif ch == "[":
            stack.append((t.position(), t.heading()))
        elif ch == "]":
            pos, head = stack.pop()
            t.penup()
            t.setposition(pos)
            t.setheading(head)
            t.pendown()


def generate():
    t.clear()
    t.penup()
    t.goto(-500,0)
    t.setheading(0)
    t.pendown()

    axiom = axiom_entry.get()
    angle = float(angle_entry.get())
    iterations = int(iter_entry.get())

    rules = {}
    raw_rules = rules_entry.get().split(",")
    for rule in raw_rules:
        key, value = rule.split(":")
        rules[key.strip()] = value.strip()

    instructions = generatel(axiom, rules, iterations)

    screen.tracer(0)
    drawl(t, instructions, angle, 5)
    screen.update()


root = tk.Tk()
root.title("L-System Fractal Architect")

canvas = tk.Canvas(root, width=1300, height=900)
canvas.grid(row=0, column=0, rowspan=6)

screen = turtle.TurtleScreen(canvas)
screen.colormode(1.0)

t = turtle.RawTurtle(screen)
t.speed(0)
t.hideturtle()


tk.Label(root, text="Axiom").grid(row=0, column=1, sticky="w")
axiom_entry = tk.Entry(root)
axiom_entry.insert(0, "F")
axiom_entry.grid(row=0, column=2)

tk.Label(root, text="Rules (A:B)").grid(row=1, column=1, sticky="w")
rules_entry = tk.Entry(root)
rules_entry.insert(0, "F:F[+F]F[-F]F")
rules_entry.grid(row=1, column=2)

tk.Label(root, text="Angle").grid(row=2, column=1, sticky="w")
angle_entry = tk.Entry(root)
angle_entry.insert(0, "25")
angle_entry.grid(row=2, column=2)

tk.Label(root, text="Iterations").grid(row=3, column=1, sticky="w")
iter_entry = tk.Entry(root)
iter_entry.insert(0, "5")
iter_entry.grid(row=3, column=2)

tk.Button(root, text="Generate", command=generate).grid(row=4, column=2)

root.mainloop()
