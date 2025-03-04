import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pola Bunga")

# Buat turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Warna-warna untuk bunga
colors = ["red", "yellow", "blue", "green", "purple", "orange", "white", "pink"]

# Gambar pola bunga
for i in range(180):
    t.color(random.choice(colors))
    t.circle(190-i, 90)
    t.left(90)
    t.circle(190-i, 90)
    t.left(18)
    
turtle.done()