def quicksort(x):
    if len(x) < 2:
        return x
    else:
        pivot = x[0]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def search_position(numbers, devide_number):
    mid = 0
    start = 0
    end = len(numbers)
    step = 0
    if devide_number > numbers[-1]:
        return end
    if devide_number < numbers[0]:
        return start

    while start <= end:
        step = step + 1
        mid = (start + end) // 2
        if devide_number == numbers[mid]:
            return mid

        if devide_number < numbers[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return mid

def main():
    try:
        input_str = input("Введите числа через пробел: ")
        entries = input_str.split(" ")
        numbers = [int(i) for i in entries]
        divide_number = int(input("Введите любое число: "))
        sorted_numbers = quicksort(numbers)
        print("Отсортированный список чисел: ", sorted_numbers)
        result = search_position(sorted_numbers, divide_number)
        print("Позиция элемента в списке, который меньше введенного числа: ", result)
    except ValueError:
        print("Введены не числа")

if __name__ == '__main__':
    main()