# 4.3
import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos : pos + 3] = normalized
    header = bytes(f"P6\n{width} {height}\n255\n", "ascii")
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(3)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def shader(x, y):
    # Цвета
    background = (0, 0, 0)
    foreground = (1, 1, 0)
    eyes_color = (0, 0, 0)

    cx, cy = 0.5, 0.5
    radius = 0.35**2

    dx = x - cx
    dy = y - cy

    dist = dx * dx + dy * dy  # Квадрат радиус-вектора

    angle = math.atan2(dy, dx)

    mouth_angle = math.radians(80)

    eye_x = cx + 0.05
    eye_y = cy - 0.2
    eye_radius = 0.05**2  # Квадрат радиуса глаза
    dist_eye = (x - eye_x) ** 2 + (y - eye_y) ** 2

    if dist < radius:  # Сравниваем квадраты (быстрее чем квадратный корень)
        if abs(angle) < mouth_angle / 2:
            return background

        if dist_eye < eye_radius:
            return eyes_color

        return foreground

    return background


main(shader)
