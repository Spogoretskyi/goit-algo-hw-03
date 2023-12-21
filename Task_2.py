import turtle
import sys


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    # Зображуємо вершину
    koch_curve(t, order, size)
    # Повертаємо на 90
    t.right(90)
    # Зображуємо праву сторону
    koch_curve(t, order, size)
    # Повертаємо на 90
    t.right(90)
    # Зображуємо низ
    koch_curve(t, order, size)
    # Повертаємо на 90
    t.right(90)
    # Зображуємо ліву сторону
    koch_curve(t, order, size)

    window.mainloop()


if __name__ == "__main__":
    try:
        order = int(input("Введіть рівень рекурсії: "))
    except:
        order = 3  # Значення за замовчуванням

    draw_koch_curve(order)
