import sys

def get_path(n ,m):
    array = list(range(1, n + 1))
    double_array = array + array

    path = []
    current_index = 0

    while True:
        interval = double_array[current_index : current_index + m]

        start_val = interval[0]
        end_val = interval[-1]

        path.append(str(start_val))

        if end_val == 1:
            break

        current_index = array.index(end_val)

    return "".join(path)

def main():
    if len(sys.argv) != 5:
        print("Ошибка -- запустите скрипт так: python task1.py n1 m1 n2 m2")
        return

    n1 = int(sys.argv[1])
    m1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    m2 = int(sys.argv[4])

    path1 = get_path(n1,m1)
    path2 = get_path(n2,m2)

    print(path1 + path2)

if __name__ == "__main__":
    main()
