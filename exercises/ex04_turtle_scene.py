"""Stary Night."""

__author__ = "730403454"

from turtle import Turtle, colormode, done, fillcolor


def main() -> None:
    """The entrypoint of my scene.""" 
    p: Turtle = Turtle()
    q: Turtle = Turtle()
    r: Turtle = Turtle()
    s: Turtle = Turtle()
    t: Turtle = Turtle()
    speedy: int = 100
    p.speed(speedy)
    q.speed(speedy)
    r.speed(speedy)
    s.speed(speedy)
    t.speed(speedy)
    
    draw_star(p, -400, 0, 150)
    draw_star(q, -200, 50, 100)
    draw_moon(r, 0, 100, 1)
    draw_building(s, "black", "brown", 250, -300, 50, 200)
    draw_building(t, "black", "orange", 275, -200, 10, 20)
    done()

def draw_sky(a: Turtle, color: str) -> None:
    d: float = 1300
    e: int = 0

    a.pencolor(color)
    a.fillcolor(color)
    a.penup()
    a.goto(-625, 300)
    a.pendown()
    a.begin_fill()
    while (e < 4):
        a.forward(d)
        a.right(90)
        e += 1
    a.end_fill()
    done()

def draw_star(star: Turtle, x: float, y: float, star_size: float) -> None:
    i: int = 0

    star.pencolor("orange")
    star.fillcolor("orange")
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.begin_fill()
    while (i < 5):
        star.forward(star_size)
        star.right(144)
        i += 1
    star.end_fill()
    done()

def draw_moon(f: Turtle, g: float, h: float, moon_size: float) -> None:
    j: int = 0

    f.pencolor("grey")
    f.fillcolor("grey")
    f.penup()
    f.goto(g, h)
    f.pendown()
    f.begin_fill()
    while (j < 360):
        f.forward(moon_size)
        f.right(1)
        j += 1
    f.end_fill()
    done()

def draw_building(k: Turtle, outline_color: str,fill_color: str, l: float, m: float, width: float, height: float) -> None:
    n: int = 0

    k.pencolor(outline_color)
    k.fillcolor(fill_color)
    k.penup()
    k.goto(l, m)
    k.setheading(0.0)
    k.pendown()
    k.begin_fill()
    while (n < 2):
        k.forward(width)
        k.left(90)
        k.forward(height)
        k.left(90)
        n += 1
    k.end_fill
    done()
