import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, length, angle, depth):
    if depth == 0:
        return

    # Обчислюємо координати кінця гілки
    new_x = x + length * np.cos(angle)
    new_y = y + length * np.sin(angle)


    plt.plot([x, new_x], [y, new_y], color="black", linewidth=2)
    

    plt.draw()
    plt.pause(0.05)  # Затримка для оновлення


    new_length = length * 0.7  


    draw_branch(new_x, new_y, new_length, angle + np.pi / 4, depth - 1)  # Ліва гілка
    draw_branch(new_x, new_y, new_length, angle - np.pi / 4, depth - 1)  # Права гілка

# Налаштовуємо графік
plt.figure(figsize=(8, 8))
plt.axis("off")  


depth = 8 # Кількість запусків рекурсії
draw_branch(0, -1, 1, np.pi / 2, depth)  


plt.show()
