import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Seni Bintang Interaktif")

# Buat turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Daftar warna
colors = ["red", "gold", "cyan", "pink", "violet", "yellow", "green", "blue"]

def draw_star(size):
    """Fungsi untuk menggambar bintang dengan ukuran tertentu"""
    t.pencolor(random.choice(colors))
    t.pendown()
    t.begin_fill()
    t.fillcolor(random.choice(colors))
    
    for _ in range(5):
        t.forward(size)
        t.right(144)
    
    t.end_fill()
    t.penup()

def click_handler(x, y):
    """Handler saat layar diklik"""
    t.penup()
    t.goto(x, y)
    draw_star(random.randint(20, 80))

# Dengarkan klik mouse
screen.onscreenclick(click_handler)

# Pesan instruksi
t.penup()
t.goto(-180, 0)
t.color("white")
t.write("Klik di mana saja untuk menggambar bintang!", font=("Arial", 16, "normal"))

# Tambahkan beberapa bintang secara otomatis
for _ in range(10):
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)
    t.goto(x, y)
    draw_star(random.randint(20, 80))

# Atur mode supaya tetap berjalan sampai window ditutup
turtle.mainloop()