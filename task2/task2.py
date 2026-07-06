import sys
import math

def read_ellipse(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            x_center, y_center = map(float, lines[0].split())
            a, b = map(float, lines[1].split())

            return x_center, y_center, a ** 2, b ** 2
    except FileNotFoundError:
        print(f"Ошибка: файл эллипса по пути {path} не найден")
        return None

def read_dotes(path):
    points = []

    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if not line.strip():
                    continue
                x, y = map(float, line.split())
                points.append((x, y))
        return points
    except FileNotFoundError:
        print(f"Ошибка: файл точек по пути {path} не найден")
        return None

def get_point_position(x, y, x_center, y_center, a_square, b_square):
    result = ((x - x_center) ** 2 / a_square) + ((y - y_center) ** 2 / b_square)

    if math.isclose(result, 1.0):
        return 0
    elif result < 1.0:
        return 1
    else:
        return 2

def main():
    if len(sys.argv) != 3:
        print("Ошибка -- запустите скрипт так: python task2.py circle.txt dot.txt")
        return

    ellipse_path = sys.argv[1]
    dotes_path = sys.argv[2]

    ellipse_data = read_ellipse(ellipse_path)
    if ellipse_data is None:
        return
    x_center, y_center, a_square, b_square = ellipse_data

    dotes = read_dotes(dotes_path)
    if dotes is None:
        return

    for x, y in dotes:
        position = get_point_position(x, y, x_center, y_center, a_square, b_square)
        print(position)

if __name__ == "__main__":
    main()