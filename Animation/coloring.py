import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Mandala Berwarna")

# Buat turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Warna untuk mandala
colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3", "#33FFF3"]

# Fungsi untuk menggambar lingkaran
def draw_circle(radius, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Fungsi untuk menggambar pola bunga
def draw_flower_pattern(size):
    for i in range(36):
        t.pencolor(colors[i % 6])
        t.circle(size)
        t.left(10)

# Posisi awal
t.penup()
t.goto(0, -200)
t.pendown()

# Gambar mandala
for i in range(10):
    # Warna bervariasi
    color = colors[i % 6]
    t.pensize(2)
    
    # Gambar dengan pola berbeda
    draw_flower_pattern(200 - i * 20)
    
    # Gambar lingkaran pusat
    t.penup()
    t.goto(0, -50 + i * 10)
    t.pendown()
    draw_circle(50 - i * 5, colors[-(i % 6) - 1])

turtle.done()