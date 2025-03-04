import turtle
import math

# Setup layar
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Lingkaran Hipnotis")

# Buat turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Ukuran lingkaran
size = 300

# Membuat lingkaran berwarna
colors = ["blue", "purple", "red", "gold", "green", "cyan", "magenta"]
for i in range(60):
    t.pencolor(colors[i % 7])
    t.pensize(2)
    t.penup()
    t.goto(0, -size)
    t.pendown()
    
    # Hitung koordinat lingkaran
    position = size * math.sin((i * 6) * math.pi / 180)
    t.circle(size)
    size = size - 5

turtle.done()