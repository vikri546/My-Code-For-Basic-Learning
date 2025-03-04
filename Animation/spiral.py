import turtle
import colorsys

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Pelangi")

# Buat turtle
t = turtle.Turtle()
t.speed(0)  # Kecepatan maksimum
turtle.colormode(1.0)

# Sembunyikan turtle
t.hideturtle()

# Animasi spiral pelangi
n = 80
h = 0
for i in range(380):
    # Mendapatkan warna dari HSV
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    t.pencolor(c)
    
    # Mengatur ketebalan garis berdasarkan i
    t.width(i//100 + 1)
    
    # Membuat spiral
    t.forward(i)
    t.left(59)  # Coba ganti angka ini (59, 89, 144, dll)

turtle.done()