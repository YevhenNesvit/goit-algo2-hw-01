import random

def quick_select(arr: list[int], k: int) -> int:
    """
    Знаходить k-й найменший елемент у несортованому масиві за допомогою алгоритму Quick Select.

    :param arr: Список чисел
    :param k: Позиція елемента (1-індексація)
    :return: Значення k-го найменшого елемента
    """
    if len(arr) == 1:
        return arr[0]

    # Вибір випадкового опорного елемента (pivot)
    pivot = random.choice(arr)

    # Розподіл елементів навколо опорного
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    # Визначення положення k в розбитому масиві
    if k <= len(smaller):
        # Якщо k знаходиться в "менших" елементах
        return quick_select(smaller, k)
    elif k <= len(smaller) + len(equal):
        # Якщо k знаходиться серед "рівних" елементів
        return pivot
    else:
        # Якщо k знаходиться в "більших" елементах
        return quick_select(larger, k - len(smaller) - len(equal))

# Приклад використання
array = [3, 8, 1, 5, 4, 6, 7, 2, 9]
k = 4
result = quick_select(array, k)
print(f"{k}-й найменший елемент: {result}")
