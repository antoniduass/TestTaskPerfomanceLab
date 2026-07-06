import sys

def fill_nums(path):
    nums = []
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                nums.append(int(line))
        return nums
    except FileNotFoundError:
        print('Файл с таким именем не найден')
        return None

def moves_counter(nums):
    nums.sort()
    median_index = len(nums)//2
    median = nums[median_index]

    total_moves = sum(abs(num - median) for num in nums)

    if total_moves <= 20:
        return total_moves
    else:
        return '20 ходов недостаточно для приведения всех элементов массива к одному числу'

def main():
    if len(sys.argv) != 2:
        print('Ошибка -- запустите скрипт так: python task4.py nums.txt')
        return

    path = sys.argv[1]

    nums = fill_nums(path)
    if not nums:
        print('Файл пуст')
        return

    total_moves = moves_counter(nums)
    print(total_moves)

if __name__ == '__main__':
    main()